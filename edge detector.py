import cv2
import matplotlib.pyplot as plt
im = cv2.imread('umbrella.jpg')
edge = cv2.Canny(im,100,300)
plt.imshow(edge)
plt.show()
