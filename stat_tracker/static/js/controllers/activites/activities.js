app.router.route('activities', function () {
  
  var loginHTML = $('#activities').html();
  
  $('.main-content').html(loginHTML);
  
  $('.main-content').on('click', '.activity-form button', function (e) {
    e.preventDefault();
    
    
    var data = {
      title: $('input[name="activity"]').val(),
      description: $('textarea[name="description"]').val()
    };
    
    console.log(data);
  });
});