"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/nyokkey").build();

var startTime = new Date()
var messageCount = 0;

connection.start().catch(function (err) {
    return console.error(err.toString());
});

connection.on("ReceiveLocation", function (message) {
    messageCount += 1;
    var deltaTime = new Date() - startTime;
    var rate = (messageCount * 1000 / deltaTime).toFixed(2);
    document.getElementById("nyokkey-data").innerHTML = `
        Recieved ${messageCount} messages (${rate} msg / sec)
    `;

    var t = document.getElementById('location');
    t.innerHTML = `
        <tr id="location">
            <td>/nyokkey/hmi/location</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});

connection.on("ReceiveRightArm", function (message) {
    messageCount += 1;
    var deltaTime = new Date() - startTime;
    var rate = (messageCount * 1000 / deltaTime).toFixed(2);
    document.getElementById("nyokkey-data").innerHTML = `
        Recieved ${messageCount} messages (${rate} msg / sec)
    `;

    var t = document.getElementById('rightarm');
    t.innerHTML = `
        <tr id="rightarm">
            <td>/nyokkey/hmi/rightarm</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});

connection.on("ReceiveLeftArm", function (message) {
    messageCount += 1;
    var deltaTime = new Date() - startTime;
    var rate = (messageCount * 1000 / deltaTime).toFixed(2);
    document.getElementById("nyokkey-data").innerHTML = `
        Recieved ${messageCount} messages (${rate} msg / sec)
    `;

    var t = document.getElementById('leftarm');
    t.innerHTML = `
        <tr id="leftarm">
            <td>/nyokkey/hmi/leftarm</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});

connection.on("ReceiveFace", function (message) {
    messageCount += 1;
    var deltaTime = new Date() - startTime;
    var rate = (messageCount * 1000 / deltaTime).toFixed(2);
    document.getElementById("nyokkey-data").innerHTML = `
        Recieved ${messageCount} messages (${rate} msg / sec)
    `;

    var t = document.getElementById('face');
    t.innerHTML = `
        <tr id="face">
            <td>/nyokkey/hmi/face</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});

connection.on("ReceiveTask", function (message) {
    messageCount += 1;
    var deltaTime = new Date() - startTime;
    var rate = (messageCount * 1000 / deltaTime).toFixed(2);
    document.getElementById("nyokkey-data").innerHTML = `
        Recieved ${messageCount} messages (${rate} msg / sec)
    `;

    var t = document.getElementById('task');
    t.innerHTML = `
        <tr id="task">
            <td>/nyokkey/hmi/task</td>
            <td>${JSON.stringify(message)}</td>
        </tr>
    `;
});