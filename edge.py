import cv2
'''
Canny algo使用
1. 降躁: 使用高斯平滑模板做卷積
2. 找圖像的亮度梯度: 4個mask檢測水平、垂直以及對角線方向的邊緣。
3. 圖像中跟蹤邊緣:
'''

image = cv2.imread('images.jpg')
# 影像轉成灰階
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 影像去除雜訊-> 高斯模糊
blurred = cv2.GaussianBlur(grey, (3, 7), 0)
# 邊緣偵測，使用兩種門檻值
canny = cv2.Canny(blurred, 30, 150)
cv2.imshow('Input1', image)
# cv2.imshow('Input2', grey)
# cv2.imshow('Input3', blurred)
cv2.imshow('Output', canny)
cv2.waitKey(0)