# 删除空文件，一对图片和label
import os

txt_path = "/Users/beauty/Documents/GitHub/pedestrianDetection/data/kitti/training/label_2"
png_path = "/Users/beauty/Documents/GitHub/pedestrianDetection/data/kitti/training/image_2"
files = os.listdir(txt_path)
png_files = os.listdir(png_path)
i=1
os.chdir(txt_path)
for filename in files:
    # 将文件名和缀名分成俩部分
    if os.path.isfile(filename):
        if filename.endswith('txt'):
            size = os.path.getsize(filename)
            if size == 0:
                portion = os.path.splitext(filename)
                os.remove(txt_path + '/' + filename)
                os.remove(png_path + '/' + str(portion[0]) + '.png')
                i = i+1