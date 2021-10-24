## Presentation

## Abstract
Traffic state prediction is necessary for many Intelligent Transportation Systems applications. Recent developments of the topic have focused on network-wide, multi-step prediction, where state of the art performance is achieved via deep learning models, in particular, graph neural network-based models. While the prediction accuracy of deep learning models is high, these models' robustness has raised many safety concerns, given that imperceptible perturbations added to input can substantially degrade the model performance. In this work, we propose an adversarial attack framework by treating the prediction model as a black-box, i.e., assuming no knowledge of the model architecture, training data, and (hyper)parameters. However, we assume that the adversary can oracle the prediction model with any input and obtain corresponding output. Next, the adversary can train a substitute model using input-output pairs and generate adversarial signals based on the substitute model. To test the attack effectiveness, two state of the art, graph neural network-based models (GCGRNN and DCRNN) are examined. As a result, the adversary can degrade the target model's prediction accuracy up to 54%. In comparison, two conventional statistical models (linear regression and historical average) are also examined. While these two models do not produce high prediction accuracy, they are either influenced negligibly (less than 3%) or are immune to the adversary's attack.



![](hero.png)

-------
## Link to the [paper](https://arxiv.org/abs/2110.08712)
