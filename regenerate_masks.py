import os
from PIL import Image
import numpy as np
import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('--input_directory', type=str, default='', help='path to the windmill image')
#parser.add_argument('--output_directory', type=str, default='results', help='name of output file')
#opt = parser.parse_args()

#directory = opt.input_directory
#out_directory = opt.output_directory

#complete_out = os.path.join("/hdd/dataplus2021/fcw/", out_directory)
#print(complete_out)

#if not os.path.exists(out_directory):
#  os.mkdir(out_directory)
#  print(out_directory + " directory was made")


directory = "/hdd/dataplus2021/fcw/transmission_masks"

for root, subdirectories, files in os.walk(directory):
    #for subdirectory in subdirectories:
    #    curr_subdir = os.path.join(root, subdirectory)
    #    curr_subdir = curr_subdir.replace("share","fcw")
    #    curr_subdir = curr_subdir.replace("data/masks", "windmill_masks/masks")
    #    print(curr_subdir)
    #    if not os.path.exists(curr_subdir):
    #        os.mkdir(curr_subdir)
    #        print(curr_subdir + " directory was made")
    for file in files:
        #Need to check if masks
        if file.endswith('.png') or file.endswith('.tif'):
          img_path = os.path.join(root, file)
          print(img_path)
          original = Image.open(img_path)
          if(len(original.split()) == 1):
            img_arr = np.array(original)
            new_img_arr = np.stack((img_arr, img_arr, img_arr), axis=2)
            out_img = Image.fromarray(new_img_arr)
            #new_img_path = img_path.replace("share","fcw")
            #new_img_path = new_img_path.replace("other_datasets/power_plant_satellite_imagery_dataset/annotations/binary", out_directory)
            #print(new_img_path)
            #out_img.save(new_img_path)
            print(img_path)
            out_img.save(img_path)
