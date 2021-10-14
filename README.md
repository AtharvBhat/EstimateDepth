# EstimateDepth

Predicting Depth from a single image is a difficult task. Multiple different arrangements of different objects in 3 dimensions may have the same 2d representation which makes it a many to one mapping. Thus estimating depth from a single image is a challenging task.

At its core it is an Image -> Image translation task which has been tackled in multiple different ways. The simplest method would be to use a Fully convolutional neural network such as a UNET which is widely used in other image to image translation tasks such as image segmentation and train it in a supervised manner using an l1 or l2 penalty. 
In recent years, models trained using adversarial loss have also emerged as a popular method to solve image to image translation tasks such as Pix2Pix.

In this project we aim to compare the performance of the same generator / translation model (UNET) which will be trained using a l1 / l2 penalty and again using a combination of content loss (l1 / l2 loss) and the adversarial loss.

# Dataset
We will be using the NYU-Depth-v2 Dataset for both training and evaluation
https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html

# Model Trained with Content loss only (l1 / l2 loss)
![alt text](https://github.com/AtharvBhat/EstimateDepth/blob/main/figures/Unetl2.png?raw=true)

# Model Trained with a combination of Adversarial loss and Content loss
![alt text](https://github.com/AtharvBhat/EstimateDepth/blob/main/figures/UnetGAN.png?raw=true)

# Team Members :- 
* Atharv Bhat (arb881@nyu.edu)
* Mayukh Ghosh (mg5610@nyu.edu)
* Valay Shah (vs2393@nyu.edu)
