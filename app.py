import os

from flask import Flask, jsonify, render_template
from flask_assets import Environment, Bundle
from livereload import Server

# App setup

app = Flask(__name__)

assets = Environment(app)

# https://github.com/lepture/python-livereload/issues/144
app.debug = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Tell flask-assets where to look for assets

assets.load_path = [
  os.path.join(os.path.dirname(__file__), 'static'),
]

# Preprocess scss and bundle CSS

css = Bundle(
  # Paths to CSS dependencies you don't want to run through scss go here
  Bundle(
    'styles/app.scss',
    filters = 'scss',
  ),
  output = 'css_all.css'
)

assets.register('css_all', css)

# Bundle JS

js = Bundle(
  'scripts/app.js',
  filters = 'jsmin',
  output = 'js_all.js'
)

assets.register('js_all', js)

# Pages

@app.route('/')
def index():
  return render_template('index.html')

# Endpoints

@app.route('/_get_data')
def getData():
  return # Query DB, third-party service, etc here

# Init

if __name__ == '__main__':

  server = Server(app.wsgi_app)
  server.watch('/templates/*')
  server.serve()
