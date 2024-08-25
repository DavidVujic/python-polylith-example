# Example usage

## Build the project
Navigate to this folder (where the `pyproject.toml` file is)

Run:
``` shell
poetry build-project
```

## Run the app locally
Build a docker image and run a container, and access the app from localhost.

### Build a docker image

``` shell
docker build -t my-fastapi-project-image .
```

### Run the image

``` shell
docker run -d --name mycontainer -p 8000:8000 my-fastapi-project-image
```

The OpenAPI specification of this FastAPI app can now be accessed at http://localhost:8000/docs#


## Deploy in Kubernetes

### Development
Build and deploy into a local Kubernetes cluster.


## Build a docker image in a minikube context

``` shell
eval $(minikube docker-env)

docker build -t my-fastapi-project-image .
```


#### Dry run, to verify the result
``` shell
kubectl apply -k kubernetes/development --dry-run=client -o yaml
```

#### Deploy

``` shell
kubectl apply -k kubernetes/development
```

#### Verify deployment

``` shell
kubectl get pods
```

``` shell
kubectl get services
```

Try out the API by port forwarding to localhost:

``` shell
kubectl port-forward svc/my-fastapi-project-api-app 9090:80
```
