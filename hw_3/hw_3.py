import cv2
import numpy as np
import json

with open('Mini_BAGLS_dataset/0.meta', 'r') as fol:
    info = json.load(fol)
header = info.get('Subject disorder status', 'No Title')
    
color = (0, 0, 255)
img1 = cv2.imread('Mini_BAGLS_dataset/0.png')
img2 = cv2.imread('Mini_BAGLS_dataset/0_seg.png')

color_layer = np.zeros_like(img1)
color_layer[:] = color
template_img = np.where(img2 == 255, color_layer, img1)
cv2.imshow(header, template_img)
cv2.waitKey(0)