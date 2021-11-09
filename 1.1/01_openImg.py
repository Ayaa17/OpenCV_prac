import cv2
import setting

file_dir = '../ex_img/01.jpg'  #路徑  ../
srcImg = cv2.imread(file_dir)

cv2.imshow("srcImg",srcImg)
cv2.waitKey(0)