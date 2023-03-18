#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import requests
import json
import yaml
import rospy
from geometry_msgs.msg import PoseStamped ,PoseArray
from std_msgs.msg import String
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
    def __init__(self, ssl, domain_name, hub):
        super(MyTopics, self).__init__()
        rospy.init_node("nyokkey_topics", anonymous=True)

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
        def callback(data):
            y = yaml.safe_load(str(data))
            rospy.loginfo(f"[ros] [location] receive: {y}")

            msg = self._build_message("SendLocation", [y])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            rospy.loginfo(f"[signalr] [location] send: {msg}")

            recv = self.signalr_ws.recv()
            rospy.loginfo(f"[signalr] [location] receive : {recv}")
        
        sub = rospy.Subscriber('/nyokkey/hmi/location', PoseStamped, callback=callback)
        rospy.spin()
                   
    def sub_nyokkey_rightarm(self):
        def callback(data):
            y = yaml.safe_load(str(data))
            rospy.loginfo(f"[ros] [rightarm] receive: {y}")

            msg = self._build_message("SendRightArm", [y])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            rospy.loginfo(f"[signalr] [rightarm] send: {msg}")

            recv = self.signalr_ws.recv()
            rospy.loginfo(f"[signalr] [rightarm] receive: {recv}")

        sub = rospy.Subscriber('/nyokkey/hmi/rightarm', PoseArray, callback=callback)
        rospy.spin()
                   
    def sub_nyokkey_leftarm(self):
        def callback(data):
            y = yaml.safe_load(str(data))
            rospy.loginfo(f"[ros] [leftarm] receive: {y}")

            msg = self._build_message("SendLeftArm", [y])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            rospy.loginfo(f"[signalr] [leftarm] send: {msg}")

            recv = self.signalr_ws.recv()
            rospy.loginfo(f"[signalr] [leftarm] receive: {recv}")

        sub = rospy.Subscriber('/nyokkey/hmi/leftarm', PoseArray, callback=callback)
        rospy.spin()
                   
    def sub_nyokkey_face(self):
        def callback(data):
            y = yaml.safe_load(str(data))
            rospy.loginfo(f"[ros] [face] receive: {y}")

            msg = self._build_message("SendFace", [y])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            rospy.loginfo(f"[signalr] [face] send: {msg}")

            recv = self.signalr_ws.recv()
            rospy.loginfo(f"[signalr] [face] receive: {recv}")

        sub = rospy.Subscriber('/nyokkey/hmi/face', PoseArray, callback=callback)
        rospy.spin()

    def sub_nyokkey_task(self):
        def callback(data):
            y = yaml.safe_load(str(data))
            rospy.loginfo(f"[ros] [task] receive: {y}")

            msg = self._build_message("SendTask", [y])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            rospy.loginfo(f"[signalr] [task] send: {msg}")

            recv = self.signalr_ws.recv()
            rospy.loginfo(f"[signalr] [task] receive: {recv}")

        sub = rospy.Subscriber('/nyokkey/hmi/task', String, callback=callback)
        rospy.spin()

   
if __name__ == "__main__":
    ssl = os.getenv('SSL', 'true').lower() in ('true', '1', 't')
    domain_name = os.getenv('DOMAIN_NAME', 'khi-signalr-server.azurewebsites.net')
    hub = os.getenv('HUB', 'nyokkey')

    Watcher()
    topics = MyTopics(ssl, domain_name, hub)
    topics.start()
