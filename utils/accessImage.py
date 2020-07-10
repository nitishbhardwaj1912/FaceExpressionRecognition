import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def plot_example_images(plt, dirName):
    '''
    A function to print the images from different directories of the dataset.
    
     Parameters:
            plt: matplot object
            dirName(str): directory name to be accessed

    Returns:
            plt: Returns plt object having images from the directory
    '''
    img_size = 48
    plt.figure(0, figsize=(12,20))
    ctr = 0
    dirName = dirName + "/"
    
    for expression in os.listdir(dirName):
        for i in range(1,6):
            ctr += 1
            plt.subplot(7,5,ctr)
            img = load_img(dirName + expression + "/" +os.listdir(dirName + expression)[i], target_size=(img_size, img_size))
            plt.imshow(img, cmap="gray")
    
    plt.tight_layout()
    return plt
