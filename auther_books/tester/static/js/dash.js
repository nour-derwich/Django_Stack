$('.expand-btn-1').click(function() {

    $('.role-description').toggleClass('expand');
    $('.expand-btn-1').toggleClass('move-button');
    $('.image-card-1').toggleClass('color-reveal');
    $('.team-info').toggleClass('text-reduce');
    $('.team-info-des').toggleClass('text-reveal-1');
    
    });
console.log('jk');
let items = document.querySelectorAll('.carousel .carousel-item')

items.forEach((el) => {
    const minPerSlide = 4
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})

  