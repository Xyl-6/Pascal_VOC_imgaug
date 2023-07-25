import os
import cv2
import shutil
from PIL import Image
from torchvision import transforms


def change(raw_img_dir, save_img_dir, raw_label_dir, save_label_dir):
    raw_img_list = os.listdir(raw_img_dir)
    RESIZED_HEIGHT = 640
    RESIZED_WIDTH = 640
    for index, name_with_extention in enumerate(raw_img_list, 1):
        name = os.path.splitext(name_with_extention)[0]
        image = Image.open(os.path.join(raw_img_dir, name_with_extention))
        resize = transforms.Resize([RESIZED_WIDTH, RESIZED_HEIGHT])
        resized_img = resize(image)
        img_save_name = f"{index}.jpg"
        label_save_name = f"{index}.txt"
        resized_img.save(os.path.join(save_img_dir, img_save_name))
        shutil.copy(os.path.join(raw_label_dir, name+'.txt'), os.path.join(save_label_dir, label_save_name))
    shutil.copy(os.path.join(raw_label_dir, 'classes.txt'), os.path.join(save_label_dir, 'classes.txt'))
    return None

# raw_img_dir = '../raw_images/images'
# save_img_dir = '../raw_images/changed_imgs'
# raw_label_dir = '../raw_images/labels'
# save_label_dir = '../raw_images/changed_labels'
# change(raw_img_dir, save_img_dir, raw_label_dir, save_label_dir)





