$('.one-time').slick({
    dots: true,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 2580,
    infinitive: true,
    slidesToShow: 1,
    slideToScroll: 1,
    fade: true,
    adaptiveHeight: true,
    cssEase: 'linear',
    responsive: [
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                dots: false
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                dots: false
            }
        }
    ]
});