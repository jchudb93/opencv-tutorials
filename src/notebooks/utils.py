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
    top = location['y'] + 140
    right = location['x'] + size['width']
    bottom = location['y'] + size['height'] + 140

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'jpeg')  # saves new cropped image
