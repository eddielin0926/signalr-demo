#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import requests
import json
import rospy
# from std_msgs.msg import String
from krnx_msgs.msg import RobotState
import threading
import os
import signal
import json
from websocket import create_connection
import requests

class Watcher:
    def __init__(self):
        self.child = os.fork()
        if self.child == 0:
            return
        else:
            self.watch()

    def watch(self):
        try:
            os.wait()
        except KeyboardInterrupt:
           print("KeyBoardInterrupt")
           self.kill()
        sys.exit()

    def kill(self):
        try:
            os.kill(self.child, signal.SIGKILL)
        except OSError:
            pass


class MyTopics(object):
    def __init__(self):
        super(MyTopics, self).__init__()
        rospy.init_node("my_topics", anonymous=True)

        negotiation = requests.post(
            f"https://khi-signalr-server.azurewebsites.net/robotic-arm-hub/negotiate?negotiateVersion=0",
            verify=False
        ).json()
        connection_id = negotiation["connectionId"]
        rospy.loginfo(f"connection id: {connection_id}")
        self.signalr_ws = create_connection(
            f"wss://khi-signalr-server.azurewebsites.net/robotic-arm-hub?id={connection_id}")

        rospy.loginfo("start ...")
        self.lock = threading.Lock()
    
    def toSignalRMessage(self, data):
        return f"{json.dumps(data)}\u001e"

    def _build_message(self, target, args):
        return {
            "type": 1,
            "target": target,
            "arguments": args,
        }
    
    def start(self):
        def handshake():
            self.signalr_ws.send(self.toSignalRMessage(
                {"protocol": "json", "version": 1}))
            handshake_response = self.signalr_ws.recv()
            rospy.loginfo(f"handshake response: {handshake_response}")

        def ping(data):
            rospy.loginfo('ping SignalR server')
            self.signalr_ws.send(self.toSignalRMessage({"type": 6}))

        handshake()
        
        pa = threading.Thread(target=self.sub_robot1_angles)
        pb = threading.Thread(target=self.sub_robot2_angles)
        sa = threading.Thread(target=self.sub_robot3_angles)
        sb = threading.Thread(target=self.sub_robot4_angles)

        pa.setDaemon(True)
        pa.start()
        pb.setDaemon(True)
        pb.start()
        sa.setDaemon(True)
        sa.start()
        sb.setDaemon(True)
        sb.start()
       
        pa.join()
        pb.join()
        sa.join()
        sb.join() 

    
    def sub_robot1_angles(self):
        def callback1(data1):
            rospy.loginfo(f"robot1 receive: {data1}")

            msg = self._build_message("SendAngles", [data1.id, data1.time, 
                data1.joint_1, data1.joint_2, data1.joint_3, data1.joint_4, data1.joint_5, data1.joint_6])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            rospy.loginfo(f"robot1 send: {msg}")
            recv = self.signalr_ws.recv()
            rospy.loginfo(f"receive signalr: {recv}")
        
        sub = rospy.Subscriber('robot1', RobotState, callback=callback1)
        rospy.spin()
                   
    def sub_robot2_angles(self):
        def callback2(data2):
            rospy.loginfo(f"robot2 receive: {data2}")  

            msg = self._build_message("SendAngles", [data2.id, data2.time, 
                data2.joint_1, data2.joint_2, data2.joint_3, data2.joint_4, data2.joint_5, data2.joint_6])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            recv = self.signalr_ws.recv()
            rospy.loginfo(f"receive signalr: {recv}")

        sub = rospy.Subscriber('robot2', RobotState, callback=callback2)
        rospy.spin()
                   
    def sub_robot3_angles(self):
        def callback3(data3):
            rospy.loginfo(f"robot3 receive: {data3}") 

            msg = self._build_message("SendAngles", [data3.id, data3.time, 
                data3.joint_1, data3.joint_2, data3.joint_3, data3.joint_4, data3.joint_5, data3.joint_6])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            recv = self.signalr_ws.recv()
            rospy.loginfo(f"receive signalr: {recv}")

        sub = rospy.Subscriber('robot3', RobotState, callback=callback3)
        rospy.spin()
                   
    def sub_robot4_angles(self):
        def callback4(data4):
            rospy.loginfo(f"robot4 receive: {data4}") 

            msg = self._build_message("SendAngles", [data4.id, data4.time, 
                data4.joint_1, data4.joint_2, data4.joint_3, data4.joint_4, data4.joint_5, data4.joint_6])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            recv = self.signalr_ws.recv()
            rospy.loginfo(f"receive signalr: {recv}")

        sub = rospy.Subscriber('robot4', RobotState, callback=callback4)
        rospy.spin()

   
if __name__ == "__main__":
    Watcher()
    topics = MyTopics()
    topics.start()
    
