app.model.activity = Backbone.Model.extend({
  idAttribute: 'userId',
  
  urlRoot: '/api/activities'
});