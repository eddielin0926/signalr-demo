#!/bin/bash

export SSL=false
export DOMAIN_NAME=localhost:5000

dotnet /app/Server.dll &
roslaunch krnx_msgs replay.launch