#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import requests
import json
import rospy
from geometry_msgs.msg import PoseStamped ,PoseArray
from std_msgs.msg import String
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
        rospy.init_node("nyokkey_topics", anonymous=True)

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
        
        pa = threading.Thread(target=self.sub_nyokkey_location)
        pb = threading.Thread(target=self.sub_nyokkey_rightarm)
        sa = threading.Thread(target=self.sub_nyokkey_leftarm)
        sb = threading.Thread(target=self.sub_nyokkey_face)
        da = threading.Thread(target=self.sub_nyokkey_task)

        pa.setDaemon(True)
        pa.start()
        pb.setDaemon(True)
        pb.start()
        sa.setDaemon(True)
        sa.start()
        sb.setDaemon(True)
        sb.start()
        da.setDaemon(True)
        da.start()
       
        pa.join()
        pb.join()
        sa.join()
        sb.join() 
        da.join()
   
    def sub_nyokkey_location(self):
        def callback1(data1):
            rospy.loginfo(f"location receive: {data1.pose.position.x, data1.pose.position.y,data1.pose.position.z, data1.pose.orientation.x, data1.pose.orientation.y, data1.pose.orientation.z, data1.pose.orientation.w}")

            # msg = self._build_message("location", [data1.pose.position.x, data1.pose.position.y, 
            #     data1.pose.position.z, data1.pose.orientation.x, data1.pose.orientation.y, data1.pose.orientation.z, data1.pose.orientation.w])
            # self.signalr_ws.send(self.toSignalRMessage(msg))
            # rospy.loginfo(f"location send: {msg}")
            # recv = self.signalr_ws.recv()
            # rospy.loginfo(f"receive signalr: {recv}")
        
        sub = rospy.Subscriber('/nyokkey/hmi/location', PoseStamped, callback=callback1)
        rospy.spin()
                   
    def sub_nyokkey_rightarm(self):
        def callback2(data2):
            rospy.loginfo(f"robot2 receive: {data2.poses[1].position.x}")  

            # msg = self._build_message("SendAngles", [data2])
            # self.signalr_ws.send(self.toSignalRMessage(msg))
            # recv = self.signalr_ws.recv()
            # rospy.loginfo(f"receive signalr: {recv}")

        sub = rospy.Subscriber('/nyokkey/hmi/rightarm', PoseArray, callback=callback2)
        rospy.spin()
                   
    def sub_nyokkey_leftarm(self):
        def callback3(data3):
            rospy.loginfo(f"robot3 receive: {data3}") 

            # msg = self._build_message("SendAngles", [data3])
            # self.signalr_ws.send(self.toSignalRMessage(msg))
            # recv = self.signalr_ws.recv()
            # rospy.loginfo(f"receive signalr: {recv}")

        sub = rospy.Subscriber('/nyokkey/hmi/leftarm', PoseArray, callback=callback3)
        rospy.spin()
                   
    def sub_nyokkey_face(self):
        def callback4(data4):
            rospy.loginfo(f"robot4 receive: {data4}") 

            # msg = self._build_message("SendAngles", [data4])
            # self.signalr_ws.send(self.toSignalRMessage(msg))
            # recv = self.signalr_ws.recv()
            # rospy.loginfo(f"receive signalr: {recv}")

        sub = rospy.Subscriber('/nyokkey/hmi/face', PoseArray, callback=callback4)
        rospy.spin()

    def sub_nyokkey_task(self):
        def callback4(data5):
            rospy.loginfo(f"robot5 receive: {data5}") 

            # msg = self._build_message("SendAngles", [data5])
            # self.signalr_ws.send(self.toSignalRMessage(msg))
            # recv = self.signalr_ws.recv()
            # rospy.loginfo(f"receive signalr: {recv}")

        sub = rospy.Subscriber('/nyokkey/hmi/task', String, callback=callback4)
        rospy.spin()

   
if __name__ == "__main__":
    Watcher()
    topics = MyTopics()
    topics.start()
