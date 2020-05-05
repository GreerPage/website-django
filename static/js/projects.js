function getXCordForTitle() {
    var idname = document.getElementsByClassName('repo-container')[0].id;
    var elem = document.getElementById(idname);
    return elem.offsetLeft;
}
function updateTitle() {
    $('.projecttitle').css('position', 'relative');
    $('.projecttitle').css('left', getXCordForTitle());
}
$(document).ready(function() {
    updateTitle();
});
window.onresize = updateTitle;