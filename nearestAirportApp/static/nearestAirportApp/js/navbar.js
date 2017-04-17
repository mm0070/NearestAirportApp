$('.burger').on('click', function(){
        $("nav").toggleClass("showing");
        $("#navbar").toggleClass("extend");
    });

    $(window).scroll(function() {
            var scroll = $(window).scrollTop();
        
                if (scroll >= 30) {
                    $("#navbar").addClass("scrolled");
                    $("#logo").addClass("scrolledLogo");
                    $("#navID").addClass("scrolledNavbar");
                } else {
                    $("#navbar").removeClass("scrolled");
                    $("#logo").removeClass("scrolledLogo");
                    $("#navID").removeClass("scrolledNavbar");
                }

        });