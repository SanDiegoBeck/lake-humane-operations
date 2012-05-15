//
// Preload the images for the page
//
var images = new Array()
images[0] = "/images/paw.jpg";
images[1] = "/images/header_animals.jpg";
images[2] = "/images/logo.png";

var cached_images = new Array();

for(i = 0; i < images.lenth; i++ ){
	cached_images[i] = new Image();
	cached_images[i].src = images[i];
}
