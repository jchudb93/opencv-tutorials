import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


DATA = '../img'

print(os.getcwd())

img = cv2.imread(f'{DATA}/captcha.PNG', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()