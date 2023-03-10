FROM ros:noetic

ENV ROS_WS=catkin_ws

RUN apt-get update && apt-get install -y python3-pip
RUN pip install websocket-client requests

COPY ./${ROS_WS} /${ROS_WS}

WORKDIR ${ROS_WS}

RUN /ros_entrypoint.sh catkin_make

# source ros package from entrypoint
RUN sed --in-place --expression \
      '$isource "/catkin_ws/devel/setup.bash"' \
      /ros_entrypoint.sh

ENTRYPOINT [ "/ros_entrypoint.sh" ]
CMD [ "roslaunch", "krnx_msgs", "replay.launch" ]