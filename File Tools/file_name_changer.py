import os
import glob

your_dest_dir = "..\\yinxiebing\\cut_images"

for file in os.listdir(your_dest_dir):
    os.rename(os.path.join(your_dest_dir, file), os.path.join(your_dest_dir, file.replace('ç¨³å®šæœŸå°æ–‘å—', 'wendingqixiaobankuai')))