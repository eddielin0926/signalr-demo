#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
from datetime import datetime, timedelta
import yaml
import rospy
from krnx_msgs.msg import RobotState
import threading
import os
import signal
import json
from websocket import create_connection
import requests
from requests.adapters import HTTPAdapter, Retry

session = requests.Session()
adapter = HTTPAdapter(max_retries=Retry(total=5, backoff_factor=1))
session.mount("http://", adapter)
session.mount("https://", adapter)

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
    def __init__(self, ssl, domain_name, hub, ms):
        self.ms = ms
        self.lastDateTime1 = datetime.min
        self.lastDateTime2 = datetime.min
        self.lastDateTime3 = datetime.min
        self.lastDateTime4 = datetime.min

        super(MyTopics, self).__init__()
        rospy.init_node("my_topics", anonymous=True)

        s = 's'if ssl else ''

        negotiation = session.post(
            f"http{s}://{domain_name}/{hub}/negotiate?negotiateVersion=0",
            verify=False
        ).json()
        connection_id = negotiation["connectionId"]
        rospy.loginfo(f"connection id: {connection_id}")
        self.signalr_ws = create_connection(
            f"ws{s}://{domain_name}/{hub}?id={connection_id}")

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
        def callback(data):
            dateTime = datetime.fromtimestamp(int(data.time) / 1000)
            if abs(dateTime - self.lastDateTime1) > timedelta(milliseconds=self.ms):
                y = yaml.safe_load(str(data))
                rospy.loginfo(f"[ros] [robot1] receive: {y}")

                msg = self._build_message("SendAngles", [data.id, data.time, 
                    data.joint_1, data.joint_2, data.joint_3, data.joint_4, data.joint_5, data.joint_6])
                self.signalr_ws.send(self.toSignalRMessage(msg))
                rospy.loginfo(f"[signalr] [robot1] send: {msg}")

                self.lastDateTime1 = dateTime
                recv = self.signalr_ws.recv()
                rospy.loginfo(f"[signalr] [robot1] receive: {recv}")
        
        sub = rospy.Subscriber('robot1', RobotState, callback=callback)
        rospy.spin()
                   
    def sub_robot2_angles(self):
        def callback(data):
            dateTime = datetime.fromtimestamp(int(data.time) / 1000)
            if abs(dateTime - self.lastDateTime2) > timedelta(milliseconds=self.ms):
                y = yaml.safe_load(str(data))
                rospy.loginfo(f"[ros] [robot2] receive: {y}")  

                msg = self._build_message("SendAngles", [data.id, data.time, 
                    data.joint_1, data.joint_2, data.joint_3, data.joint_4, data.joint_5, data.joint_6])
                self.signalr_ws.send(self.toSignalRMessage(msg))
                rospy.loginfo(f"[signalr] [robot2] send: {msg}")

                self.lastDateTime2 = dateTime
                recv = self.signalr_ws.recv()
                rospy.loginfo(f"[signalr] [robot2] receive: {recv}")

        sub = rospy.Subscriber('robot2', RobotState, callback=callback)
        rospy.spin()
                   
    def sub_robot3_angles(self):
        def callback(data):
            dateTime = datetime.fromtimestamp(int(data.time) / 1000)
            if abs(dateTime - self.lastDateTime3) > timedelta(milliseconds=self.ms):
                y = yaml.safe_load(str(data))
                rospy.loginfo(f"[ros] [robot3] receive: {y}") 

                msg = self._build_message("SendAngles", [data.id, data.time, 
                    data.joint_1, data.joint_2, data.joint_3, data.joint_4, data.joint_5, data.joint_6])
                self.signalr_ws.send(self.toSignalRMessage(msg))
                rospy.loginfo(f"[signalr] [robot3] send: {msg}")

                self.lastDateTime3 = dateTime
                recv = self.signalr_ws.recv()
                rospy.loginfo(f"[signalr] [robot3] receive: {recv}")

        sub = rospy.Subscriber('robot3', RobotState, callback=callback)
        rospy.spin()
                   
    def sub_robot4_angles(self):
        def callback(data):
            dateTime = datetime.fromtimestamp(int(data.time) / 1000)
            if abs(dateTime - self.lastDateTime4) > timedelta(milliseconds=self.ms):
                y = yaml.safe_load(str(data))
                rospy.loginfo(f"[ros] [robot4] receive: {y}") 

                msg = self._build_message("SendAngles", [data.id, data.time, 
                    data.joint_1, data.joint_2, data.joint_3, data.joint_4, data.joint_5, data.joint_6])
                self.signalr_ws.send(self.toSignalRMessage(msg))
                rospy.loginfo(f"[signalr] [robot4] send: {msg}")

                self.lastDateTime4 = dateTime
                recv = self.signalr_ws.recv()
                rospy.loginfo(f"[signalr] [robot4] receive: {recv}")

        sub = rospy.Subscriber('robot4', RobotState, callback=callback)
        rospy.spin()

   
if __name__ == "__main__":
    ssl = os.getenv('SSL', 'true').lower() in ('true', '1', 't')
    domain_name = os.getenv('DOMAIN_NAME', 'khi-signalr-server.azurewebsites.net')
    hub = os.getenv('HUB', 'robotic-arm-hub')
    milliseconds = int(os.getenv('milliseconds', '1000'))

    Watcher()
    topics = MyTopics(ssl, domain_name, hub, milliseconds)
    topics.start()
    
