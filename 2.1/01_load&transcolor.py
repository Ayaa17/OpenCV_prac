import cv2
import numpy as np
import matplotlib.pyplot as plt
import setting

src_img_dir = '../ex_img/03.jpg'
src_img = cv2.imread(src_img_dir)
if(src_img is None):
    print("Load img fail...")
else:
    print("Load img success")
# cv2.imshow("img",src_img)
# src_img.shape
plt.axis('off')
#色彩通道 BGR
for i in range(3):
    title_ch = f'img_ch{i}'
    src_img1 = np.zeros(shape=(1328,1080,3))
    src_img1[:,:,i] =src_img[:,:,i]
    # cv2.imshow(title_ch , src_img1/255)

    plt.subplot(3,3,i+1)
    plt.axis('off')
    plt.imshow(src_img1/255)

title = "img_"
# 轉灰階
img=cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)
# cv2.imshow(title+"COLOR_BGR2GRAY",img)
plt.subplot(3,3,4).imshow(img)
plt.axis('off')
# 轉HSV色彩空間
img=cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)
# cv2.imshow(title+"COLOR_BGR2HSV",img)
plt.subplot(3,3,5).imshow(img)
plt.axis('off')
# 轉HSV色彩空間
img=cv2.cvtColor(src_img,cv2.COLOR_BGR2HLS)
# cv2.imshow(title+"COLOR_BGR2HLS",img)
plt.subplot(3,3,6).imshow(img)
plt.axis('off')
# 轉LAB色彩空間
img=cv2.cvtColor(src_img,cv2.COLOR_BGR2LAB)
# cv2.imshow(title+"COLOR_BGR2LAB",img)
plt.subplot(3,3,7).imshow(img)
plt.axis('off')
# 轉LUV色彩空間
img=cv2.cvtColor(src_img,cv2.COLOR_BGR2LUV)
# cv2.imshow(title+"COLOR_BGR2LUV",img)
plt.subplot(3,3,8).imshow(img)
plt.axis('off')
# 轉HSV色彩空間
img=cv2.cvtColor(src_img,cv2.COLOR_RGB2BGRA)
# cv2.imshow(title+"COLOR_BGR2LAB",img)
plt.subplot(3,3,9).imshow(img)
plt.axis('off')


cv2.waitKey(0)
plt.show()

