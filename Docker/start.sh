#!/bin/bash

export DOTNET_ROOT=$HOME/.dotnet
export PATH=$PATH:$HOME/.dotnet:$HOME/.dotnet/tools
cd /Server
dotnet run &

cd /catkin_robot
source devel/setup.bash
roscore &

sleep 5

cd /catkin_robot/src/krnx_msgs/scripts
python3 listener.py &

cd /catkin_robot
rosbag play -l four_robots.bag