## Installation

```sh
# First, install the global requirements if they're not already installed on the machine
pip install virtualenv
sudo gem install sass

git clone git@github.com:sir-dunxalot/flask-boilerplate.git <project-name> # Clone repo
cd <project-name>

virtualenv <project-name> --no-site-packages # Create the virtualenv without requiring all locally-installed packages

source <project-name>/bin/activate # Start the virtual env
pip install -r requirements.txt # Install backend dependencies
npm install # Install frontend dependencies

git remote set-url origin git@github.com:<your-username>/<project-name>.git # If you want to use Github
```

Comes with the following packages installed:

- flask
- flask_assets
- jsmin
- livereload

## Running the server

```sh
# Start the virtualenv if you haven't already
source jebbit-product-health-env/bin/activate

# Run the server
python app.py # Visit http://127.0.0.1:5500/

# Remember: when you want to stop working in the virtualenv, run the following
deactivate
```

## Installing new dependencies

```sh
# Install a package like normal
pip install packagename

# Update the requirements doc
pip freeze > requirements.txt
```
