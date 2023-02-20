# 1. https://github.com/dotnet/aspnetcore/blob/main/src/SignalR/docs/specs/TransportProtocols.md
# 2. https://github.com/dotnet/aspnetcore/blob/main/src/SignalR/docs/specs/HubProtocol.md

import asyncio
import websockets
import requests
import json
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s]\t%(message)s')

host = "localhost"
port = "5213"
negotiation = requests.post(f'http://{host}:{port}/amr-hub/negotiate?negotiateVersion=0').json()

def toSignalRMessage(data):
    return f'{json.dumps(data)}\u001e'

async def connectToHub(connectionId):
    uri = f"ws://{host}:{port}/amr-hub?id={connectionId}"
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
        ping_task  = asyncio.create_task(ping())
        listen_task = asyncio.create_task(listen())

        # Sending data
        for i in range(5):
            message = {
                "type": 1,
                "target": "SendMessage",
                "arguments": [ f"test data {i}" ]
            }
            await websocket.send(toSignalRMessage(message))
            await asyncio.sleep(5)

        _running = False
        await ping_task
        await listen_task

logging.info(f"connection id: {negotiation['connectionId']}")
asyncio.run(connectToHub(negotiation['connectionId']))