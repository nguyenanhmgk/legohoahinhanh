import cv2
import numpy  as np

lego_brick = cv2.imread("1x1.png")
size = 15
lego_brick = cv2.resize(lego_brick, (size,size)).astype(np.int64)

image = cv2.imread("input.jpg")
image = cv2.resize(image, (image.shape[1] // size * size, image.shape[0] // size * size))
height, width , channels = image.shape
for i in range(width // size):
    for j in range(height // size):
        cell = image[j * size: (j + 1) * size, i * size : (i + 1) * size, : ]
        avg_color= np.mean(cell, axis=(0,1))
        image[j * size: (j + 1) * size, i * size: (i + 1) * size, :] = np.clip(avg_color + lego_brick, 0 , 255 )
cv2.imwrite("output.jpg", image)
