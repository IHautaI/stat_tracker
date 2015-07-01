app.router.route('activities', function () {
  
  var activitiesHTML = $('#activities').html();
  
  $('.main-content').html(activitiesHTML);
  
  $.ajax({
    url: '/api/activities/',
    method: 'GET',
    contentType: 'application/json',
  }).done(function (data) {
    console.log(data);
    data.map(function (item) {
      $('.list-activities').append('<a href="#/activities/' + item.id + '"><li>' + item.title + ' : ' + item.description + '</li></a>');
    });
  }).fail(function () {
    console.log(arguments);
  });
  
  $('.activity-form').on('click', 'button', function (e) {
    e.preventDefault();
    console.log('click');
    
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken'); 
    
    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    
    var activity = {
      title: $('input[name="activity"]').val(),
      description: $('textarea[name="description"]').val()
    };
    
    $.ajax({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      },
      url: '/api/activities/',
      method: 'POST',
      data: JSON.stringify(activity),
      contentType: 'application/json; charset=utf-8'
    }).done(function () {
      $.ajax({
        url: '/api/activities/',
        method: 'GET',
        contentType: 'application/json',
      }).done(function (data) {
        $('.list-activities *').remove();
        data.map(function (item) {
          $('.list-activities').append('<a href="#/activities/' + item.id + '"><li>' + item.title + ' : ' + item.description + '</li></a>');
        });
      }).fail(function () {
        console.log(arguments);
      });
    }).fail(function () {
      console.log(arguments);
    });
    
    $('input[name="activity"]').val(''),
    $('textarea[name="description"]').val('')
  });
});