# SingalR Demo

`Server` is ASP.NET server for SingalR and `Client` is the client implement in python.

## Environment

### Server

Install .NET 7.0

### Client

Install Pipenv

## Start

### Server

```shell
cd Server
dotnet run
```

### Client

#### Listener

This is just an example. It's not necessary to run this program.

```shell
cd Client
pipenv shell
python amr-client.py
```

#### Emulator

```shell
cd Client
pipenv shell
python amr-emulator.py
```

## Develop

Modify the sending data section in `amr-emulator.py`.

```python
# Sending data
for i in range(5):
    message = {
        "type": 1,
        "target": "SendMessage",
        "arguments": [ f"test data {i}" ]
    }
    await websocket.send(toSignalRMessage(message))
    await asyncio.sleep(5)
```
