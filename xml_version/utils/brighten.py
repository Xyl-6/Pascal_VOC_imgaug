import os
import cv2
import xml.etree.ElementTree as ET

def brighten(image_path, xml_path):
    image = cv2.imread(image_path)
    brighten_image = cv2.addWeighted(image, 1.1, image, 0, 0)
    cv2.imwrite(image_path.replace('.jpg', '_brighten.jpg'), brighten_image)

    tree = ET.parse(xml_path)
    tree.write(xml_path.replace('.xml', '_brighten.xml'))

def darken(image_path, xml_path):
    image = cv2.imread(image_path)
    darken_image = cv2.addWeighted(image, 0.9, image, 0, 0)
    cv2.imwrite(image_path.replace('.jpg', '_darken.jpg'), darken_image)

    tree = ET.parse(xml_path)
    tree.write(xml_path.replace('.xml', '_darken.xml'))

