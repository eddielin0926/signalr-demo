FROM ros:noetic

RUN apt-get update && apt-get install -y wget python3-pip
RUN pip install websocket-client requests

# Dotnet
RUN wget https://dot.net/v1/dotnet-install.sh
RUN chmod +x ./dotnet-install.sh
RUN ./dotnet-install.sh --channel 6.0

COPY ROS/catkin_ws /catkin_ws
WORKDIR /catkin_ws
RUN /ros_entrypoint.sh catkin_make

COPY Scripts/ /

COPY Server /Server
WORKDIR /Server
RUN /entrypoint.sh dotnet publish -c Release -o /app /p:UseAppHost=false

EXPOSE 5000
EXPOSE 5001

WORKDIR /app
ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "/robotic-arm.sh" ]
