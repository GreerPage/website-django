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

function Slide(idname){
    document.getElementById(idname).classList.toggle('closed');
    return 0;
}

//jQuery
$(document).ready(function() {
    function CheckWindowWidth(){
        if($(window).width() > 768){
            document.getElementById('smallmenu').classList.add('closed1');
        }
    }
    
});