import os 
#from skimage.transform import resize
from PIL import Image
import matplotlib.image as mpimg
import numpy as np

#directory = "/hdd/dataplus2021/share/background_images"
directory = "/hdd/dataplus2021/share/domain_experiment/BC_team_domain_experiment/background_by_domain"
#my_dir = "./"

for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        curr_subdir = os.path.join(root, subdirectory)
        curr_subdir = curr_subdir.replace("share","fcw")
        #curr_subdir = curr_subdir.replace("background_images", "background_images_cropped")
        curr_subdir = curr_subdir.replace("/domain_experiment/BC_team_domain_experiment", "")
        if not os.path.exists(curr_subdir):
            os.mkdir(curr_subdir)
        print(curr_subdir + " directory was made")
    for file in files:
        if file.endswith('.jpg'):
            img_path = os.path.join(root, file)
            img = Image.open(img_path)
            #img = mpimg.imread(img_path)
            #if(len(img.shape) > 2 and img.shape[2] == 4):
            # print(img_path)
            #  img = img[:, :, :-1]
            #img_2 = Image.fromarray((img*255).astype(np.uint8))
            cropped_img = img.resize((608,608))
            cropped_img_path = img_path.replace("share","fcw")
            #cropped_img_path = cropped_img_path.replace("background_images","background_images_cropped")
            cropped_img_path = cropped_img_path.replace("/domain_experiment/BC_team_domain_experiment", "")
            print(cropped_img_path)
            cropped_img.save(cropped_img_path)

#image = 
#image_resized = resize(image, (604,604), anti_aliasing = True)
