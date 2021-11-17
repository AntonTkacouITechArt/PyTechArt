'use strict';

const btn = document.getElementById('send');
const message = document.getElementById('message')
const chat = document.getElementById('chatview')
let path = window.location.pathname.replace(/\//g,'');
let url = `ws://127.0.0.1:8000/${path}/websocket/`
const socket = new WebSocket(url);

socket.onopen = function() {
   socket.send("connect to chat");
};

socket.onclose = function(event) {
  if (event.wasClean) {
    socket.send("disconnect to chat")
  } else {
    alert('Обрыв соединения');
  }
  alert('Код: ' + event.code + ' причина: ' + event.reason);
};

socket.onmessage = function(event) {
   let pElem = document.createElement('p');
   pElem.textContent = event.data;
   chat.append(pElem);
};

btn.addEventListener('click', () => {
  socket.send(message.value);
});