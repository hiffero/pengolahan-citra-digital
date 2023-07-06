import cv2
import numpy as np

# Load the image
img = cv2.imread('p1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the histogram of the grayscale image
hist,bins = np.histogram(gray.flatten(),256,[0,256])

# Calculate the cumulative distribution function (CDF) of the histogram
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

# Perform contrast stretching
equ = cv2.equalizeHist(gray)

# Display the original and enhanced images
# cv2.imshow('Original Image', gray)
cv2.imshow('Enhanced Image', equ)
cv2.waitKey(0)
cv2.destroyAllWindows()