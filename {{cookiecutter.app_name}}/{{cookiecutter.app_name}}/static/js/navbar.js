var nav = document.querySelector('nav')

window.addEventListener('scroll', function () {
    if (window.pageYOffset > 100) {
        nav.classList.add('bg-dark', 'shadow')
    } else {
        if (window.outerWidth > 992){
            nav.classList.remove('bg-dark', 'shadow')
        }
    }
})

window.addEventListener('resize', function () {
    if (window.outerWidth <= 992) {
        nav.classList.add('bg-dark', 'shadow')
    } else {
        if (window.pageYOffset < 100) {
            nav.classList.remove('bg-dark', 'shadow')
        }
    }
})