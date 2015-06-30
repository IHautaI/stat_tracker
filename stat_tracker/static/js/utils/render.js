app.render = {
  stats: function (dates, values) {
    var chart = c3.generate({
      bindto: '.visual',
      data: {
        x: 'dates',
        xFormat: '%Y-%m-%d',
        columns: [
          dates,
          values
        ]
      },
      axis: {
        y: {
          label: {
            text: 'Stats',
            position: 'outer-middle'
          }
        },
        x: {
          type: 'timeseries',
          label: {
            text: 'Time',
            position: 'outer-middle'
          },
          tick: {
            fit: false,
            format: function (d) {
              return d.toLocaleDateString();
            }
          }
        }
      }
    });
  }
}