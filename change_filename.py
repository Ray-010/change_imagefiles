""" 使い方
先にresize_images.py を実行してください.
処理結果がimages_outputに入ります.
images_output内のリサイズされた画像に対して処理をしていきます.
"""

import os
import glob

path_jpg = './images_output/*.jpg'
flist = glob.glob(path_jpg)

# 画像名前の変更
file_name = 'a_pedestrian_light_image'
for i, file in enumerate(flist):
    print(file)
    os.rename(file, './images_output/' + file_name + str(i) + '.jpg')
