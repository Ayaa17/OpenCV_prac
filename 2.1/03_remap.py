from math import radians,cos,sin

import cv2
import numpy as np


'''旋轉用'''
def getRotationMatrix2D(theta, cx=0, cy=0):
    # 角度值转换为弧度值
    # 因为图像的左上角是原点 需要×-1
    theta = radians(-1 * theta)
    M = np.float32([
        [cos(theta), -sin(theta), (1-cos(theta))*cx + sin(theta)*cy],
        [sin(theta), cos(theta), -sin(theta)*cx + (1-cos(theta))*cy]])
    return M



f_dir= '../ex_img/05.jpg'
src_img = cv2.imread(f_dir)
if(src_img.all()==None):
    print("load src_img fail!!!")
else:
    a=src_img.shape
    b = 1 #縮小倍數
    c = int(a[0]/b)
    r = int(a[1]/b)
    print(r,c)

    cx = int(c / 2)
    cy = int(r / 2)

    new=cv2.resize(src_img,(r,c),interpolation=cv2.INTER_AREA)

    M = getRotationMatrix2D(0, cx=cx, cy=cy)
    rotated_30 = cv2.warpAffine(src_img, M, (r, c))


# cv2.imshow('ori', src_img)
# cv2.imshow('result',new)
cv2.imshow('rotate',rotated_30)
cv2.waitKey(0)

