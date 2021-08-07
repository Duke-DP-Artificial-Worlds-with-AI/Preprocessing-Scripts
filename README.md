# Preprocessing-Scripts

crop_background_images.py- Given a directory, it walks the directory and crops the background images to 608x608 (to match source image size, maintain consistency with previous image sizes in YOLOv3 experiments)

extract_masks.py- Given a directory, it walks the directory and separates the multichannel masks into its separate components (separate for each energy infrastructure)

normalize_image_channels.py- Given a directory, it walks the directory and converts images of 4 channels to 3 channels (required for GP GAN image blending downstream)

regenerate_masks.py- Given a directory, it walks the directory and converts binary masks of 1 channel to 3 channels using numpy stack to maintain its grayscale nature (required for effective GP GAN image blending downstream) 
