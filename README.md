# Result: time 232s frames 7518;  32 FPS; 30 ms per frame
# Accuracy: check the toyotamap.png
  
# Note:
https://github.com/lzccccc/SMOKE


# install
conda activate py37 (specific version required)
conda install pytorch=1.3.1  cudatoolkit=10.0 -c pytorch (specific version required)
pip install yacs
pip install scikit-image
pip install Pillow==6.1 (specific version required)
conda install torchvision -c pytorch

realated 
https://github.com/prclibo/kitti_eval
https://github.com/sshaoshuai/PointRCNN/tree/master/data/KITTI/ImageSets

# Set up 
#load the weight model from lacal path, change it in configs/smoke_gn_vector.yaml
WEIGHT: "/home/carla/SMOKE/model_final.pth"

# using carla to capture images and gps data
#For example:
cd /opt/carla-simulator/PythonAPI/examples/examples
python measurement_data_1.py
python measurement_data_2.py
the collcted data is stored in /home/carla/carla_data/


# using python generate_location.py to generate grountruth and location difference file
mamunally set here, reason and challenges
gps and image frames are in different frequency (1 frame with ~20 gps)
the start and end time of each vehicle is not sychronized (the ground truth are not 100% accurate because of the time shift)
camera parameters are different between carla and existing trained models (camera location shift)
prediction results are not very accurate

# prepare the images and test.txt file, follow the setting in generate_location.py
python modify.py

# predict results
python tools/plain_train_net.py --eval-only --config-file "configs/smoke_gn_vector.yaml"

# get evaluation result
python evaluate.py

# matlab toyota_map.m for visualization

