import cv2


# src_img_dir2 = './ex_img/02.jpg'
src_img_dir2 = '../ex_img/02.jpg'
src_img2 = cv2.imread(src_img_dir2)
src_img2 = src_img2[:,:,0]
# 旋轉、縮放參數
center = (int(src_img2.shape[0]/2),int(src_img2.shape[1]/2))
angle:float = 60
scale:float = 0.5
# 計算旋踵的仿射變換矩陣
rotateImg=cv2.getRotationMatrix2D(center,angle,scale)
# 仿射轉換
result=cv2.warpAffine(src_img2,rotateImg,src_img2.shape)



cv2.imshow("img2",src_img2)
cv2.imshow("rotateImg",result)


cv2.waitKey(0)