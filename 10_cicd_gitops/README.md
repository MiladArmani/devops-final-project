# CI/CD Pipeline

## How the image is built
On every push to `main` that touches `04_application/**`, a GitHub Actions
workflow (`.github/workflows/ci.yml`) automatically:
1. Checks out the code
2. Builds the Docker image from `04_application/`
3. Runs a smoke test (starts the container, checks `/health`)
4. Pushes the image to GitHub Container Registry (ghcr.io), tagged with
   both the commit SHA and `latest`

## How it reaches the cluster
Deployment to Kubernetes is manual for this project: after CI pushes a new
image, `helm upgrade myapp <chart-path> -n myapp` is run to roll it out.
Automatic deployment (GitOps) was out of scope but could be added with a
tool like ArgoCD or Flux watching the Helm chart / image tag.
