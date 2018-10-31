import os
from shutil import copyfile
import random

classes=["Basal_Cell_Carcinoma",
         "Acne_Vulgaris",
         "Seborrheic_Keratosis",
         "Rosacea",
         "Actinic_solar_Damage__Actinic_Keratosis",
         "Atopic_Dermatitis_Eczema",
         "Compound_Nevus",
         "Stasis_Ulcer",
         "Onychomycosis",
         "Tinea_Corporis"]

subfolders = ['train', 'val']

ratio = 0.25

base_dir = '/home/arthur/Documents/derm101'
output_dir = '/home/arthur/Desktop/skin-10-balanced'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)


for name in classes:

    namedir = os.path.join(output_dir, name)

    if not os.path.exists(namedir):

        os.makedirs(os.path.join(output_dir, name))

    for folder in subfolders:

        subfolderdir = os.path.join(namedir, folder)

        if not os.path.exists(subfolderdir):
            os.makedirs(subfolderdir)

    all_imgs = os.listdir("{}/selected".format(os.path.join(base_dir, name)))
    train_num = (int)(len(all_imgs)*0.75)
    train_images = set()
    val_images = []

    while len(train_images) < train_num:
        train_images.add(all_imgs[random.randint(0, len(all_imgs)-1)])

    for img in all_imgs:
        if img not in train_images:
            val_images.append(img)

    print(len(train_images)+len(val_images))

    for file in train_images:
        copyfile("{}/{}/selected/{}".format(base_dir, name, file), "{}/{}/train/{}".format(output_dir, name, file))

    for file in val_images:
        copyfile("{}/{}/selected/{}".format(base_dir, name, file), "{}/{}/val/{}".format(output_dir, name, file))
