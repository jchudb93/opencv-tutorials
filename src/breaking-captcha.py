import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


DATA = '../img'

# https://training.play-with-docker.com/ops-s1-hello


print(os.getcwd())

img = cv2.imread(f'{DATA}/captcha.PNG')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# gray[(gray == 140)] = 0

bilateral = cv2.bilateralFilter(gray, 3, 75, 75)
ret, thresh = cv2.threshold(
    bilateral,
    25,
    255,
    cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# Kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# other things
erosion = cv2.erode(thresh, kernel, iterations=1)
closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel, iterations=1)

# Transform image
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(
    dist_transform,
    0.02*dist_transform.max(),
    255,
    cv2.THRESH_BINARY)
# ,255,0)

# kernel_1
kernel_1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 2))

dilation_1 = cv2.dilate(sure_fg, kernel_1, iterations=2)
erosion_1 = cv2.erode(dilation_1, kernel_1, iterations=3)

cv2.imshow("img", erosion_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
