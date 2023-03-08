FROM ros:noetic

RUN apt-get update && apt-get install -y wget python3-pip libnss3-tools git
RUN pip install websocket-client requests

RUN wget https://dot.net/v1/dotnet-install.sh
RUN chmod +x ./dotnet-install.sh
RUN ./dotnet-install.sh --channel 7.0

RUN echo 'export DOTNET_ROOT=$HOME/.dotnet' >> ~/.bashrc
RUN echo 'export PATH=$PATH:$HOME/.dotnet:$HOME/.dotnet/tools' >> ~/.bashrc

COPY ./catkin_ws /catkin_ws

RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; cd /catkin_ws; catkin_make'
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc

COPY ./Server /Server

COPY ./dotnet-devcert /dotnet-devcert
RUN dotnet-devcert/create-dotnet-devcert.sh

EXPOSE 5213

COPY ./start.sh .
RUN chmod +x ./start.sh

CMD [ "./start.sh" ]