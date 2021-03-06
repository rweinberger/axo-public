var x = window.location.pathname;
var title;

switch(x) {
  case '/':
    title = '#home'
    break;
  case '/sisterhood/':
  case '/philanthropy/':
    title = '#chapter-life'
    break;
  case '/blm/':
    title = '#philanthropy'
    break;
  case '/recruitment/':
  case '/faq/':
    title = '#recruitment'
    break;
  case '/sisters/':
  case '/involvement/':
    title = '#sisters'
    break;
  default:
    title = '#about'
    break;
};

$(title).css('color', '#000');
$(title).css('border-bottom', 'solid 1px #ccc');
