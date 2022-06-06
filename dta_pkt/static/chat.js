var socket = io('http://127.0.0.1:5000');
socket.on('connect', function() {
    console.log("conected");
    // TODO: let the server know my username and get room number into local storage
});

function Triger_disconect() {
  // TODO: send room number to disconect
  socket.emit('client_disconnecting', 'bye');
}

function SendToServer() {
    socket.emit('new message',{message: document.getElementById("myText").value});
    document.getElementById("myText").value = ''
}
socket.on('incoming message', function(data){
  console.log(data['message']);
  var ul = document.getElementById("chatView");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(data['message']));
  ul.appendChild(li);
});
