let NavbarBtn;
let btnIcon;
let navLinks;


function init(page){
    NavbarBtn = document.getElementById('navbar-btn');
    btnIcon = document.getElementById('btn-icon');
    navLinks = document.querySelectorAll('.nav-links')[0];
    removeAllActive(page);
    try {
        document.getElementById(page).classList.add('active')
    } catch (error) {
        
    }

}  

function removeAllActive(page){
    if(page !== 'home'){
        document.getElementById('home').classList.remove('active');
    }
    if(page !== 'about'){
        document.getElementById('about').classList.remove('active');
    }
    if(page !== 'coaching'){
        document.getElementById('coaching').classList.remove('active');
    }
    if(page !== 'contact'){
        document.getElementById('contact').classList.remove('active');
    }
    if(page !== 'blog'){
        document.getElementById('blog').classList.remove('active');
    }
    if(page !== 'athletes'){
        document.getElementById('athletes').classList.remove('active');
    }
}

function dropdown(){
    document.getElementById('submenu').classList.toggle("open");
    document.getElementById('arrow').classList.toggle("open");
}

// them navigation menu apperas if the icon is clicked
function toggleNavbar() {
    btnIcon.classList.toggle('openNav');
    navLinks.classList.toggle('openNav');
}


function closeImg(){
    document.getElementById('image-container').classList.add('d-none');
    document.getElementById('body').classList.remove('noscroll');
}

function openImg(imgUrl){
    document.getElementById('image-container').classList.remove('d-none');
    document.getElementById('body').classList.add('noscroll');
    document.getElementById('detail-image').src = imgUrl;
}





