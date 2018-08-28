import cv2
import numpy as np
import matplotlib.pyplot as plt


DATA = '../img'

img = cv2.imread(f'{DATA}/sat.jpg')

green = img[:, :, 0]


cv2.imshow("img", green)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(f'{DATA}sat-output.jpg', green)
