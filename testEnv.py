import cv2

print("-------------Hello OpenCV!-------------")

# windows 下文件路径字符串可用表示方法 r" "
# src = cv2.imread(r"E:\Chang\dataset\DIP\OpenCV\lena.png")
src = cv2.imread("E:/Chang/dataset/DIP/OpenCV/lena.png")

# 创建窗口，显示图像
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input image", src)

# 保持窗口
cv2.waitKey(0)

# 销毁窗口
cv2.destroyAllWindows()
