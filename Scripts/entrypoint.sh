#!/bin/bash
set -e

# setup dotnet environment
export DOTNET_ROOT=$HOME/.dotnet
export PATH=$PATH:$HOME/.dotnet:$HOME/.dotnet/tools

# setup ros environment
source "/opt/ros/$ROS_DISTRO/setup.bash"
source /catkin_ws/devel/setup.bash

exec "$@"