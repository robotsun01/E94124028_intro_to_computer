import cv2
import numpy as np
image = cv2.imread("TW.jpg") #圖片讀取
cv2.imshow("normalphoto", image) #一般圖片

B,G,R = cv2.split(image)#不用函式轉詼諧
zeros = np.zeros(image.shape[:2],dtype="uint8")
li= (B+G+R)//3

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#用函式轉詼諧

ret, output = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY) #二值化

cv2.imshow("Nogray",li) #照片輸出
cv2.imshow("Gray",gray)
cv2.imshow("MoreGray", output)
cv2.waitKey(0)   #等任意鍵被按下
cv2.destroyAllWindows()    #關閉視窗