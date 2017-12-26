## Installation

```sh
# First, install the global requirements if they're not already installed on the machine
pip install virtualenv
sudo gem install sass

git clone git@github.com:sir-dunxalot/flask-boilerplate.git <project-name> # Clone repo
cd <project-name>

virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt # Create the virtualenv and install dependencies

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

source .env/bin/activate # Start the virtual env

export FLASK_DEBUG=1 && export FLASK_APP=app.py

flask run
```

If you want to stop working in the virtualenv, run the following:

```sh
deactivate
```

## Installing new dependencies

```sh
# Install a package like normal
pip install packagename

# Update the requirements doc
pip freeze > requirements.txt
```
