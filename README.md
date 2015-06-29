# Welcome to your new Django single-page app project!

This template will ease your way in building a single-page app backed by a Django API.

To use this template, run:

```
django-admin.py startproject YOUR_PROJECT_NAME --template=https://github.com/tiyd-python-2015-05/single-page-app-template/archive/master.zip --extension=py,md --name=Procfile
```

Change YOUR_PROJECT_NAME before running the above.

## Files you should know about

* `stat_tracker/templates/index.html` - This is where all your HTML should go. It has a few funny things in there. Make sure to use `\{% static "path/to/file.css" %\}` for all links to static files.

* `stat_tracker/static/` - All your static files go here. You can write them by hand or generate them with gulp or another tool.

## Heroku instructions

This app should work well with Heroku as long as you run the following commands:

```
heroku config:set DJANGO_SETTINGS_MODULE=stat_tracker.heroku_settings
heroku config:set PYTHONPATH=stat_tracker
heroku config:set SECRET_KEY=$(date | md5 | base64)
```
