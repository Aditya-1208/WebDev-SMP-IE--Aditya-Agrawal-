window.onload = function(){
var message_element = document.getElementsByClassName("alert")
setTimeout(function(){
    for (let message of message_element){
        message.style.display = "none";
    }
},1500)
}