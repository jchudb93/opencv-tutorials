import pandas as pd
import urllib
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time
import pytesseract
from pytesseract import image_to_string
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException 
import time
from PIL import Image, ImageFilter
import numpy as np
import cv2
from datetime import datetime
import os
from selenium.webdriver.firefox.options import Options

from utils import *


def instance_driver(options, profile, binary, gecko_path):
    return webdriver.Firefox(firefox_options=options, firefox_profile=profile, firefox_binary=binary, executable_path=gecko_path)
    
def load_page(driver, url):
    driver.get(url)

def navigate_to_form(driver, xpath):
    driver = driver.find_elements_by_xpath(xpath)[1].click()    
    
def get_captcha(driver, element, path):
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = element.location
    size = element.size
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, '')  # saves new cropped image

def transform_image(image_path, output_filename='image', img_format = 'PNG'):
    
    # print(image_path)
    img = cv2.imread(image_path)
    
    img = np.array(img, dtype=np.uint8)
    
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    bilateral = cv2.bilateralFilter(blur, 5, 75, 75)
    
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

    cv2.imwrite(f'{output_filename}.{img_format}', erosion_1)