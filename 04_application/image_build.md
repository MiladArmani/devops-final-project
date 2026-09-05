# Image Build

## Build
docker build -t myapp:v1 .

## Tag for GHCR
docker tag myapp:v1 ghcr.io/miladarmani/myapp:v1

## Push
docker push ghcr.io/miladarmani/myapp:v1

Note: base image pulled via docker.arvancloud.ir mirror (Docker Hub is
unreliable from Iran). CI pipeline (see 10_cicd_gitops/) builds and pushes
automatically on every push to main.
