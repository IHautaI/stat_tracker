app.collection.activity = Backbone.Collection.extend({
  model: Activity,
  
  url: '/api/activities'
});