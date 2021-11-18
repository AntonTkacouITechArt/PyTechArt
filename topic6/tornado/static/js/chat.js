'use strict';

const btn = document.getElementById('send');
const message = document.getElementById('message')
const chat = document.getElementById('chatview')
// const online_count = document.getElementById('online_count')
const online_users = document.getElementById('online');

let path = window.location.pathname.replace(/\//g,'');
let url = `ws://127.0.0.1:8000/${path}/websocket/`
let chatroom = `ws://127.0.0.1:8000/${path}/chatroom/`

let socket_user = new WebSocket(url);
let socket_chatroom = new WebSocket(chatroom);


socket_user.onopen = function() {
   socket_user.send("connect to chat");
};

socket_chatroom.onopen = function() {
    socket_chatroom.send('');
   // let pElem = document.createElement('p');
   // pElem.textContent = event.data;
   // online_users.append(pElem);
}

socket_user.onclose = function(event) {

  if (event.wasClean) {
      socket_user.send("disconnect success")
  } else {
    alert('Обрыв соединения');
  }
  if (event.reason == ''){
    alert('Код: ' + event.code + ' причина: Admin reload chat' );
  }
  else {
      alert('Код: ' + event.code + ' причина: ' + event.reason);
  }
};

socket_chatroom.onclose = function(event) {
  if (event.wasClean) {
      socket_chatroom.send("")
  } else {
    alert('Обрыв соединения');
  }
  if (event.reason == ''){
    alert('Код: ' + event.code + ' причина: Admin reload chat' );
  }
  else{
    alert('Код: ' + event.code + ' причина: ' + event.reason);
  }
};


socket_user.onmessage = function(event) {
   let pElem = document.createElement('p');
   pElem.textContent = event.data;
   chat.append(pElem);
};


socket_chatroom.onmessage = function(event) {
   let pElem = document.createElement('p');
   pElem.textContent = event.data;
   online_users.append(pElem);
};

btn.addEventListener('click', () => {
  socket_user.send(message.value);
});