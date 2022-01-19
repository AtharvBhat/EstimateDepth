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

# Results
We observed that the models trained withℓ2loss wasn’t able to accurately predict the depthof the input image.  The output depth values are highly correlated to the pixel intensityvalues.  Brighter objects in the scene always end up being predicted as being far and themodel shows complete disregard for the actual scene of the image and focuses too much onthe RGB pixel intensities.

![alt text](https://raw.githubusercontent.com/AtharvBhat/EstimateDepth/main/figures/result.png)

UNet model trained with scale invariant lossis better than the UNet model trained with $\ell_2$ loss at predicting the depth of the scene butthe outputs lack detail and are blurry.  The depths predicted by the UNet Model trained with a combination of scale invariant and Adversarial loss have a much clearer and less blurry depth map prediction. Unfortunately, from the metrics, while the outputs look more plausible and realistic, they are inaccurate.

Our paper can be found [here](https://github.com/AtharvBhat/EstimateDepth/blob/main/CV_Project_Report.pdf)

|Metric   |Unet($\ell$_2)   |  Unet(scale inv.) |  Unet(Adversarial) |
|---|:-:|:-:|:-:|
| RMSE (linear)  | 2.0761  | 1.6827  | 4.2640  |
| RMSE (log)  | 0.2648  | 0.2308  |  0.5531 |
| RMSE (log, scale inv.)  | 0.1436  |  0.1116 |  0.1354 |

# Team Members :- 
* Atharv Bhat (arb881@nyu.edu)
* Mayukh Ghosh (mg5610@nyu.edu)
* Valay Shah (vs2393@nyu.edu)
