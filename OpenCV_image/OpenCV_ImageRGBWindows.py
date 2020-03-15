import cv2,os

#获取工程根目录的路径
rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#print('rootPath:'+rootPath)
#数据文件路径
dataPath = os.path.abspath(rootPath + r'\Image')
#print('dataPath:'+dataPath)
#切换目录
os.chdir(dataPath)
#SHP文件路径
imgFile ="CrayfishRice.jpg"
# 读取图片并缩放方便显示
img = cv2.imread(imgFile)
height, width = img.shape[:2]
size = (int(width * 0.2), int(height * 0.2))
# 缩放
img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

# BGR转化为HSV
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 鼠标点击响应事件
def getposHsv(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("HSV is", HSV[y, x])


def getposBgr(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Bgr is", img[y, x])


cv2.imshow("imageHSV", HSV)
cv2.imshow('image', img)
cv2.setMouseCallback("imageHSV", getposHsv)
cv2.setMouseCallback("image", getposBgr)
cv2.waitKey(0)