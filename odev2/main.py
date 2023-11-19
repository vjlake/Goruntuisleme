#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np
cap=cv2.VideoCapture(0)
sinirdeg=72
while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    B=frame[:,:,0]
    G=frame[:,:,1]
    R=frame[:,:,2]
    B=255-B
    G=255-G
    B=B/255  #mavi ve yesil ne kadar siyahsa 1e ne kadar beyazsa 0 a o kadar yakin olacak
    G=G/255
    T=R*G*B
    T=np.array(T,dtype="uint8")
    B=np.array(B,dtype="uint8")
    G=np.array(G,dtype="uint8")
    T=cv2.inRange(T,sinirdeg,255)
    sonuc=cv2.merge((B,G,T))
    cv2.imshow("kizil",sonuc)

cap.release()
cv2.destroyAllWindows()

