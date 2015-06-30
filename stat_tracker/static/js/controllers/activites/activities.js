app.router.route('activities', function () {
  
  var activitiesHTML = $('#activities').html();
  
  $('.main-content').html(activitiesHTML);
  
  $.ajax({
    url: '/api/activities/',
    method: 'GET',
    contentType: 'application/json',
  }).done(function (data) {
    $('.list-activites').text(data[0].title);
  }).fail(function () {
    console.log(arguments);
  });
  
  $('.main-content').on('click', '.activity-form button', function (e) {
    e.preventDefault();
    
    var activity = {
      title: $('input[name="activity"]').val(),
      description: $('textarea[name="description"]').val()
    };
    
    $.ajax({
      url: '/api/activities/',
      method: 'POST',
      data: JSON.stringify(activity),
      contentType: 'application/json; charset=utf-8'
    }).done(function (data) {
      console.log('success!');
    }).fail(function () {
      console.log(arguments);
    });
  });
});