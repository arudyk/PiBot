function setBackground() {
     document.body.style.background="#f3f3f3 url('../../static/virt_tours/img/background_grey_line.png') no-repeat right top";
}

function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}
