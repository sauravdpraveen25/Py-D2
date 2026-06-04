# pip install flask

# Web Application Framework or simply Web Framework
# which represents a collection of libraries and modules that
# enables a web application developer to write applications without having to bother about low-level details such as
# protocols, thread management etc.

# Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine.
# Both are Pocco projects.


# WSGI
# Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development.
# WSGI is a specification for a universal interface between the web server and the web applications.


# Werkzeug

# It is a WSGI toolkit, which implements requests, response objects, and other utility functions.
# This enables building a web framework on top of it.
#  The Flask framework uses Werkzeug as one of its bases


# jinja2
# jinja2 is a popular templating engine for Python.
# A web templating system combines a template with a certain data source to render dynamic web pages.

from flask import Flask

app = Flask(__name__)

print(__name__)


# The route() function of the Flask class is a decorator, which tells the application which URL should call the
# associated function

# app.route(rule, options)
# The rule parameter represents URL binding with the function.
# The options is a list of parameters to be forwarded to the underlying Rule object.


@app.route('/')
def hello_world():
    return "Hello World"


# if __name__ == '__main__':

# the run() method of Flask class runs the application on the local development server called
# app.run(host, port, debug, options)

# while the application is under development, it should be restarted manually for each change in the code. To
# avoid this inconvenience, enable debug support. The server will then reload itself if the code changes.

# app.run(host, port, debug, options)

# host
# Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally

# port

# Defaults to 5000

# debug
# Defaults to false. If set to true, provides a debug information

# options
# To be forwarded to underlying Werkzeug server.

app.run(debug=True)
