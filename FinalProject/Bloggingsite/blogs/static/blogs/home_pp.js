function pp(){
    
    var blogsTotal = document.getElementById("blogs-total").value.toString();
    for(let blogNumber=1; blogNumber<=blogsTotal; blogNumber++)
    {
        var username = document.getElementById("username_for_avatar-"+blogNumber).value
        var blogId = document.getElementById("blog_id-"+blogNumber).value.toString();
        document.getElementById(blogId).src = "https://api.multiavatar.com/" + username + ".png"
    }
}
window.onload = pp();