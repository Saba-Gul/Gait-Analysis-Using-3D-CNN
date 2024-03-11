import cv2 # Importing the OpenCV library for image processing
import numpy as np # Importing the NumPy library for numerical operations
import matplotlib.pyplot as plt # Importing the Matplotlib library for data visualization

# Reading the image 'dd.png' in grayscale mode
img = cv2.imread('dd.png',0)

# Defining the structuring elements for dilation and erosion
kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(2,2))
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))

# Displaying the original image
plt.imshow(img)

# Performing dilation on the image with the specified kernel and number of iterations
dilation = cv2.dilate(img,kernel,iterations =7)

# Displaying the dilated image
plt.imshow(dilation)

# Performing erosion on the dilated image with the specified kernel and number of iterations
erosion = cv2.erode(dilation,kernel,iterations =4)

# Displaying the eroded image
plt.imshow(erosion)

# Performing dilation on the eroded image with the specified kernel and number of iterations
d2 = cv2.dilate(erosion,kernel,iterations =4)

# Displaying the dilated image
plt.imshow(d2)

# Performing erosion on the dilated image with the specified kernel and number of iterations
e2 = cv2.erode(d2,kernel,iterations =1)

# Displaying the eroded image
plt.imshow(erosion)

# Performing dilation on the eroded image with the specified kernel and number of iterations
d3 = cv2.dilate(e2,kernel1,iterations =2)

# Displaying the dilated image
plt.imshow(d3)

# Performing erosion on the dilated image with the specified kernel and number of iterations
erosion = cv2.erode(dilation,kernel,iterations =1)

# Displaying the eroded image
plt.imshow(erosion)