"""
* @File: face_detection.py
* @Author: CSY - 25809 
* @Date: 2020/3/29 - 19:50
* @Project: demo
"""
import cv2


class FaceDetectionTest(object):
    """
    人脸检测
    """

    def __init__(self):
        """
        导入分类器
        """
        self.face_patterns = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

    def run(self):
        """
        运行程序
        :return:
        """
        # 读取图片
        sample_image = cv2.imread(r'face.jpg')

        # 检测人脸
        faces = self.face_patterns.detectMultiScale(sample_image, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        # 画出人脸
        for (x, y, w, h) in faces:
            cv2.rectangle(sample_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # # 窗口中文解决方案1：容易丢失中文
        # def zh_ch(string):
        #     return string.encode("gbk").decode(errors="ignore")
        #
        #
        # cv2.imshow(zh_ch('图片'), sample_image)
        #
        # # 窗口中文解决方案2：依旧乱码
        # cv2.imshow(u'图片', sample_image)

        # 显示图片
        cv2.imshow('Face Detection', sample_image)

        # 等待关闭
        cv2.waitKey(0)

        # 保存文件
        cv2.imwrite(r'face detection.png', sample_image)


if __name__ == "__main__":
    fd = FaceDetectionTest()
    fd.run()
