import os
import shutil
from my_utils.change import *
from my_utils.blur import *
from my_utils.brighten import *
from my_utils.sharpen import *
from my_utils.cutout import *
from my_utils.flip import *


def copyto(input_img_path, input_label_path, save_img_dir, save_label_dir, save_kind, name):
    save_img_path = os.path.join(save_img_dir, save_kind, name + '.jpg')
    save_label_path = os.path.join(save_label_dir, save_kind, name + '.txt')
    shutil.copy(input_img_path, save_img_path)
    shutil.copy(input_label_path, save_label_path)


if __name__ == '__main__':

    raw_img_dir = './raw_images/images'
    save_img_dir = './raw_images/changed_imgs'
    raw_label_dir = './raw_images/labels'
    save_label_dir = './raw_images/changed_labels'

    if os.path.exists(save_img_dir) == 0:
        os.mkdir(save_img_dir)
    if os.path.exists(save_label_dir):
        os.mkdir(save_label_dir)

    change(raw_img_dir, save_img_dir, raw_label_dir, save_label_dir)

    img_list = os.listdir(save_img_dir)
    for index, img_name_with_extension in enumerate(img_list, 1):
        name = os.path.splitext(img_name_with_extension)[0]

        input_img_dir = './raw_images/changed_imgs'
        input_label_dir = './raw_images/changed_labels'
        save_img_dir = './aug_images/images'
        save_label_dir = 'aug_images/labels'

        if os.path.exists(save_img_dir) == 0:
            os.mkdir(save_img_dir)
        if os.path.exists(save_label_dir):
            os.mkdir(save_label_dir)

        blur(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        gussian_blur(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        sharpen(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        brighten(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        cutout(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip1(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip2(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip3(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip4(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
        flip5(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)

    # 将所得数据分类
    input_img_dir = save_img_dir
    input_label_dir = save_label_dir

    final_img_dir = './datasets/images'
    final_label_dir = './datasets/labels'

    if os.path.exists(final_img_dir) == 0:
        os.mkdir(final_img_dir)
    if os.path.exists(final_label_dir):
        os.mkdir(final_label_dir)

    img_list = os.listdir(save_img_dir)
    img_num = len(img_list)
    for index, name_with_extention in enumerate(img_list, 1):
        rate = (index*1.0)/img_num
        name = os.path.splitext(name_with_extention)[0]
        input_img_path = os.path.join(input_img_dir, name_with_extention)
        input_label_path = os.path.join(input_label_dir, name+'.txt')
        if rate <= 0.7:
            copyto(input_img_path, input_label_path, final_img_dir, final_label_dir, save_kind='train', name=name)
        elif rate <= 0.9:
            copyto(input_img_path, input_label_path, final_img_dir, final_label_dir, save_kind='test', name=name)
        else:
            copyto(input_img_path, input_label_path, final_img_dir, final_label_dir, save_kind='val', name=name)
        shutil.copy(os.path.join('raw_images', 'changed_labels', 'classes.txt'), os.path.join('datasets/labels/train', 'classes.txt'))
        shutil.copy(os.path.join('raw_images', 'changed_labels', 'classes.txt'), os.path.join('datasets/labels/test', 'classes.txt'))
        shutil.copy(os.path.join('raw_images', 'changed_labels', 'classes.txt'), os.path.join('datasets/labels/train', 'classes.txt'))











