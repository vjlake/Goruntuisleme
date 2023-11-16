#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import numpy as np
cap=cv2.VideoCapture(0)
sinirdeg=50 #sinirdegeri_fark_hassasiyetini_ayarliyor

while cap.isOpened():
    ret,frame=cap.read()
    T=np.array([[0 for dim1 in range(len(frame[0]))]for dim2 in range(len(frame))],dtype="uint8")
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    B=frame[:,:,0]
    G=frame[:,:,1]
    R=frame[:,:,2]
    for de0 in range(len(frame)):
        for c1 in range(len(frame[de0])):
            if frame[de0][c1][2]==max(frame[de0][c1]):
                if (frame[de0][c1][2]-frame[de0][c1][1])>sinirdeg:
                    if (frame[de0][c1][2]-frame[de0][c1][0])>sinirdeg:
                        T[de0][c1]=255
            B[de0][c1]=0
            G[de0][c1]=0
    sonuc=cv2.merge((B,G,T))
    cv2.imshow("kizil",sonuc)
    
    
cap.release()
cv2.destroyAllWindows()


# In[ ]:




