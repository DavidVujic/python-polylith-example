# Example usage

## Build the project
Navigate to this folder (where the `pyproject.toml` file is)

Run:
``` shell
poetry build-project
```

## Build a docker image

``` shell
docker build -t myimage .
```

## Run the image

``` shell
docker run -d --name mycontainer -p 8000:8000 myimage
```

The OpenAPI specification of this FastAPI app can now be accessed at http://localhost:8000/docs#

