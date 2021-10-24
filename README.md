## Black-box Adversarial Attacks on Network-wide Multi-step Traffic State Prediction Models

[Paper](https://arxiv.org/abs/2110.08712),  [Website](https://stars-cs.github.io/black_box_traffic/),  [Slides](https://github.com/stars-cs/black_box_traffic/blob/gh-pages/Black%20Box%20Adversarial%20Attacks.pdf), [Video](https://www.youtube.com/watch?v=yxOBCIl1o-Y)

------

1. Major Code Dependencies
```
Python = 3.6.5
TensorFlow = 1.8.0 (For GCGRNN and DCRNN)
PyTorch = 1.8.0 (For ResNet50)
AdverTorch
```

2. Dataset:
The data was downloaded from [CalTrans](https://dot.ca.gov) by following the procedure given [here](https://github.com/leilin-research/GCGRNN/blob/master/Download_and_Process_PEMS_traffic_volume_data.ipynb) for obtaining and preprocessing (including train, test split). The dates for data collected range from Jan 1, 2018 to Jun 30, 2019.

4. Understanding the code:
The code given here assumes you have pretrained models for GCGRNN and DCRNN. To learn more about how to train them, please refer:

-  GCGRNN code: https://github.com/leilin-research/GCGRNN
-  DCRNN code: https://github.com/liyaguang/DCRNN

Essentially, for each type of model all other code is contained in 7 Jupyter Notebooks:
- Part_0_(Model_Name)_preds_on_training : See model performance on training data
- Part_1_Run_Pretrained_(Model_Name)_in_test.ipynb : Obtain trained model performance and also the output on the test data
- Part_2_Train_new_CNN_(Model_Name).ipynb: Train ResNet50 model on the (test input, predictions) pairs to mimic the target model
- Part_3_Generate_Adversarial_for_new_CNN.ipynb : Generate adversarial examples for a trained ResNet50 model
- Part_4_Error_Results_FGSM.ipynb : See model performance in Adversarial Signals from FGSM
- Part_5_Error_Results_BIM.ipynb : See model performance in Adversarial Signals from BIM
- Part_6_common_viz.ipynb: Generate images/ visualizations presented in the paper

__Other files and folders:__
-

-----
Result Display
<img width="1197" alt="hero" src="https://user-images.githubusercontent.com/15305740/138611368-770e1c71-30d3-42ff-8ddf-cba7de80cf29.png">

References:

