//JQuery(document).ready(function(){});
$(function() {
    'use strict';

    //Menu fijo
    var barraAltura = $('.barra').innerHeight();
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll == barraAltura) {
            $('.barra').removeClass('fixed');
            $('.contenido-header').removeClass('sinbarra');
            $('body').css({ 'margin-top': '0px' });

        } else {
            $('.barra').addClass('fixed');
            $('.contenido-header').addClass('sinbarra');
            $('body').css({ 'margin-top': barraAltura + 'px' });
        }

    });
});