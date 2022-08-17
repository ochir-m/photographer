$(function () {
    $('.categories-nav-item .categories-nav-link').each(function () {
        var location = window.location.href
        var link = this.href
        var result = location.match(link);
        if(result != null) {
            $(this).addClass('onTop');
            $(this).parents('li').addClass('onTop');
        }
    });
});