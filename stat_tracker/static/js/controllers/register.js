app.router.route('register', function () {
  
  var activitiesHTML = $('#new-user').html();
  
  $('.main-content').html(activitiesHTML);
  
  $('.new-user').on('click', 'button', function (e) {
    e.preventDefault();
    
    var userInfo = {
      username: $('#id_username').val(),
      password: $('#id_password').val(),
      email:$('#id_email').val()
    };
    
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
    
    $.ajax({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      },
      url: 'register/',
      method: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(userInfo)
    }).done(function () {
      console.log('success');
    }).fail(function () {
      console.log(arguments);
    });
    
    $('input').val('');
    
  });
  
});