app.router.route('activities/:id', function () {
  
  var activityHTML = $('#activity').html();
  
  $('.main-content').html(activityHTML);

});