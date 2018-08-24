import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


DATA = '../img'

print(os.getcwd())

img = cv2.imread(f'{DATA}/captcha.PNG')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bw = cv2.adaptiveThreshold(
    ~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY, 15, -2)

horizontal = bw.copy()
vertical = bw.copy()

horizontal_length = int(horizontal.shape[1] / 20)
print("horizontal length ", horizontal_length)
horizontal_structure = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (horizontal_length, 1))

horizontal = cv2.erode(horizontal, horizontal_structure, (-1, -1))
horizontal = cv2.dilate(horizontal, horizontal_structure, (-1, -1))

vertical_length = int(vertical.shape[1] / 60)

vertical_structure = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (1, vertical_length))

print("vertical length ", vertical_length)

vertical = cv2.erode(vertical, vertical_structure, (-1, -1))
vertical = cv2.dilate(vertical, vertical_structure, (-1, -1))
cv2.imshow('image', vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
