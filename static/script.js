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

//jQuery
$(document).ready(function() {
    $('#language-bars-container').click(function(){
        DisplayIdToggle('git-langs-list-container');
        padding = $('.repo-page-info').css('margin-bottom');
        if(padding === '50px') {
            $('.repo-page-info').css('margin-bottom', '20px');
        }
        else {
            $('.repo-page-info').css('margin-bottom', '50px');
        }
    });    
});