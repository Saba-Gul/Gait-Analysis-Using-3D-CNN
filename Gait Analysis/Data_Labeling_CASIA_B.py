import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pickle
import random
from tqdm import tqdm

DATADIR = "acasia\\train\\"  # directory for the images
CATEGORIES = ['001','002','003',...,'123','124']  # list of categories for the images

# Display each image in the categories
for category in CATEGORIES: 
   path = os.path.join(DATADIR,category)  # create path to the images
   for img in os.listdir(path):  # iterate over each image per dogs and cats
       img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
       plt.imshow(img_array, cmap='gray')  # graph it
       plt.show()  # display!
       break  # we just want one for now so break
   break  #...and one more!

IMG_SIZE = 120  # resize the image to this size

# Resize the image and display it
img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE) 
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap='gray')
plt.show()

# Create a list for storing the training data
training_data = []

def create_training_data():
   for category in CATEGORIES: 
       path = os.path.join(DATADIR,category)  # create path to silhouettes
       class_num = CATEGORIES.index(category)  # get the classification 
       
       for img in tqdm(os.listdir(path)):  # iterate over each image for each category 
           try:
               img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
               new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
               training_data.append([new_array, class_num])  # add this to our training_data
           except Exception as e:  # in the interest in keeping the output clean...
               pass

# Shuffle the training data
random.shuffle(training_data)

# Separate the features and labels from the training data
X = []
y = []
for features,label in training_data:
   X.append(features)
   y.append(label)

# Display the shape of the first item in the feature list
print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

# Convert the features and labels into numpy arrays
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# Save the features and labels into pickle files
pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()

# Load the features and labels from the pickle files
pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)