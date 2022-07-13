groundtruth = open('vehicle_output_1.txt','r').readlines()
groundtruth_filter = open('ground_truth.txt','w')
local = open('vehicle_output_2.txt','r').readlines()
local_filter = open('camera_loc.txt','w')
diff = open('locdiff.txt','w')

for i in range(50):
	loc_gx,loc_gy = float(groundtruth[(39+i)*21].split(' ')[0]),float(groundtruth[(39+i)*21].split(' ')[1])
	loc_cx,loc_cy = float(local[i*22].split(' ')[0]),float(local[i*22].split(' ')[1])

	diff.write(str(loc_gx-loc_cx)+' '+str(loc_gy-loc_cy)+'\n')

	groundtruth_filter.write(groundtruth[39+i*21])
	local_filter.write(local[i*22])
	
