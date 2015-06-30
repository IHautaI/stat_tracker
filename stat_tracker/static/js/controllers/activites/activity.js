app.router.route('activities/:id', function (id) {
  
  var activityHTML = $('#activity').html();
  
  $('.main-content').html(activityHTML);
  
  $.ajax({
    url: '/api/activities/' + parseInt(id) + '/',
    method: 'GET',
    contentType: 'application/json'
  }).done(function (data) {
    console.log(data);
  }).fail(function (data) {
    console.log(arguments);
  });

});