import os
import torch
import shutil
import numpy as np

from PIL import Image
from tqdm import tqdm
from urllib.request import urlretrieve


class MRDataset(torch.utils.data.Dataset):
    def __init__(self, root, mode="train", transform=None):

        assert mode in {"train", "valid", "test"}

        self.root = root
        self.annot_home = f"{root}/train_annot_2"
        self.mode = mode
        self.transform = transform

        self.images_directory = os.path.join(self.root, "images_2")
        self.masks_directory = os.path.join(self.root, "mask_2")

        self.filenames = self._read_split()  # read train/valid/test splits

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):

        filename = self.filenames[idx]
        image_path = os.path.join(self.images_directory, filename[1:])
        mask_path = os.path.join(self.masks_directory, filename)#.replace("jpg", "png"))
        image = np.array(Image.open(image_path).convert("RGB"))

        trimap = np.array(Image.open(mask_path))
        mask = self._preprocess_mask(trimap)
        mask = np.mean(mask, axis=2)
        sample = dict(image=image, mask=mask, f_n = filename)
        if self.transform is not None:
            sample = self.transform(**sample)

        return sample

    @staticmethod
    def _preprocess_mask(mask):
        mask = mask.astype(np.float32)
        mask[mask<128] = 0.0
        mask[mask>=128] = 1.0
        return mask

    def _read_split(self):
        split_filename = "annot_train.txt"
        split_filepath = os.path.join(self.annot_home, split_filename)
        with open(split_filepath) as f:
            split_data = f.read().strip("\n").split("\n")
        filenames = [x.split(" ")[0] for x in split_data]
        if self.mode == "valid":  # 10% for validation
            filenames = [x for i, x in enumerate(filenames) if (i % 30 < 3)]
        elif self.mode == "test": # 10% for test
            filenames = [x for i, x in enumerate(filenames) if (i % 30 == 3) or (i % 30 == 4) or (i % 30 == 5)]
        elif self.mode == "train":  # 80% for train
            filenames = [x for i, x in enumerate(filenames) if i % 30 > 5]
        return filenames


class SimpleMRDataset(MRDataset):
    def __getitem__(self, *args, **kwargs):

        sample = super().__getitem__(*args, **kwargs)

        # resize images
        image = np.array(Image.fromarray(sample["image"]).resize((256, 256), Image.BILINEAR))
        mask = np.array(Image.fromarray(sample["mask"].squeeze()).resize((256, 256), Image.NEAREST))

        # convert to other format HWC -> CHW
        sample["image"] = np.moveaxis(image, -1, 0)
        sample["mask"] = np.expand_dims(mask, 0)
        a = sample["image"]
        b = sample["mask"]

        return sample

