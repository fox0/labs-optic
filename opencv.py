import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img.bmp')
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)

MAGIC = 645
ysize, xsize, _ = dst.shape

plt.imshow(dst)
plt.xticks(np.arange(0, xsize, MAGIC), labels=np.arange(0, 1000, 100))
plt.yticks(np.arange(0, ysize, MAGIC), labels=np.arange(0, 1000, 100))
plt.show()

# frame = cv2.imread('img.bmp')
#
#
# # Convert BGR to HSV
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
# # define range of blue color in HSV
# lower_blue = np.array([110, 50, 50])
# upper_blue = np.array([130, 255, 255])
#
# # Threshold the HSV image to get only blue colors
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
#
# # Bitwise-AND mask and original image
# res = cv2.bitwise_and(frame, frame, mask=mask)
#
# cv2.imshow('frame', frame)
# cv2.imshow('mask', mask)
# cv2.imshow('res', res)
# # k = cv2.waitKey(5) & 0xFF
# # if k == 27:
# #     break
# cv2.w
# cv2.destroyAllWindows()
