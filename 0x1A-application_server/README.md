# 0x1A. Application server

This is a repository containing assignments for Holberton School.

|FILES| DESCRIPTIONS|
|---|---|
|README.md|  Let’s serve what you built for ```AirBnB clone v2 - Web framework``` on ```web-01```. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.|
|2-app_server-nginx_config|  Now that you have your development environment set up, let’s get your production application server set up with ```Gunicorn``` on ```web-01```, port ```5000```. You’ll need to install ```Gunicorn``` and any libraries required by your application. Your ```Flask``` application object will serve as a ```WSGI``` entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.|
|3-app_server-nginx_config|  Building on your work in the previous tasks, configure ```Nginx``` to serve your page from the route ```/airbnb-onepage/```|
|4-app_server-nginx_config|  Building on what you did in the previous tasks, let’s expand our web application by adding another service for ```Gunicorn``` to handle. In ```AirBnB_clone_v2/web_flask/6-number_odd_or_even```, the route ```/number_odd_or_even/&lt;int:n&gt;``` should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure ```Nginx``` to proxy HTTP requests to the route ```/airbnb-dynamic/number_odd_or_even/(any integer)``` to a ```Gunicorn``` instance listening on port ```5001```. The key to this exercise is getting ```Nginx``` configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of ```Gunicorn``` without having multiple terminals open, see tips below.|
|5-app_server-nginx_config|  Let’s serve what you built for ```AirBnB clone v3 - RESTful API``` on ```web-01```.|

