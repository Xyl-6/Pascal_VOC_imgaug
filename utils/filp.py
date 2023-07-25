import os
import cv2
import xml.etree.ElementTree as ET

def horizontal_flip(image_path, xml_path):
    image = cv2.imread(image_path)
    flipped_image = cv2.flip(image, 1)  # 1表示水平翻转
    cv2.imwrite(image_path.replace('.jpg', '_flipped1.jpg'), flipped_image)

    tree = ET.parse(xml_path)
    root = tree.getroot()
    width = int(root.find('size').find('width').text)
    for obj in root.findall('object'):
        xmin = int(obj.find('bndbox').find('xmin').text)
        xmax = int(obj.find('bndbox').find('xmax').text)
        obj.find('bndbox').find('xmin').text = str(width - xmax)
        obj.find('bndbox').find('xmax').text = str(width - xmin)
    tree.write(xml_path.replace('.xml', '_flipped.xml'))

def vertical_flip(image_path, xml_path):
    image = cv2.imread(image_path)
    flipped_image = cv2.flip(image, 0)  # 0表示垂直翻转
    cv2.imwrite(image_path.replace('.jpg', '_flipped0.jpg'), flipped_image)

    tree = ET.parse(xml_path)
    root = tree.getroot()
    height = int(root.find('size').find('height').text)
    for obj in root.findall('object'):
        ymin = int(obj.find('bndbox').find('ymin').text)
        ymax = int(obj.find('bndbox').find('ymax').text)
        obj.find('bndbox').find('ymin').text = str(height - ymax)
        obj.find('bndbox').find('ymax').text = str(height - ymin)
    tree.write(xml_path.replace('.xml', '_flipped.xml'))
