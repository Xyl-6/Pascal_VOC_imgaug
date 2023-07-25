import os
import shutil
from PIL import Image, ImageEnhance


def brighten(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name):
    input_img_path = os.path.join(input_img_dir, name + '.jpg')
    input_label_path = os.path.join(input_label_dir, name + '.txt')
    image = Image.open(input_img_path)
    brighten_enhancer = ImageEnhance.Brightness(image)
    output_img = brighten_enhancer.enhance(1.2)
    save_img_path = os.path.join(save_img_dir, name + "_brighten.jpg")
    save_label_path = os.path.join(save_label_dir, name + "_brighten.txt")
    output_img.save(save_img_path)
    shutil.copy(input_label_path, save_label_path)

# input_img_dir = '../raw_images/changed_imgs'
# input_label_dir = '../raw_images/changed_labels'
# save_img_dir = '../aug_images/images'
# save_label_dir = '../aug_images/labels'
# name = '1'
# brighten(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
