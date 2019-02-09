var socket = new WebSocket("ws://" + window.location.hostname + ":8080/websocket") //TODO remove reliance on 8080 part

socket.onopen = function() {
    socket.send("Test");
};
socket.onmessage = function(socketResponse) {
    alert(socketResponse.data);
}