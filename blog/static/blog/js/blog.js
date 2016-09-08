$(document).ready(function () {

    $('.post-status').each(function () {
        if ($(this).html() == 'published') {
            $(this).css('color', 'green');
        } else {
            $(this).css('color', 'orange');
        }
    });

    hljs.initHighlightingOnLoad();
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