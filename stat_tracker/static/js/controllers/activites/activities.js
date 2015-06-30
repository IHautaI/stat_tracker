app.router.route('activities', function () {
  
  var activitiesHTML = $('#activities').html();
  
  $('.main-content').html(activitiesHTML);
  
  $('.main-content').on('click', '.activity-form button', function (e) {
    e.preventDefault();
    
    
    var activity = {
      title: $('input[name="activity"]').val(),
      description: $('textarea[name="description"]').val()
    };
    
    console.log(activity);
    
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