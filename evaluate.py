resultpath = "/home/carla/SMOKE/tools/logs/inference/kitti_test/data/"
frame_nums = 50 #indicate how many frames to test




for i in range(frame_nums):
	ff1 = open(resultpath+"%06d.txt"%i,'r')
	lines = ff1.readlines()
	for line in lines:
		x,y,z = line.split(' ')[-5:-2]
		object_class = line.split(' ')[0]
		if object_class == 'Car':
			print(x,z)
			break
		else:
			print("0.0 0.0")
			break
		

