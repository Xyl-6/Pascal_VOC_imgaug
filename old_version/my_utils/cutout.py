import os
import cv2
import shutil
import numpy as np
from PIL import Image

'''
Randomly pick out four positions
Fill with black/color rectangles
'''

# def cutout(image, image_name, save_dir):
def cutout(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name):
    input_img_path = os.path.join(input_img_dir, name + '.jpg')
    input_label_path = os.path.join(input_label_dir, name + '.txt')
    image = cv2.imread(input_img_path)
    min_size_ratio, max_size_ratio = 0.1, 0.3
    channel_wise = False
    max_crop = 4
    replacement = 0

    size = np.array(image.shape[:2])
    mini, maxi = min_size_ratio * size, max_size_ratio * size
    cutout_image = image
    for _ in range(max_crop):
        # random size
        h = np.random.randint(mini[0], maxi[0])
        w = np.random.randint(mini[1], maxi[1])
        # random place
        shift_h = np.random.randint(0, size[0] - h)
        shift_w = np.random.randint(0, size[1] - w)

        if channel_wise:
            c = np.random.randint(0, image.shape[-1])
            cutout_image[shift_h:shift_h+h, shift_w:shift_w+w, c] = replacement
        else:
            cutout_image[shift_h:shift_h+h, shift_w:shift_w+w] = replacement

    save_img_path = os.path.join(save_img_dir, name + '_cutout.jpg')
    cv2.imwrite(save_img_path, image)
    save_label_path = os.path.join(save_label_dir, name + "_cutout.txt")
    shutil.copyfile(input_label_path, save_label_path)

# input_img_dir = '../raw_images/changed_imgs'
# input_label_dir = '../raw_images/changed_labels'
# save_img_dir = '../aug_images/images'
# save_label_dir = '../aug_images/labels'
# name = '1'
# cutout(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
