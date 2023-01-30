import cv2
import numpy as np

img = cv2.imread("img/group_poop.png")
print(img) # This image is a huge array!
print('//////')
print(img[30][30]) # This is a pixel