import os
import cv2
import xml.etree.ElementTree as ET
from utils.filp import *
from utils.blur import *
from utils.brighten import *

if __name__ == "__main__":
    # 设置文件夹路径
    image_folder = 'test/images/'
    xml_folder = 'test/annotations/'

    # 遍历文件夹中的图片和XML文件
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg'):
            image_path = os.path.join(image_folder, filename)
            xml_path = os.path.join(xml_folder, filename.replace('.jpg', '.xml'))

            # 水平翻转
            horizontal_flip(image_path, xml_path)

            # 垂直翻转
            vertical_flip(image_path, xml_path)

            # 亮度增强
            brighten(image_path, xml_path)

            # 亮度减弱
            darken(image_path, xml_path)

            # 模糊
            blur(image_path, xml_path)

            # 高斯模糊
            Gaussion_blur(image_path, xml_path)
            

