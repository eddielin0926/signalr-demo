#!/bin/bash

export DOTNET_ROOT=$HOME/.dotnet
export PATH=$PATH:$HOME/.dotnet:$HOME/.dotnet/tools

cd /Server
dotnet run --launch-profile "https" &

cd /catkin_ws
source devel/setup.bash
roscore &

sleep 5

cd /catkin_ws/src/krnx_msgs/scripts
python3 listener.py &

cd /catkin_ws
rosbag play -l four_robots.bag