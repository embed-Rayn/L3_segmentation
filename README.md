# L3_segmentation

근감소증 환자를 판별하기 위해 L3 부위 피하지방, 근육, 내장지방을 세그멘테이션 하는 프로젝트

![process](./documentation/assets/process2.png)

---

## INTRO

-   근감소증
    -   sarcopenia는 근육량 감소, 근력 감소, 근지구력 감소를 특징으로 하는 근육 질환
    -   sarcopenia는 노화, 만성질환, 약물 부작용 등으로 인해 발생할 수 있으며, 사망 위험을 증가시킴
-   AI를 적용하는 이유
    -   정확하고 신속한 진단
    -   개별적인 특성 고려
    -   효과적인 치료
-   기대 효과
    -   AI는 sarcopenia의 진단 및 치료에 있어 중요한 역할을 할 것으로 기대
    -   정확하고 효과적으로 진단하고 치료

---

---

## 모델

### 1. [SMP(segmentation_models.pytorch)](https://github.com/qubvel/segmentation_models.pytorch/tree/master)

#### [프로젝트 세부 내용](./models/SMP/README.md)

#### 결과

-   결과분석(아래 3epoch 학습 결과)

    -   1000 epoch 학습한 결과 intensity에 따라 segmentation은 잘 됨.
    -   그러나 [binary segmentation 예제](https://github.com/qubvel/segmentation_models.pytorch/blob/master/examples/binary_segmentation_intro.ipynb)바탕으로 전처리 및 학습을 하였고, 위 예제에는 두 class가 한 사진에 동시 등장하지 않으므로 설계 구조 자체가 다르기에 동시에 여러 클래스를 나타낼 수 없으므로 아래와 같이 loss가 낮아지도록 몸통 전체를 잡아냄.
    -   결과: 실패
    -   보완점: 다중 클래스, 한 이미지 동시 등장하도록 전처리, 설계를 바꿔야함.

    ![smp_rst_mini](./documentation/assets/smp_result1.png)

---

### 2. [nnUNet](https://github.com/MIC-DKFZ/nnUNet)

#### [프로젝트 세부 내용](./models/nnUNet/README.md)

#### 결과

-   결과분석

    -   73epoch에서 가장 낮은 validation loss가 나옴
    -   visceral fat에서 intentsity가 낮은 부분은 제외하고 mask를 그림
    -   기존 모델에 비해 준수한 성능

-   predict test set

|                | Sfat       | muscle     | Vfat       |
| -------------- | ---------- | ---------- | ---------- |
| IoU            | 0.95033022 | 0.89425196 | 0.91567544 |
| f1_macro score | 0.98567289 | 0.96375608 | 0.97519908 |
| accuacy        | 0.99475716 | 0.97857931 | 0.99035207 |
| dice_score     | 0.97432034 | 0.94070718 | 0.95585051 |

![nnunet_result1](./documentation/assets/nnunet_result1.png)

-   nnUNet모델: **predict test set(HU 적용된 테스트 셋 900개)**

|            | Sfat     | muscle   | Vfat     |
| ---------- | -------- | -------- | -------- |
| IoU        | 0.906541 | 0.80487  | 0.851837 |
| F1 score   | 0.971276 | 0.936495 | 0.9549   |
| accuacy    | 0.994272 | 0.977522 | 0.99231  |
| dice_score | 0.945715 | 0.885566 | 0.913961 |

![nnunet_result2](./documentation/assets/nnunet_result2.png)

-   기존 모델: **predict test set(HU 적용된 테스트 셋 900개 중 149개)**

|            | Sfat     | muscle   | Vfat     |
| ---------- | -------- | -------- | -------- |
| IoU        | 0.810893 | 0.807782 | 0.729217 |
| F1 score   | 0.938769 | 0.938475 | 0.905202 |
| accuacy    | 0.988644 | 0.978098 | 0.9796   |
| dice_score | 0.883777 | 0.88919  | 0.821543 |

---

### 3. [MedSAM](https://github.com/bowang-lab/MedSAM)

#### [프로젝트 세부 내용](./models/MedSAM/README.md)

#### 결과

-   RTX 3080 단일 GPU, 1080개 데이터 학습 기준 1epoch 당 3시간 소요
-   45 epoch 중 34 epoch 결과 아래 표시
-   낮은 성능 및 열화 발생 - 더 많은 학습 필요할 것으로 보임
    ![sam_loss](documentation/assets/MedSAM_loss.png)
    ![sam_rst_1](documentation/assets/sam_rst_1.png)
    ![sam_rst_2](documentation/assets/sam_rst_2.png)
    ![sam_rst_3](documentation/assets/sam_rst_3.png)
    ![sam_rst_4](documentation/assets/sam_rst_4.png)

---
