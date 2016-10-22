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
        $('#inflearn-logo-purple').removeClass('hidden');
        $('#inflearn-logo').addClass('hidden');
    });
    inflearnLink.mouseleave(function () {
        $('#inflearn-logo-purple').addClass('hidden');
        $('#inflearn-logo').removeClass('hidden');
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