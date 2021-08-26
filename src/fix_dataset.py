# #setup data
# import os
# import glob2
# import numpy as np
# data_folder = './dataset'
# root_folder = '.'
# os.chdir(data_folder)
# files = []
# for ext in ["*.png", "*.jpeg", "*.jpg"]:
#   image_files = glob2.glob(ext)
#   files += image_files
# for idx in np.arange(len(files)):
#   text_file = files[idx][:-3] + "txt"
#   text = ''
#   with open(text_file, "r") as f:
#     text = f.readline()
#   text = text.replace("lane","lanes")
#   with open(text_file, "w") as f:
#     f.write(text)