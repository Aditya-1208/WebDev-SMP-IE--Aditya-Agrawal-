function pp1(){
    var username = document.getElementById("username_for_avatar").value
    document.getElementById("pp").src = "https://api.multiavatar.com/" + username + ".png"
}
window.onload = pp1();