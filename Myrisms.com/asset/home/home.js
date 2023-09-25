const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,

    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    autoplay: {
        delay: 2500,
    },
});

function dropdown() {
    let status = $('#dropdown').css('display')
    if (status == 'block') {
        $('#dropdown').hide()
        $('#hambuger').attr('src','asset/hambuger1.png')
    } else {
        $('#dropdown').show()
        $('#hambuger').attr('src','asset/hambuger2.png')
    }
}

