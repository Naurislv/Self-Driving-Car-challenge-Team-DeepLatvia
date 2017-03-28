# Team-DeepLatvia-Self-Driving-Car-challenge
Participation in [Udacity-DIDI](https://goo.gl/tVLrBx) self driving car challenge. Team DeepLativa.

[Brief challenge description - blog](http://blog.udacity.com/2017/03/udacity-didi-self-driving-car-challenge.html)

### Dataset

Download dataset and calibration data and place all files in right Datasets subdirectory as they downloaded.

##### Datasets/Didi-Training-Release-1 :

* [Dataset torrent](https://challenge.udacity.com/data/76352487923a31d47a6029ddebf40d9265e770b5.torrent)
* [Calibration data torrent](https://challenge.udacity.com/data/d9e413a9fbd07f668fd5370d53ee2691404ae32c.torrent)

##### Installing ROS and visualizing data on Ubuntu : [Follow instructions](https://github.com/jokla/didi_challenge_ros)

##### Reading .bags with python.

1. ROS officially supports only python2 so install python2
2. Install ROS. Full ROS installation (as explained above) contains python-rosbag which independently installed might not work.
3. If you are using Anaconda you may need to install catkin_pkg ```~/anaconda2/bin/conda install -c auto catkin_pkg```
4. As I always used Anacaonda3 (python 3.x) I had to install dependecies such as OpenCV. There was some issues, so see "Installing OpenCV for Anaconda2" of proper way to do it.
5. Example of how to load .bag file can be found python/load_bag_example.ipynb

##### Installing OpenCV for Anaconda2
```
~/anaconda2/bin/conda config --add channels menpo

~/anaconda2/bin/conda install opencv3

sudo apt-get install libstdc++6
sudo add-apt-repository ppa:ubuntu-toolchain-r/test && sudo apt-get update && sudo apt-get upgrade

~/anaconda2/bin/conda install libgcc
```
