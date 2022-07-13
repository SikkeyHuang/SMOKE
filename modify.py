import os,sys

imagesetpath = "/home/carla/SMOKE/datasets/kitti/testing/ImageSets/"
testfilepath = imagesetpath+'test.txt'

frame_nums = 50 #indicate how many frames to test

ff = open(testfilepath,'w')

for i in range(frame_nums-1):
	ff.write("%06d\n"%i)
ff.write("%06d"%(i+1))


import shutil
imagepath = "/home/carla/carla_data/vehicle_data_2/"
arr = sorted(os.listdir(imagepath))



for i in range(frame_nums):
	src=imagepath+arr[i]
	dst="/home/carla/SMOKE/datasets/kitti/testing/image_2/%06d.png"%i
	shutil.copy(src,dst)

