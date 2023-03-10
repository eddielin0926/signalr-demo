import json
import time
from websocket import create_connection
import requests
import rospy
from std_msgs import String

class Sender():
    def __init__(self) -> None:
        rospy.loginfo("Setting up node ...")

        rospy.init_node('signalr_sender')

        # SignalR Initialization
        negotiation = requests.post(
            f"http://127.0.0.1:5213/robotic-arm-hub/negotiate?negotiateVersion=0"
        ).json()
        connection_id = negotiation["connectionId"]
        rospy.loginfo(f"connection id: {connection_id}")
        self.signalr_ws = create_connection(
            f"ws://127.0.0.1:5213/robotic-arm-hub?id={connection_id}")

        rospy.loginfo("Complete initialization")

    def toSignalRMessage(self, data):
        return f"{json.dumps(data)}\u001e"

    def _build_message(self, target, args):
        return {
            "type": 1,
            "target": target,
            "arguments": args,
        }

    def run(self):
        def callback(data):
            rospy.loginfo(f"receive: {data}")

            msg = self._build_message("SendAngles", ["amr1", time.time(), data.joint_1, data.joint_2, data.joint_3,data.joint_4,data.joint_5,data.joint_6])
            self.signalr_ws.send(self.toSignalRMessage(msg))
            recv = self.signalr_ws.recv()
            rospy.loginfo(f"receive signalr: {recv}")

        def handshake():
            self.signalr_ws.send(self.toSignalRMessage(
                {"protocol": "json", "version": 1}))
            handshake_response = self.signalr_ws.recv()
            rospy.loginfo(f"handshake response: {handshake_response}")

        def ping(data):
            rospy.loginfo('ping SignalR server')
            self.signalr_ws.send(self.toSignalRMessage({"type": 6}))

        handshake()

        rospy.Subscriber('mycobot/angles_real', String, callback=callback)
        rospy.Timer(rospy.Duration(10), ping)

        rospy.spin()


if __name__ == "__main__":
    s = Sender()
    s.run()