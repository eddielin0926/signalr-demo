"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/nyokkey").build();

connection.start().catch(function (err) {
    return console.error(err.toString());
});

connection.on("ReceiveLocation", function (message) {
    console.log(message);
});