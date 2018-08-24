import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


DATA = '../img'

print(os.getcwd())

img1 = cv2.imread(f'{DATA}/captcha.PNG')

ret, mask = cv2.threshold(img1, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.biwsise
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()