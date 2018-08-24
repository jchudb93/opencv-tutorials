import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


DATA = '../img'

print(os.getcwd())

img = cv2.imread(f'{DATA}/music_sheet.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bw = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
cv2.imshow('image', bw)
cv2.waitKey(0)
cv2.destroyAllWindows()