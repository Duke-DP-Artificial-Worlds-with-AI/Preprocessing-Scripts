from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import os

object_types = [
    'distribution_tower',
    'distribution_line',
    'transmission_tower',
    'transmission_line',
    'other_tower',
    'other_line',
    'sub_station'
]

directory = "/hdd/dataplus2021/share/other_datasets/transmission_dataset/"

for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        curr_subdir = os.path.join(root, subdirectory)
        curr_subdir = curr_subdir.replace("share","fcw")
        curr_subdir = curr_subdir.replace("other_datasets/transmission_dataset/", "transmission_masks/")
        for x in object_types:
            obj_subdir = curr_subdir.replace("transmission_masks/", "transmission_masks/" + x + "/")
            if not os.path.exists(obj_subdir):
                os.makedirs(obj_subdir)
                print(obj_subdir + " directory was made")
    for file in files:
        if file.endswith('multiclass.tif'):
            img_path = os.path.join(root, file)
            new_img_path = img_path.replace("share", "fcw")
            new_img_path = new_img_path.replace("other_datasets/transmission_dataset/", "transmission_masks/")
            multiclass_lbl_tif = io.imread(img_path).T
            for object_type, mask_val in zip(object_types, np.unique(multiclass_lbl_tif)):
                mask_multiclass_tif = multiclass_lbl_tif == mask_val
                obj_img_path = new_img_path.replace("transmission_masks/","transmission_masks/" + object_type + "/")
                print(obj_img_path)
                io.imsave(obj_img_path, mask_multiclass_tif)

