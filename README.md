# background-subtraction
python背景减除法对视频进行处理
cap = cv2.VideoCapture(0)中是0的话代表取电脑的摄像头，
如果换成cap = cv2.VideoCapture(path)则是对path中视频进行处理  
CV中可以调用CNT,GMG,GSOC,LSBP,MOG几种背景减除法，并且可以设置参数
