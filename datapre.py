#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import glob, os

# 数据集的位置/home/robocup/Downloads/darknettest/darknet2/data/sipailou1018merge
imgs_dir = 'data/RoboCup2020'
print(imgs_dir)

#用作 test 的图片数据的比例
percentage_test = 10

#创建训练数据集和测试数据集：train.txt 和 test.txt
file_train = open('data/RoboCup2020/train.txt', 'w')
file_test = open('data/RoboCup2020/test.txt', 'w')

counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(imgs_dir, "*.png")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(imgs_dir + "/" + title + '.png' + "\n")
    else:
        file_train.write(imgs_dir + "/" + title + '.png' + "\n")
        counter = counter + 1
