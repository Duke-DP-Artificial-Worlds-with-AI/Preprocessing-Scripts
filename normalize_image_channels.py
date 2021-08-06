import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

#directory = "/hdd/dataplus2021/fcw/background_images_cropped"
directory = "/hdd/dataplus2021/fcw/plants_cropped"

for root, subdirectories, files in os.walk(directory):
    for file in files:
        if file.endswith('.png') or file.endswith('.tif'):
          img_path = os.path.join(root, file)
          img = mpimg.imread(img_path)
          if(img.shape[2] == 4):
            # print(img_path)
              img_out = img[:, :, :-1]
              img_2 = Image.fromarray((img_out*255).astype(np.uint8))
              img_2.save(img_path)
        #cropped_img.save(cropped_img_path)
