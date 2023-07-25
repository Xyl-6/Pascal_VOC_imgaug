from PIL import Image
import os


def flip1(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name):
    input_img_path = os.path.join(input_img_dir, name + '.jpg')
    input_label_path = os.path.join(input_label_dir, name + '.txt')
    image = Image.open(input_img_path)
    output_img = image.transpose(Image.FLIP_LEFT_RIGHT)

    save_img_path = os.path.join(save_img_dir, name + "_flip1.jpg")
    save_label_path = os.path.join(save_label_dir, name + "_flip1.txt")

    output_img.save(save_img_path)

    with open(input_label_path) as before_contest:
        with open(save_label_path, 'w') as after_contest:
            for line in before_contest.readlines():
                word = line.split()
                after_contest.write(
                    word[0] + ' ' + str(1-float(word[1])) + ' ' + word[2] + ' ' +
                    word[3] + ' ' + word[4]
                )


def flip2(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name):
    input_img_path = os.path.join(input_img_dir, name + '.jpg')
    input_label_path = os.path.join(input_label_dir, name + '.txt')
    image = Image.open(input_img_path)
    output_img = image.transpose(Image.FLIP_TOP_BOTTOM)

    save_img_path = os.path.join(save_img_dir, name + "_flip2.jpg")
    save_label_path = os.path.join(save_label_dir, name + "_flip2.txt")

    output_img.save(save_img_path)

    with open(input_label_path) as before_contest:
        with open(save_label_path, 'w') as after_contest:
            for line in before_contest.readlines():
                word = line.split()
                after_contest.write(
                    word[0] + ' ' + word[1] + ' ' + str(1-float(word[2])) + ' ' +
                    word[3] + ' ' + word[4]
                )


def flip3(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name):
    input_img_path = os.path.join(input_img_dir, name + '.jpg')
    input_label_path = os.path.join(input_label_dir, name + '.txt')
    image = Image.open(input_img_path)
    output_img = image.rotate(90)

    save_img_path = os.path.join(save_img_dir, name + "_flip3.jpg")
    save_label_path = os.path.join(save_label_dir, name + "_flip3.txt")

    output_img.save(save_img_path)

    with open(input_label_path) as before_contest:
        with open(save_label_path, 'w') as after_contest:
            for line in before_contest.readlines():
                word = line.split()
                after_contest.write(
                    word[0] + ' ' + str(1-float(word[2])) + ' ' + word[1] + ' ' +
                    word[4] + ' ' + word[3]
                )


def flip4(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name):
    input_img_path = os.path.join(input_img_dir, name + '.jpg')
    input_label_path = os.path.join(input_label_dir, name + '.txt')
    image = Image.open(input_img_path)
    output_img = image.rotate(180)

    save_img_path = os.path.join(save_img_dir, name + "_flip4.jpg")
    save_label_path = os.path.join(save_label_dir, name + "_flip4.txt")

    output_img.save(save_img_path)

    with open(input_label_path) as before_contest:
        with open(save_label_path, 'w') as after_contest:
            for line in before_contest.readlines():
                word = line.split()
                after_contest.write(
                    word[0] + ' ' + str(1-float(word[1])) + ' ' + str(1-float(word[2])) + ' ' +
                    word[3] + ' ' + word[4]
                )


def flip5(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name):
    input_img_path = os.path.join(input_img_dir, name + '.jpg')
    input_label_path = os.path.join(input_label_dir, name + '.txt')
    image = Image.open(input_img_path)
    output_img = image.rotate(270)

    save_img_path = os.path.join(save_img_dir, name + "_flip5.jpg")
    save_label_path = os.path.join(save_label_dir, name + "_flip5.txt")

    output_img.save(save_img_path)

    with open(input_label_path, 'r') as before_contest:
        with open(save_label_path, 'w') as after_contest:
            for line in before_contest.readlines():
                word = line.split()
                after_contest.write(
                    word[0] + ' ' + word[2] + ' ' + str(1-float(word[1])) + ' ' +
                    word[4] + ' ' + word[3]
                )


# input_img_dir = '../raw_images/changed_imgs'
# input_label_dir = '../raw_images/changed_labels'
# save_img_dir = '../aug_images/images'
# save_label_dir = '../aug_images/labels'
# name = '1'
# flip1(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)
# flip2(input_img_dir, save_img_dir, input_label_dir, save_label_dir, name)



