app.router.route('', function () {
  
  var loginHTML = $('#login').html();
  
  $('.main-content').html(loginHTML);
  
  console.log(loginHTML);
});