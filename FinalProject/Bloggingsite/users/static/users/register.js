(function () {
    'use strict'
    const forms = document.querySelectorAll('.requires-validation')
    Array.from(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()


function generateAvatar() {
    var username = document.getElementById("username").value;
    var svgCode = multiavatar(username);
    document.getElementById("avatar-div").innerHTML = svgCode;
    document.getElementById("avatar_data").value=svgCode;
    document.getElementById("avatartext").style.display="";
    
}