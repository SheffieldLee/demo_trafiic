import cv2

def filter_mask(img):
    # 创建一个2*2的椭圆核
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    # 闭运算，填补白色区域（前景）中的小洞，或马路上的白色缝隙
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    # 开运算，去除白色噪点
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    # 膨胀，连接同一车辆相邻的前景（白块），使前景更清晰好分辨，迭代2次
    dilation = cv2.dilate(opening, kernel, iterations=2)
    # 阈值化，去除车辆的灰色阴影
    ret, threshold = cv2.threshold(dilation, 240, 255, cv2.THRESH_BINARY)
    return threshold