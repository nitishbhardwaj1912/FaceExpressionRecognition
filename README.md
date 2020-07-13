# Face Expression Recognition
A deep learning project[1] to detect the face expressions based on TensorFlow framework.

## Project Tasks
* Develop a facial expression recognition model in Keras
* Build and train a convolutional neural network (CNN)
* Deploy the trained model to a web interface with Flask
* Apply the model to real-time video streams and image data

## About Dataset
The data consists of 48x48 pixel grayscale images of faces. The dataset was prepared by Pierre-Luc Carrier and Aaron Courville, as part of an ongoing research project. The dataset used in this project is based on Kaggle: Facial Expression Recognition Challenge [2].

## Model
Convolutional Neural Network(CNN) is used in this project. It consists of four Convolution layers and two fully connected layer. Used Adam as the optimizer, categorical crossentropy as the loss function, and accuracy as the evaluation metric.

Model summmary:
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 48, 48, 64)        640       
_________________________________________________________________
batch_normalization (BatchNo (None, 48, 48, 64)        256       
_________________________________________________________________
activation (Activation)      (None, 48, 48, 64)        0         
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 24, 24, 64)        0         
_________________________________________________________________
dropout (Dropout)            (None, 24, 24, 64)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 24, 24, 128)       204928    
_________________________________________________________________
batch_normalization_1 (Batch (None, 24, 24, 128)       512       
_________________________________________________________________
activation_1 (Activation)    (None, 24, 24, 128)       0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 12, 12, 128)       0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 12, 12, 128)       0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 12, 12, 512)       590336    
_________________________________________________________________
batch_normalization_2 (Batch (None, 12, 12, 512)       2048      
_________________________________________________________________
activation_2 (Activation)    (None, 12, 12, 512)       0         
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 6, 6, 512)         0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 6, 6, 512)         0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 6, 6, 512)         2359808   
_________________________________________________________________
batch_normalization_3 (Batch (None, 6, 6, 512)         2048      
_________________________________________________________________
activation_3 (Activation)    (None, 6, 6, 512)         0         
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 3, 3, 512)         0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 3, 3, 512)         0         
_________________________________________________________________
flatten (Flatten)            (None, 4608)              0         
_________________________________________________________________
dense (Dense)                (None, 256)               1179904   
_________________________________________________________________
batch_normalization_4 (Batch (None, 256)               1024      
_________________________________________________________________
activation_4 (Activation)    (None, 256)               0         
_________________________________________________________________
dropout_4 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               131584    
_________________________________________________________________
batch_normalization_5 (Batch (None, 512)               2048      
_________________________________________________________________
activation_5 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_5 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 7)                 3591      
=================================================================
Total params: 4,478,727
Trainable params: 4,474,759
Non-trainable params: 3,968

## Model Training and Evaluation
It took me around 30 minutes to train and validate the model on GPU: 4 GB Nvidia GeForce GTX 1050 Ti and CPU: i5 8th Gen. 

<p align="center">
  <img src="Images\Accuracy.png" alt="Accuracy and Loss Graph">
</p>

## References:
[1] Coursera. 2020. Project Certificate. [online] Available at: <https://www.coursera.org/account/accomplishments/records/ZXZMTPWDD9EF> [Accessed 8 July 2020].

[2] Kaggle.com. 2020. Challenges In Representation Learning: Facial Expression Recognition Challenge | Kaggle. [online] Available at: <https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/overview/evaluation> [Accessed 1 July 2020].
