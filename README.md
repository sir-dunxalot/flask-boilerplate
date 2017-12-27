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

You can see what containers are running:

```sh
docker container ls
```

You can stop any active container:

```sh
docker container stop <container-id>
```

## Installing new dependencies

1. Add package name to `requirements.txt`
2. Run docker builder command (see running server instructions)
