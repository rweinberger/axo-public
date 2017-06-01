var slideIndex = 0;
var x = document.getElementsByClassName("slideshow");
rotate();

function switchimg(n) {
  slideIndex += n;
  showimg(slideIndex);
}

function showimg(n) {
  var i;
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none"; 
  }
  if (n > x.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = x.length} ;
  x[slideIndex-1].style.display = "block";
  setTimeout(rotate, 4000);
}

function rotate() {
  var i;
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none"; 
  }
  slideIndex++;
  showimg(slideIndex)
}