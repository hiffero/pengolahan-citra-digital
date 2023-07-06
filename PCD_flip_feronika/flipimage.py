import cv2

# Load image
img = cv2.imread('fero.jpg')

# Flip image
flipped_img = cv2.flip(img, 0)
flipped_img = cv2.flip(img, 1)
flipped_img = cv2.flip(img, -1)

# Display original and flipped images
cv2.imshow('Original Image', img)
cv2.imshow('Flipped Image', flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
