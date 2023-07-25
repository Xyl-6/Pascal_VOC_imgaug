import os
import cv2
import shutil


def blur(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name):
    input_img_path = os.path.join(input_img_dir, name+'.jpg')
    input_label_path = os.path.join(input_label_dir, name+'.txt')
    image = cv2.imread(input_img_path)
    output_img = cv2.blur(image, (5, 5))
    save_img_path = os.path.join(save_img_dir, name + f"_blur1.jpg")
    save_label_path = os.path.join(save_label_dir, name + f"_blur1.txt")
    cv2.imwrite(save_img_path, output_img)
    shutil.copy(input_label_path, save_label_path)
    # cv2.imshow(output_img)
    # cv2.waitKey(0)


def gussian_blur(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name):
    input_img_path = os.path.join(input_img_dir, name + '.jpg')
    input_label_path = os.path.join(input_label_dir, name + '.txt')
    image = cv2.imread(input_img_path)
    output_img = cv2.GaussianBlur(image, (5, 5), 2)
    save_img_path = os.path.join(save_img_dir, name + f"_blur2.jpg")
    save_label_path = os.path.join(save_label_dir, name + f"_blur2.txt")
    cv2.imwrite(save_img_path, output_img)
    shutil.copy(input_label_path, save_label_path)
#
# input_img_dir = '../raw_images/changed_imgs'
# input_label_dir = '../raw_images/changed_labels'
# save_img_dir = '../aug_images/images'
# save_label_dir = '../aug_images/labels'
# name = '1'
# blur(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
# gussian_blur(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)








