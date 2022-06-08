var socket = io('http://127.0.0.1:5000');
//when new user conects it updates list of abailable users
socket.on('new active user', function(message){
  // TODO: make this update abailable user list
  var ul = document.getElementById("connected_users");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(message));
  li.setAttribute("id", message);
  ul.appendChild(li);
});

//when client types message it sends it to the server
function SendToServer() {
    socket.emit('new message',{message: document.getElementById("myText").value});
    document.getElementById("myText").value = ''
}

//displays incomingo message into the chatView
// TODO: make it diference betwen mesages sent by client or difeent user
socket.on('incoming message', function(data){
  console.log(data['message']);
  var ul = document.getElementById("chatView");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(data['message']));
  ul.appendChild(li);
});

// lets server know when cleint disconected
function Triger_disconect() {
  // TODO: send client room number so server knows its gone
  socket.emit('client_disconnecting', 'bye');
  window.location.replace("/");
}
