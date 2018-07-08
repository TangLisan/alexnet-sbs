import os
import numpy as np
import cv2
# All the function that will be used to fetch unprocessed data should be put here


# Given the address of a folder, parsing all the .jpeg file within the folder.
# Return: an numpy array consisting 1. the label of the image
#                                   2. the numpy array version of the image
def get_image_data(folder_address):
    result_list = []
    directory = os.fsencode(folder_address)
    for file in os.listdir(directory):  # Iterate through the folder
        filename = os.fsdecode(file)  # File name in string
        print("Parsing: " + filename + "...")
        if filename.endswith(".jpeg"):
            img_path = folder_address + "/" + filename
            img_array = cv2.imread(img_path, 0)  # Converting image into numpy array
            if filename.find("bacteria") != -1:
                result_list.append("bacteria")
                result_list.append(img_array)
            elif filename.find("virus") != -1:
                result_list.append("virus")
                result_list.append(img_array)
            else:
                result_list.append("normal")
                result_list.append(img_array)
        print("Done.")
    result_list = np.array(result_list, dtype=object)
    return result_list
