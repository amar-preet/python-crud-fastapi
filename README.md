```
./bootstrap.sh
```

This will create a directory a [virtualenv](https://virtualenv.pypa.io/en/latest/) `env` directory.

## Running local

Use the `env` directory above:

```
source env/bin/activate
```

To start the application:

```
uvicorn app.main:app --reload
```

## Running in Docker

To run the application in docker, first build then run:

```
docker build -t <tag-name> .
docker run -d --name mycontainer -p 80:80 <tag-name>
```