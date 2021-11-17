// const btn_clear = document.getElementById('clear');
// const btn_reload = document.getElementById('reload');
//
// btn_clear.addEventListener('click', () => {
//     let data = {
//         chatroom: document.getElementById('sel_chatroom').value,
//         clear: true,
//     };
//
//     fetch(`${window.location.href}`, {
//         method: "POST",
//         credentials: "include",
//         body: JSON.stringify(data),
//         cache: "no-cache",
//         headers: new Headers({
//             "content-type": "application/json"
//         })
//     }).then(
//     function(response){
//         if(!response.ok) {
//             alert(`Error: ${response.statusText} \n
//              status code: ${response.status}`);
//         }else {
//             alert(`All messages deleted`);
//         }
//     })
// })
//
// btn_reload.addEventListener('click', () => {
//     let data = {
//         chatroom: document.getElementById('sel_chatroom').value,
//         reload: true,
//     };
//
//     fetch(`${window.location.href}`, {
//         method: "POST",
//         credentials: "include",
//         body: JSON.stringify(data),
//         cache: "no-cache",
//         headers: new Headers({
//             "content-type": "application/json"
//         })
//     }).then(
//     function(response){
//         if(!response.ok) {
//             alert(`Error: ${response.statusText} \n
//              status code: ${response.status}`);
//         }else {
//             alert(`ALl user kicked`);
//         }
//     })
// });
