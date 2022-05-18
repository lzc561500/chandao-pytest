#encoding=utf-8
from PIL import ImageGrab
import cv2
import numpy as np
class VideoRecord:

    def video_record(self):
        fps = 10
        #截取当前屏幕
        screen = ImageGrab.grab()
        width,height = screen.size
        #编码格式 MEPG-4 后缀名.avi
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        #创建video
        video = cv2.VideoWriter("test.avi",fourcc,fps,(width,height))
        flag = True
        print("开始录屏")
        while flag:
            #截图
            capture = ImageGrab.grab()
            #图片转换成彩色
            image= cv2.cvtColor(np.array(capture),cv2.COLOR_RGB2BGR)
            #将image写入video中
            video.write(image)
            #展示窗口
            cv2.imshow("test",np.zeros((400,400),np.uint8))
            if cv2.waitKey(1) == 27:
                print("录屏结束！")
                flag=False
        #关闭录屏流
        video.release()
        #关闭所有窗口
        cv2.destroyAllWindows()

    #解决窗口中文乱码
    # def zh_ch(self,title):
    #     return title.encode("gbk").decode(errors='ignore')

if __name__ == '__main__':
    v = VideoRecord()
    v.video_record()





