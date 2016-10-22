$(document).ready(function () {

    $('.post-status').each(function () {
        if ($(this).html() == 'published') {
            $(this).css('color', 'green');
        } else {
            $(this).css('color', 'orange');
        }
    });

    hljs.initHighlightingOnLoad();

    var inflearnLink = $('.inflearn a');
    inflearnLink.mouseenter(function () {
        $('#inflearn-logo').attr('src', '/static/blog/img/inflearn_logo_purple.png');
        console.log($(self).find('img'));
    });
    inflearnLink.mouseleave(function () {
        $('#inflearn-logo').attr('src', '/static/blog/img/inflearn_logo.png');
        console.log($(self).find('img'));
    });
});

// this script keeps sidebar height same as content height
// $(window).on('load resize', function () {
//     if (window.matchMedia('(min-width: 992px)').matches) {
//         var docHeight = $(document).height();
//         $('.sidebar').height(docHeight);
//     } else {
//         $('.sidebar').height('auto');
//     }
// });