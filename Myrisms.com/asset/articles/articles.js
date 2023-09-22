function dropdown() {
    let status = $('#dropdown').css('display')
    if (status == 'block') {
        $('#dropdown').hide()
        $('#hambuger').attr('src', '../asset/hambuger1.png')
    } else {
        $('#dropdown').show()
        $('#hambuger').attr('src', '../asset/hambuger2.png')
    }
}

