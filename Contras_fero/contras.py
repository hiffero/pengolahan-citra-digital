import cv2
import numpy as np

def contrast_stretching(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the minimum and maximum pixel values
    min_val = np.min(gray)
    max_val = np.max(gray)

    # Calculate the stretching range
    range_val = max_val - min_val

    # Perform contrast stretching
    stretched = cv2.normalize(gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    return stretched

# Load an image
image = cv2.imread('3.jpg')

# Apply contrast stretching
result = contrast_stretching(image)

# Display the result
cv2.imshow('Original', image)
cv2.imshow('Contrast Stretched', result)
cv2.waitKey(0)
cv2.destroyAllWindows()