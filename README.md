## Intro

This repo is intended to make it easy to get started with a Flask project. If you want to use it for your own projects, I suggest cloning this repo locally rather than following the installation instructions below:

```
git clone https://github.com/sir-dunxalot/flask-boilerplate.git <project-name>
```

## Installation

Create a new docker container, using flask-boilerplate as the base:

```sh
FROM sirdunxalot/flask-boilerplate

COPY ./app /app
```

## Running the server in development

```sh
docker build -t <image-name> .

# Without Flask debugging server

docker run -d --name <image-name> -p 80:80 -v $(pwd)/app:/app -e FLASK_APP=main.py -e FLASK_DEBUG=1 <image-name> flask run --host=0.0.0.0 --port=80

# OR with Flask debugging server

docker run -d --name <image-name> -p 80:80 -v $(pwd)/app:/app -e FLASK_APP=main.py -e FLASK_DEBUG=1 <image-name> bash -c "while true ; do sleep 10 ; done"

docker exec -it <image-name> bash

flask run --host=0.0.0.0 --port=80 # Run command to start and subsequently restart server

```

Once you've created a container, if it's not running you can start it:

```sh
docker start <image-name>
```

You can see what containers are running:

```sh
docker container ls
```

You can stop any active container:

```sh
docker stop <image-name>
```

## Installing new dependencies

1. Add package name to `requirements.txt`
2. Run `docker build -t <image-name> .`
