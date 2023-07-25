import os
import cv2
import xml.etree.ElementTree as ET

def blur(image_path, xml_path):
    image = cv2.imread(image_path)
    blur_image = cv2.blur(image, (5, 5))
    cv2.imwrite(image_path.replace('.jpg', '_blur.jpg'), blur_image)

    tree = ET.parse(xml_path)
    tree.write(xml_path.replace('.xml', '_blur.xml'))


def Gaussion_blur(image_path, xml_path):
    image = cv2.imread(image_path)
    Gaussion_blur_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite(image_path.replace('.jpg', '_Gaussion_blur.jpg'), Gaussion_blur_image)

    tree = ET.parse(xml_path)
    tree.write(xml_path.replace('.xml', '_Gaussion_blur.xml'))