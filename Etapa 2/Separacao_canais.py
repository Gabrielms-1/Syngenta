import cv2
import numpy as np
import os

BGRA = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA) 
print(BGRA.shape)


redChannel = BGRA[:,:,2]
redImg = np.zeros(img.shape)
redImg[:,:,2] = redChannel

greenChannel = BGRA[:,:,1]
greenImg = np.zeros(img.shape)
greenImg[:,:,1] = greenChannel

blueChannel = BGRA[:,:,0]
blueImg = np.zeros(img.shape)
blueImg[:,:,0] = blueChannel


cv2.imwrite('cv2-red-channel.png', redImg) 
cv2.imwrite('cv2-green-channel.png', greenImg) 
cv2.imwrite('cv2-blue-channel.png', blueImg) 

