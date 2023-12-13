# 모델

## 3. [MedSAM](https://github.com/bowang-lab/MedSAM)

Segment Anything in Medical Images.

### [SAM(Segment Anything Model)](https://github.com/facebookresearch/segment-anything)

-   점이나 상자와 같은 입력 프롬프트에서 고품질 개체 마스크를 생성하며 이미지의 모든 개체에 대한 마스크를 생성하는 데 사용 가능
-   1,100만 개의 이미지와 11억 개의 마스크로 구성된 데이터 세트에 대해 훈련됨
-   다양한 분할 작업에서 강력한 제로샷 성능을 발휘

### 환경 설정

```
conda create -n medsam python=3.10 -y
conda activate medsam
conda install -y pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.8 -c pytorch -c nvidia
git clone https://github.com/bowang-lab/MedSAM
cd MedSAM
pip install -e .
```

### 데이터 전처리

`train_one_gpu.py` 의 학습 스크립트를 따름
`work_dir/SAM/sam_vit_b_01ec64.pth` 를 바탕으로 학습하기에 데이터 입력 형식 맞춤

-   img
    -   shape = (1024 \* 1024 \* 3)
    -   확장자는 npy
-   mask
    -   shape = (1024 \* 1024)
    -   확장자는 npy

### 사용 방법

### 결과
