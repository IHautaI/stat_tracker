app.router.route('activities/:id', function (id) {

  var activityHTML = $('#activity').html();
  
  $('.main-content').html(activityHTML);
  
  $.ajax({
    url: '/api/activities/' + parseInt(id) + '/',
    method: 'GET',
    contentType: 'application/json'
  }).done(function (data) {
    var dates = [];
    var counts = []; 
    
    $('.activity-title').text(data.title);
    data.stats.map(function (stats) {
      dates.push(stats.date);
      counts.push(stats.count);
    })
    dates.unshift('dates');
    counts.unshift('stats');
    
    app.render.stats(dates, counts);
  }).fail(function (data) {
    console.log(arguments);
  });
  
  $('.activity-form').on('submit', function (e) {
    e.preventDefault();
    
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
  
    var activityData = {
      date: $('input[name="date"]').val(),
      count: $('input[name="count"]').val()
    }
    
    $.ajax({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      },
      url: '/api/activities/' + parseInt(id) + '/stats/',
      method: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(activityData)
    }).done(function (data) {
      console.log(data);
    }).fail(function () {
      console.log(arguments);
    });
    
    $('input[name="date"]').val('');
    $('input[name="count"]').val('');
    
    $.ajax({
      url: '/api/activities/' + parseInt(id) + '/',
      method: 'GET',
      contentType: 'application/json'
    }).done(function (data) {
      var dates = [];
      var counts = [];
      
      $('.activity-title').text(data.title);
      data.stats.map(function (stats) {
        dates.push(stats.date);
        counts.push(stats.count);
      })
      dates.unshift('dates');
      counts.unshift('stats');
      
      $('.visual *').remove();
      
      app.render.stats(dates, counts);
    }).fail(function (data) {
      console.log(arguments);
    });
    
    
    
  });

});