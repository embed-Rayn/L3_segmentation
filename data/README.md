# 데이터

## 전처리

-   ~~train 데이터 1차 전처리~~ [[ipynb 파일](./preprocess_script/train_preprocess_1.ipynb)]
    -   ~~HU 값 적용된 데이터셋 (900개)~~ : **미사용**으로 삭제
    -   사용처: `SMP` 모델에 사용
    -   분석
        -   학습에 적용하기 어려운 데이터셋
        -   HU 값이 적용되어 학습에 방해 될 것으로 판단
        -   아래 test 셋으로 사용
        -   성능 평가 시 예측 마스크에 HU값을 이용한 후처리 진행해야함

<br/>

-   **train 데이터 2차 전처리** [[ipynb 파일](./preprocess_script/train_preprocess_2.ipynb)]
    -   `SMP` 모델 학습에 직접 사용하는 데이터 셋(1078개) : ./data_train
        -   train: 862개, validation: 108개, test: 108개
    -   image
        -   40 ~ 400 윈도잉 적용
    -   mask: S[파일이름], M[파일이름], V[파일이름]
        -   0: background, 1:Subcutaneous fat
        -   0: background, 1:Muscle
        -   0: background, 1:Visceral fat

<br/>

-   **train 데이터 3차 전처리**
    -   train 데이터 2차 전처리를 폴더별 분리
    -   mask파일 3개를 하나로 합침
    -   `nnUNet`학습에 직접 사용하는 데이터 셋(1078개) : ./data_train2
        -   train: 862개, validation: 108개, test: 108개
    -   image
        -   40 ~ 400 윈도잉 적용
    -   mask: 0: background, 1:subcutaneous fat, 2:muscle, 3:visceral fat

<br/>

-   **test 데이터 전처리** [[ipynb 파일](./preprocess_script/test_preprocess_1.ipynb)]
    -   HU 값 적용된 데이터셋 (900개) : ./data_test
    -   image
        -   40 ~ 400 윈도잉 적용
    -   mask - 0: background, 1:subcutaneous fat, 2:muscle, 3:visceral fat
    -   분석
        -   학습에 적용하기 어려운 데이터셋
        -   HU 값이 적용되어 학습에 방해 될 것으로 판단
        -   test 셋으로 사용
        -   성능 평가 시 예측 마스크에 HU값을 이용한 후처리 진행해야함
