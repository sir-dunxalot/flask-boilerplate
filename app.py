import os

from flask import Flask, g, jsonify, render_template, request
from flask_assets import Environment, Bundle

# App setup

app = Flask(__name__)

assets = Environment(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True # https://github.com/lepture/python-livereload/issues/144

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
    depends = ('**/*.scss', '**/**/*.scss'),
  ),
  output = 'css-dist.css'
)

assets.register('css-dist', css)

# Bundle JS

js = Bundle(
  'scripts/app.js',
  filters = 'jsmin',
  output = 'js-dist.js'
)

assets.register('js-dist', js)

# Pages

@app.route('/')
def index():
  return render_template('index.html')

# Note, error handler's don't trigger when flask's debug mode is enabled

@app.errorhandler(500)
def internal_server_error(error):
  return render_template('500.html')

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 80)
