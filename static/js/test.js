$(document).ready(function(){
    $("#thing").click(function(){
        $(".container").addClass('horizTranslate');
        var computedStyle = $(window).height();
        console.log(computedStyle);
        var marginBottom = $('.container').height();
        console.log(marginBottom);
        $(".container").animate({
            opacity: 0,
            top:computedStyle

        });
        $(".container").removeClass('horizTranslate');
    });
});

