// this script keeps sidebar height same as content height
$(document).ready(function(){

    console.log($(document).height())
    if (window.matchMedia('(min-width: 992px)').matches) {
        var docHeight = $(document).height();
        $('.sidebar').height(docHeight);
    }

    $(window).resize(function(){
        console.log($(document).height())
        if (window.matchMedia('(min-width: 992px)').matches) {
            var docHeight = $(document).height();
            $('.sidebar').height(docHeight);
        } else {
            $('.sidebar').height('auto');
        }
    });

    hljs.initHighlightingOnLoad();
});
