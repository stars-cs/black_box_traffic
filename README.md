## Black-box Adversarial Attacks on Network-wide Multi-step Traffic State Prediction Models

[Paper](https://arxiv.org/abs/2110.08712),  [Website](https://stars-cs.github.io/black_box_traffic/),  [Slides](https://github.com/stars-cs/black_box_traffic/blob/gh-pages/Black%20Box%20Adversarial%20Attacks.pdf), [Video](https://www.youtube.com/watch?v=yxOBCIl1o-Y)

------

1. Major Code Dependencies

Python = 3.6.5
TensorFlow = 1.8.0 (For GCGRNN and DCRNN)
PyTorch = 1.8.0 (For ResNet50)
AdverTorch


2. Understanding the code:
The code given here assumes you have pretrained models for GCGRNN and DCRNN. To learn more about how to train them, please refer:

-  GCGRNN code: https://github.com/leilin-research/GCGRNN
-  DCRNN code: https://github.com/liyaguang/DCRNN

Essentially, for each type of model all other code is contained in 7 Jupyter Notebooks:
- Part_0_(Model_Name)_preds_on_training

-----
Result Display
<img width="1197" alt="hero" src="https://user-images.githubusercontent.com/15305740/138611368-770e1c71-30d3-42ff-8ddf-cba7de80cf29.png">

References:

