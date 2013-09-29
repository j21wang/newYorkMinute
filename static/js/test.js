$(document).ready(function(){
    $(".next.button").click(function(){
        var topic = $(".topic").val();
            if(topic != ""){
            $("#read").addClass('downTranslate');
            var computedStyle = $(window).height();
            console.log(computedStyle);
            var marginBottom = $('.container').height();
            console.log(marginBottom);
            $("#read").animate({
                opacity: 0,
                top:computedStyle,
                height: 0
            });
            $("#read").removeClass('downTranslate');

            $("select").show();
            $(".next.button").hide();
            $(".topic").hide();
            $(".submit").show();
            $("#time").fadeIn();

         
        } 
    });
});

