#this file is used to change the wrong label in pascal file into the right one

import os

file_path = '/home/arthur/Desktop/skin-10-balanced-3/Atopic_Dermatitis_Eczema'
old_string = 'Apotic_dermatitis_Eczemaw'
new_string = 'Apotic_dermatitis_Eczema'

for filename in os.listdir(file_path):
    file = open(os.path.join(file_path, filename))
    content = file.read()
    if old_string not in content:
        print('"{}" not found in {}.'.format(old_string, filename))
        file.close()
        continue

    else:
        file.close()

        with open(os.path.join(file_path, filename), 'w') as f:
            print('Changing "{}" to "{}" in {}.'.format(old_string, new_string, filename))
            content = content.replace(old_string, new_string)
            f.write(content)