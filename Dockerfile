FROM ros:noetic

RUN apt-get update && apt-get install -y wget python3-pip
RUN pip install websocket-client requests

RUN wget https://dot.net/v1/dotnet-install.sh
RUN chmod +x ./dotnet-install.sh
RUN ./dotnet-install.sh --channel 7.0

RUN echo 'export DOTNET_ROOT=$HOME/.dotnet' >> ~/.bashrc
RUN echo 'export PATH=$PATH:$HOME/.dotnet:$HOME/.dotnet/tools' >> ~/.bashrc

COPY ./catkin_ws /catkin_ws

RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; cd /catkin_robot; catkin_make'
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
RUN echo "source /catkin_robot/devel/setup.bash" >> ~/.bashrc

COPY ./Server /Server

EXPOSE 5213

WORKDIR /catkin_ws

COPY ./start.sh .
RUN chmod +x ./start.sh

ENTRYPOINT [ "./start.sh" ]