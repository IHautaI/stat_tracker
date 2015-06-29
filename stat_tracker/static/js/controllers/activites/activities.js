app.router.route('activities', function () {
  
  var loginHTML = $('#activities').html();
  
  $('.main-content').html(loginHTML);
  
  console.log(loginHTML);
});