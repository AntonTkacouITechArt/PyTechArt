function submit_entry(){
    let data = {
        currency_1: document.getElementById("currency_1").value,
        currency_2: document.getElementById("currency_2").value,
        cur_val_1: document.getElementById("cur_val_1").value
    }
    console.log(window.location.href)
    console.log(data)
    fetch(`${window.location.href}`,{
        method: "POST",
        credentials: "include",
        body: JSON.stringify(data),
        cache: "no-cache",
        headers: new Headers({
        "content-type": "application/json"
        })
    })
    .then(
    function(response){
        if(response.status !== 200) {
            return 'Error';
        }
        response.json().then(function(data){
            console.log(data)
            document.getElementById('cur_val_2').value = data["cur_val_2"]
        })
    }
)}
