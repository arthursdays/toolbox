import os
import glob

for file in os.listdir("..\\yinxiebing\\img_data"):
    os.rename(os.path.join("..\\yinxiebing\\img_data", file), os.path.join("..\\yinxiebing\\img_data", file.replace(',', '_')))