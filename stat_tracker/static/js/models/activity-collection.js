app.collection = Backbone.Collection.extend({
  model: app.model,
  
  url: '/api/activities'
});