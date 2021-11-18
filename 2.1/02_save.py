import cv2

f_dir = '../ex_img/04.jpg'
src_img = cv2.imread(f_dir)
if(src_img.all() !=None):
    src_img2 = cv2.cvtColor(src_img,cv2.COLOR_RGB2GRAY)
    cv2.imwrite("../ex_img/gray04.jpg",src_img2)

# cv2.imshow("src_img",src_img)
# cv2.imshow("src_img2",src_img2)
# cv2.waitKey(0)
