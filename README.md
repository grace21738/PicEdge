# PicEdge
### 實作方式
1. 將圖片轉成灰階
2. 降躁: 使用高斯平滑模板做卷積
3. 找圖像的亮度梯度: 4個mask檢測水平、垂直以及對角線方向的邊緣。
4. 圖像中利用兩種參數門檻跟蹤邊緣
### 實作圖
![images](https://user-images.githubusercontent.com/61674033/136801844-86c2794e-2174-4f28-9f72-89b207305021.jpg)
![img_edge](https://user-images.githubusercontent.com/61674033/136801846-fd99ea53-d8b6-4f34-ac25-3f625abce9e1.jpg)
