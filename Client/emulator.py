# 1. https://github.com/dotnet/aspnetcore/blob/main/src/SignalR/docs/specs/TransportProtocols.md
# 2. https://github.com/dotnet/aspnetcore/blob/main/src/SignalR/docs/specs/HubProtocol.md

import asyncio
import websockets
import requests
import json
import logging
import time
import random
from requests.adapters import HTTPAdapter, Retry

logging.basicConfig(level=logging.INFO, format="[%(levelname)s]\t%(message)s")

HOST = "127.0.0.1"
PORT = "5213"
HUB = "robotic-arm-hub"
MODES = ["idle", "move patrol", "move dock", "delivery specimen", "delivery expendables"]

session = requests.Session()
adapter = HTTPAdapter(max_retries=Retry(total=5, backoff_factor=1))
session.mount("http://", adapter)
session.mount("https://", adapter)
negotiation = session.post(
    f"http://localhost:5213/{HUB}/negotiate?negotiateVersion=0",
).json()

class Message(object):
    def __init__(self, type, target, arguments):
        self.type = type
        self.target = target
        self.arguments = arguments

    def __str__(self):
        return "type: {0} ,target: {1}, arguments: {3}".format(self.type, self.target, self.arguments)


def toSignalRMessage(data):
    return f"{json.dumps(data)}\u001e"

async def connectToHub(connectionId):
    uri = f"ws://localhost:5213/{HUB}?id={connectionId}"
    async with websockets.connect(uri) as websocket:
        # https://github.com/dotnet/aspnetcore/blob/main/src/SignalR/docs/specs/HubProtocol.md#overview
        async def handshake():
            await websocket.send(toSignalRMessage({"protocol": "json", "version": 1}))
            handshake_response = await websocket.recv()
            logging.info(f"handshake response: {handshake_response}")

        # https://github.com/dotnet/aspnetcore/blob/main/src/SignalR/docs/specs/HubProtocol.md#ping-message-encoding
        async def ping():
            while _running:
                await asyncio.sleep(10)
                await websocket.send(toSignalRMessage({"type": 6}))

        async def listen():
            while _running:
                recv = await websocket.recv()
                logging.info(f"receive: {recv}")

        await handshake()

        _running = True
        ping_task = asyncio.create_task(ping())
        listen_task = asyncio.create_task(listen())

        t = 0.9;
        while _running:
            t = t + 0.1
            message = {
                "type": 1,
                "target": "SendAngles",
                "arguments": [
                    "robot1",
                    str(t),
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
            }
            #logging.info(f"send: {message}")
            await websocket.send(toSignalRMessage(message))
            await asyncio.sleep(1)

        await ping_task
        await listen_task

logging.info(f"connection id: {negotiation['connectionId']}")
asyncio.run(connectToHub(negotiation["connectionId"]))
