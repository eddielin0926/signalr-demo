#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd
import rospy
import rosbag
from beginner_tutorials.msg import Robot
robot1 = pd.read_csv('/home/tina997726/catkin_robot/src/beginner_tutorials/scripts/robot1_KRNX.csv')
robot2 = pd.read_csv('/home/tina997726/catkin_robot/src/beginner_tutorials/scripts/robot2_KRNX.csv')
robot3 = pd.read_csv('/home/tina997726/catkin_robot/src/beginner_tutorials/scripts/robot3_KRNX.csv')
robot4 = pd.read_csv('/home/tina997726/catkin_robot/src/beginner_tutorials/scripts/robot4_KRNX.csv')
rospy.init_node("record_topics")
# def talker():
#     pub = rospy.Publisher('chatter', Robot, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     while not rospy.is_shutdown():
#         msg = Robot()
#         msg.id= "robot1"
#         msg.time = "11111"
#         msg.joint_1 = 12.2222
#         msg.joint_2 = 32.2222
#         msg.joint_3 = 42.2222
#         msg.joint_4 = 52.2222
#         msg.joint_5 = 62.2222
#         msg.joint_6 = 72.2222
#         # hello_str = "hello world %s" % rospy.get_time()
#         rospy.loginfo(msg)
#         pub.publish(msg)
#         rate.sleep()

# if __name__ == '__main__':
#     try:
#         talker()
#     except rospy.ROSInterruptException:
#         pass
with rosbag.Bag('four_robots.bag', 'w') as bag:
    for row in range(robot1.shape[0]):
        # rospy.Time.now()
        timestamp = rospy.Time.from_sec(robot1['timestamp'][row]/1000)  

        joints_msg1 = Robot()
        joints_msg1.id= "robot1"
        joints_msg1.time = str(robot1['timestamp'][row])
        joints_msg1.joint_1 = float(robot1['ang1j'][row])
        joints_msg1.joint_2 = float(robot1['ang2j'][row])
        joints_msg1.joint_3 = float(robot1['ang3j'][row])
        joints_msg1.joint_4 = float(robot1['ang4j'][row])
        joints_msg1.joint_5 = float(robot1['ang5j'][row])
        joints_msg1.joint_6 = float(robot1['ang6j'][row])

        joints_msg2 = Robot()
        joints_msg2.id= "robot2"
        joints_msg2.time = str(robot1['timestamp'][row])
        joints_msg2.joint_1 = float(robot2['ang1j'][row])
        joints_msg2.joint_2 = float(robot2['ang2j'][row])
        joints_msg2.joint_3 = float(robot2['ang3j'][row])
        joints_msg2.joint_4 = float(robot2['ang4j'][row])
        joints_msg2.joint_5 = float(robot2['ang5j'][row])
        joints_msg2.joint_6 = float(robot2['ang6j'][row])

        joints_msg3 = Robot()
        joints_msg3.id= "robot3"
        joints_msg3.time = str(robot1['timestamp'][row])
        joints_msg3.joint_1 = float(robot3['ang1j'][row])
        joints_msg3.joint_2 = float(robot3['ang2j'][row])
        joints_msg3.joint_3 = float(robot3['ang3j'][row])
        joints_msg3.joint_4 = float(robot3['ang4j'][row])
        joints_msg3.joint_5 = float(robot3['ang5j'][row])
        joints_msg3.joint_6 = float(robot3['ang6j'][row])

        joints_msg4 = Robot()
        joints_msg4.id= "robot4"
        joints_msg4.time = str(robot1['timestamp'][row])
        joints_msg4.joint_1 = float(robot4['ang1j'][row])
        joints_msg4.joint_2 = float(robot4['ang2j'][row])
        joints_msg4.joint_3 = float(robot4['ang3j'][row])
        joints_msg4.joint_4 = float(robot4['ang4j'][row])
        joints_msg4.joint_5 = float(robot4['ang5j'][row])
        joints_msg4.joint_6 = float(robot4['ang6j'][row])
        bag.write("robot3", joints_msg3, timestamp )
        bag.write("robot2", joints_msg2, timestamp )
        bag.write("robot1", joints_msg1, timestamp )
        bag.write("robot4", joints_msg4, timestamp )
bag.close()


# import json
# from websocket import create_connection
# import requests
# import rospy
# from std_msgs.msg import String
# from mycobot_communication.msg import MycobotAngles


# class Sender():
#     def __init__(self) -> None:
#         rospy.loginfo("Setting up node ...")

#         rospy.init_node('signalr_sender')

#         # SignalR Initialization
#         negotiation = requests.post(
#             f"http://127.0.0.1:5213/robotic-arm-hub/negotiate?negotiateVersion=0"
#         ).json()
#         connection_id = negotiation["connectionId"]
#         rospy.loginfo(f"connection id: {connection_id}")
#         self.signalr_ws = create_connection(
#             f"ws://127.0.0.1:5213/robotic-arm-hub?id={connection_id}")

#         rospy.loginfo("Complete initialization")

#     def toSignalRMessage(self, data):
#         return f"{json.dumps(data)}\u001e"

#     def _build_message(self, target, args):
#         return {
#             "type": 1,
#             "target": target,
#             "arguments": args,
#         }

#     def run(self):
#         def callback(data):
#             rospy.loginfo(f"receive: {data}")

#             msg = self._build_message("SendAngles", [f"{data.joint_1}",f"{data.joint_2}", f"{data.joint_3}",f"{data.joint_4}",f"{data.joint_5}",f"{data.joint_6}"])
#             self.signalr_ws.send(self.toSignalRMessage(msg))
#             recv = self.signalr_ws.recv()
#             rospy.loginfo(f"receive signalr: {recv}")

#         def handshake():
#             self.signalr_ws.send(self.toSignalRMessage(
#                 {"protocol": "json", "version": 1}))
#             handshake_response = self.signalr_ws.recv()
#             rospy.loginfo(f"handshake response: {handshake_response}")

#         def ping(data):
#             rospy.loginfo('ping SignalR server')
#             self.signalr_ws.send(self.toSignalRMessage({"type": 6}))

#         handshake()

#         rospy.Subscriber('mycobot/angles_real', MycobotAngles, callback=callback)
#         rospy.Timer(rospy.Duration(10), ping)

#         rospy.spin()


# if __name__ == "__main__":
#     s = Sender()
#     s.run()