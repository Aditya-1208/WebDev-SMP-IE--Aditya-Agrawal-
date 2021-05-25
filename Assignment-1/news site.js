// //using current date for website!
// let a=document.getElementById("today")
// let d =new Date
// // a.innerHTML=d.getMonth() + " " + d.getDate() + ", " + d.getFullYear()
// a.innerHTML=Date()
function date_update(){
    // date=new Date // date becomes an object of type Date,now we can access member functions!
    document.getElementById("today").innerText=Date()
}
date_update()
setInterval(date_update,1000)
function print(input){
alert(input);
}
function show_form(){
    document.getElementById("after_read_more").style.display="initial"
    document.getElementById("read_more").style.display="none"
}
var dialog = document.querySelector('dialog');
    // dialogPolyfill.registerDialog(dialog);
