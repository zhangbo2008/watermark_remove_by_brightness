import cv2
a=cv2.imread('999.jpg',0)
a[a>90]=255
cv2.imwrite('100.png',a)