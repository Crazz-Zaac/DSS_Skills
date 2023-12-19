import cv2
import json
import numpy as np

np.random.seed(23272000)


num = np.random.randint(100)
img1 = cv2.imread('Mini_BAGLS_dataset/'+str(num)+'.png')
img2 = cv2.imread('Mini_BAGLS_dataset/'+str(num)+'_seg.png')
with open('Mini_BAGLS_dataset/'+str(num)+'.meta', 'r') as info:
    file = json.load(info)
    header = file.get('Subject disorder status', 'No Title')
    