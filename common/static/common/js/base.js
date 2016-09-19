var navy = '#34495E';
var djangoDarkGreen = '#0C4B33';
var djangoGreen = '#44B78B';
var djangoLightGreen = '#C9F0DD';

$(window).on('load', function () {

    var circleLogo = $('#circle-logo');

    $('#preloader-div').delay(1000).fadeOut("slow", function () {
        var logoSrc = circleLogo.attr('src');
        circleLogo.attr('src', logoSrc);
    });
});


$(document).ready(function () {

    var circleLogo = $('#circle-logo');
    var navbar = $('.navbar');
    var navbarBrand = $('.navbar-default .navbar-brand');
    var body = $('body');


    $("[href]").each(function () {
        if (this.href == window.location.href) {
            $(this).addClass("active");
        }
    });

    if (body.hasClass('home')) {
        $('.menu-item:first a').addClass('active');
    } else if (body.hasClass('blog')) {
        $('.menu-item:nth-of-type(2) a').addClass('active');
    } else if (body.hasClass('about')) {
        $('.menu-item:nth-of-type(3) a').addClass('active');
    } else if (body.hasClass('contact')) {
        $('.menu-item:nth-of-type(4) a').addClass('active');
    }

    var activeLink = $('.navbar-default .navbar-nav li a.active');

    if (body.hasClass('home')) {
        activeLink.css({
            'color': 'deepskyblue'
        });
    } else {
        activeLink.css({
            'color': djangoGreen
        });
    }


    // change home page's header height
    var currentWindowHeight = $(window).height();
    //console.log(currentWindowHeight);
    $('header').css({
        'height': currentWindowHeight
    });
    $('#bg-image').css({
        'height': currentWindowHeight
    });

    // reload logo animation
    $('#circle-logo-wrap').mouseenter(function () {
        var logoSrc = circleLogo.attr('src');
        circleLogo.attr('src', logoSrc);
    });

    // change scrolltop when logo is clicked
    $('a.page-scroll').bind('click', function (event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 800, 'easeInExpo');
        event.preventDefault();
    });


    // Scroll Control
    $(window).scroll(function () {

        var scrollTop = $(window).scrollTop();

        // console.log(scrollTop);

        if (scrollTop > 800) {
            $('#back-to-top').css({right: 0});
        } else {
            $('#back-to-top').css({right: "-50px"});
        }

        // Hide navbar when scrollTop is over 600
        if (scrollTop > 600) {
            navbar.css({
                'top': '-100px'
            });
        } else {
            navbar.css({
                'top': 0
            });
        }

        // navbar for blog
        if (scrollTop > 40) {
            navbar.css({
                'background-color': djangoDarkGreen,
                'border-bottom': '1px solid #34495E'
            });
            $('.navbar-default .navbar-nav li a, .navbar-default .navbar-brand').css({
                'color': 'white',
                'background-color': 'transparent'
            });
            navbarBrand.mouseenter(function () {
                $(this).css({
                    'color': '#93278F'
                });
            });
            navbarBrand.mouseleave(function () {
                $(this).css({
                    'color': 'white'
                });
            });
            activeLink.css({
                'color': djangoGreen
            });
        } else {
            navbar.css({
                'background-color': 'white',
                'border-bottom': '1px solid #34495E'
            });
            $('.navbar-default .navbar-nav li a, .navbar-default .navbar-brand').css({
                'color': djangoDarkGreen,
                'background-color': 'transparent'
            });
            navbarBrand.mouseenter(function () {
                $(this).css({
                    'color': '#39B54A'
                });
            });
            navbarBrand.mouseleave(function () {
                $(this).css({
                    'color': djangoDarkGreen
                });
            });
            activeLink.css({
                //'background-color'  : djangoDarkGreen,
                'color': djangoGreen
            });
        }

        // navbar for home
        if ($('body').hasClass('home')) {

            activeLink.css({
                //'background-color'  : 'white',
                'color': 'deepskyblue'
            });

            if (scrollTop > 40) {
                navbar.css({
                    'background-color': 'black',
                    'border-bottom': '1px solid #ccc'
                });
                $('.navbar-default .navbar-nav li a, .navbar-default .navbar-brand').css({
                    'color': 'white',
                    'background-color': 'transparent'
                });
                navbarBrand.mouseenter(function () {
                    $(this).css({
                        'color': '#29ABE2'
                    });
                });
                navbarBrand.mouseleave(function () {
                    $(this).css({
                        'color': 'white'
                    });
                });
                activeLink.css({
                    'color': 'deepskyblue'
                });
            } else {

                navbar.css({
                    'background-color': 'rgba(255,255,255,0.1)',
                    'border-bottom': '1px solid #ccc'
                });
                $('.navbar-default .navbar-nav li a, .navbar-default .navbar-brand').css({
                    'color': '#ccc',
                    'background-color': 'transparent'
                });
                navbarBrand.mouseenter(function () {
                    $(this).css({
                        'color': '#39B54A'
                    });
                });
                navbarBrand.mouseleave(function () {
                    $(this).css({
                        'color': '#ccc'
                    });
                });
                activeLink.css({
                    'color': 'deepskyblue'
                });
            }
        }

    });

    new WOW().init();

});