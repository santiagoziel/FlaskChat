document.getElementById("user-name-submit").onclick = function() {myFunction()};

function myFunction() {
  username = document.getElementById("user-name-field").value;
  if(username.length == 0) return false;
  //socket.emit('new user', {username: username});
  window.location.replace("/chat");
}
