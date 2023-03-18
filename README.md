# SingalR Demo

`Server` is ASP.NET server for SingalR and `Client` is the client implement in python.

## Environment

- .NET 6.0
- Python

## Start Docker

```sh
docker build -t signalr-server .
docker run -it --rm -p 7067:7067 -p 5213:5213 signalr-server
```

## Start Solution

Open signalr-demo.sln and press start.