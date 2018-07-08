# The functions that help pre-process(Not fetching) data should be put in here
import numpy as np
import tensorflow as tf
from fetch_hf import get_image_data
import matplotlib.pyplot as plt


def largest_image_size(img_array):
    max_row = float('-inf')
    max_column = float('-inf')
    for i in range(1, len(img_array), 2):
        array = img_array[i]
        if len(array) > max_row:
            max_row = len(array)
        if len(array[0]) > max_column:
            max_column = len(array)
    largest_size = (max_row, max_column)
    return largest_size


def smallest_image_size(img_array):
    min_row = float('inf')
    min_column = float('inf')
    for i in range(1, len(img_array), 2):
        array = img_array[i]
        if len(array) < min_row:
            min_row = len(array)
        if len(array[0]) < min_column:
            min_column = len(array)
    largest_size = (min_row, min_column)
    return largest_size


def resize_img_numpy(img_list, shape):
    result = []
    print("Start resizing images...")
    for img in img_list:
        img = tf.constant(img)
        img = tf.image.resize_images(img, shape)
        result.append(img)
    print("Done.")
    return result


#The following codes test the function above
# label_list,img_list = get_image_data("/Users/frank/Documents/GitHub/alexnet-sbs/dataSet/train/NORMAL")
#
# size = tf.constant([100, 100])
#
# test = resize_img_numpy(img_list[:10], size)[3]
#
# sess = tf.InteractiveSession()
# im = sess.run(test)
# row = im.shape[0]
# column = im.shape[1]
# im = im.flatten().reshape(row, column)
#
#
#  with tf.Session() as sess:
#      print(sess.run(test))
#
# plt.imshow(im[::], cmap="gray")
# plt.show()


