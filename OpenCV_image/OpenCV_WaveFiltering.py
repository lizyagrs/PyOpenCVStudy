import numpy as np
import cv2,os
import matplotlib.pyplot as plt

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.sans-serif']=['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False# 显示负号
plt.rcParams['figure.dpi'] = 100 #分辨率


def Filtering(imgFile):
    ########     四个不同的滤波器    #########
    img = cv2.imread(imgFile)

    imgSource = np.flip(img, axis=2)
    # 均值滤波
    img_mean = cv2.blur(img, (5,5))

    # 高斯滤波
    img_Guassian = cv2.GaussianBlur(img,(5,5),0)

    # 中值滤波
    img_median = cv2.medianBlur(img, 5)

    # 双边滤波
    img_bilater = cv2.bilateralFilter(img,9,75,75)

    # 展示不同的图片
    titles = ['srcImg','mean', 'Gaussian', 'median', 'bilateral']
    imgs = [imgSource, img_mean, img_Guassian, img_median, img_bilater]

    for i in range(5):
        plt.subplot(2,3,i+1)#注意，这和matlab中类似，没有0，数组下标从1开始
        plt.imshow(imgs[i])
        plt.title(titles[i])
    plt.show()

def KalmanFilting():
    # 模拟数据
    t = np.linspace(1,100,100)
    print(t)
    a = 0.5
    position = (a * t**2)/2

    position_noise = position+np.random.normal(0,120,size=(t.shape[0]))
    plt.plot(t,position,label='truth position')
    plt.plot(t,position_noise,label='only use measured position')


    # 初试的估计导弹的位置就直接用GPS测量的位置
    predicts = [position_noise[0]]
    position_predict = predicts[0]

    predict_var = 0
    odo_var = 120**2 #这是我们自己设定的位置测量仪器的方差，越大则测量值占比越低
    v_std = 50 # 测量仪器的方差
    for i in range(1,t.shape[0]):

        dv =  (position[i]-position[i-1]) + np.random.normal(0,50) # 模拟从IMU读取出的速度
        position_predict = position_predict + dv # 利用上个时刻的位置和速度预测当前位置
        predict_var += v_std**2 # 更新预测数据的方差
        # 下面是Kalman滤波
        position_predict = position_predict*odo_var/(predict_var + odo_var)+position_noise[i]*predict_var/(predict_var + odo_var)
        predict_var = (predict_var * odo_var)/(predict_var + odo_var)**2
        predicts.append(position_predict)


    plt.plot(t,predicts,label='kalman filtered position')

    plt.legend()
    plt.show()


if __name__=='__main__':
    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #print('rootPath:'+rootPath)
    #数据文件路径
    dataPath = os.path.abspath(rootPath + r'\Image')
    #print('dataPath:'+dataPath)
    #切换目录
    os.chdir(dataPath)
    #SHP文件路径
    imgFile ="YellowPeaches.jpg"
    #imgFile ="ShaHu.png"
    Filtering(imgFile)
    #KalmanFilting()