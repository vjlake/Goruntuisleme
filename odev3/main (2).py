#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

img = cv2.imread('recep.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, thresh = cv2.threshold(gray, 157, 255, cv2.THRESH_BINARY)
#sadece yatay olanları buluyor metod
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rice_grains = []

for contour in contours:
    area = cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(w)/h
    if area > 100 and aspect_ratio > 1.5 and aspect_ratio < 3.5:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
        rice_grains.append((x, y, w, h))

pSayi = len(rice_grains)

print("Total number of rice grains:",pSayi)
thresh=cv2.resize(thresh, (500, 600))
cv2.imshow("tresh sonucu",thresh)
img=cv2.resize(img, (500, 600))
cv2.imshow('secilebilenler', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

