import cv2
import numpy as np

img = cv2.imread('welcometocat.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('test1', img)
cv2.imshow('test2', gray)
cv2.waitKey()
#cv2.destroyAllWindow()
