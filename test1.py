import cv2
'''
读取图像
cv2.imread(imgpath,flag)
    imgpath表示图像的路径。
    flag表示读取图象的方式
        1. cv.IMREAD_COLOR: 读取彩色图片，忽略alpha通道（也就是透明度）
        0. cv.IMREAD_GRAYSCALE: 以灰度模式读取图片 
        -1. cv.IMREAD_UNCHANGED: 读取完整的图片，包括alpha通道
'''
img = cv2.imread("C:\\Users\\Shinelon\\Desktop\\work\code\\CV\\16.jpg",0)

'''
创建一个空窗口
cv2.namedWindow(name,flags)
    name表示要创建的窗口的名字
    flags表示窗口是否可以调整大小(ps:默认是cv.WINDOW_AUTOSIZE不能调整大小，当图片太大会出现显示不全的问题。)
        1 cv.WINDOW_AUTOSIZE: 不能调整大小
        2 cv.WINDOW_NORMAL: 可以调整大小
'''
cv2.namedWindow("img",cv2.WINDOW_NORMAL)

'''
显示在指定窗口中显示图像
cv2.imshow(name,img)
    name窗口名字
    img表示读取的图片数据
'''
cv2.imshow("img",img)

'''
等待用户按下一次按键
cv.waitKey(time)
time(单位ms)
    当time <= 0时表示无限期等待，直到用户产生一次按键事件
    当time >0 表示等待time毫秒之后程序继续运行
返回值为在等待期间按下按键的ASCII码的整数数值
'''
k = cv2.waitKey(0)
if(k == ord('s')):# ord(__c)将字符__c转化成它对应的整型数值
    '''
    保存图片
    cv.imwrite(name,img)
    name 表示要创建的图片名
    img 表示图片数据
    '''
    cv2.imwrite("gary.png",img)

'''
销毁所有窗口
cv.destroyAllWindows()

也可以使用销毁指定窗口
cv2.destroyWindow(name)
name表示窗口的名字
'''
cv2.destroyAllWindows()
