function VisibilityIdToggle(idname){
    var x = document.getElementById(idname);
    if(window.getComputedStyle(x).visibility === "hidden"){
        document.getElementById(idname).style.visibility = "visible"; 
        return 0;
    }
    if(window.getComputedStyle(x).visibility === "visible"){
        document.getElementById(idname).style.visibility = "hidden"; 
        return 0;
    }
    
}
function DisplayIdToggle(idname) {
    var x = document.getElementById(idname);
    if(window.getComputedStyle(x).display === "none"){
        document.getElementById(idname).style.display = "block"; 
        return 0;
    }
    if(window.getComputedStyle(x).display === "block"){
        document.getElementById(idname).style.display = "none"; 
        return 0;
    }
}
function Slide(idname){
    document.getElementById(idname).classList.toggle('closed');
    return 0;
}
function display() {
    var ele = document.getElementById('more-links');
    var dis = getComputedStyle(ele).top;
    if(dis === "-130px") {
        ele.style.top = '60px';
        return;
    }
    else {
        ele.style.top = '-130px';
        return;
    }  
}
function scroll() {
    console.log('document.body.scrollTop');
}
function displayList() {
    DisplayIdToggle('git-langs-list-container');
    padding = $('.repo-page-info').css('margin-bottom');
    if(padding === '50px') {
        $('.repo-page-info').css('margin-bottom', '20px');
    }
    else {
        $('.repo-page-info').css('margin-bottom', '50px');
    }
}
$(document).ready(() => {
    document.body.onscroll = () => {
        if (window.pageYOffset > 0) {
            document.getElementById('navbar').style.backgroundColor = 'white';
            var elems = document.getElementsByClassName('link');
            for (let i in elems) {
                elems[i].className = "link link1";
            }
        }
        else if (window.pageYOffset == 0) {
            document.getElementById('navbar').style.backgroundColor = 'transparent';
            var elems = document.getElementsByClassName('link link1');
            for (let i in elems) {
                elems[i].className = "link";
            }
            if (elems.length > 0) elems[0].className = 'link';
        }
    }  
});