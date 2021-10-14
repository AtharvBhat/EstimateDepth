# EstimateDepth
Single Image Depth Estimation project done for our computer vision class.

# Problem statement :- 
Predicting Depth from a single image is a difficult task. Multiple different arrangements of different objects in 3 dimensions may have the same 2d representation which makes it a many to one mapping. Thus estimating depth from a single image is a challenging task.

At its core it is an Image -> Image translation task which has been tackled in multiple different ways. The simplest method would be to use a Fully convolutional neural network such as a UNET which is widely used in other image to image translation tasks such as image segmentation and train it in a supervised manner using an l1 or l2 penalty. 
In recent years, models trained using adversarial loss have also emerged as a popular method to solve image to image translation tasks such as Pix2Pix.

In this project we aim to compare the performance of the same generator / translation model (UNET) which will be trained using a l1 / l2 penalty and again using a combination of content loss (l1 / l2 loss) and the adversarial loss.

// Add images here


# Team Members :- 
* Atharv Bhat
* Mayukh Ghosh
* Valay Shah
