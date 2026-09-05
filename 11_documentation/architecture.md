# Architecture

## Infrastructure
- 2 Arvan Cloud VMs (Ubuntu 22.04), 4→8GB RAM each:
  - `milad-master`: Kubernetes control-plane
  - `milad-worker`: Kubernetes worker node
- Networking: Calico (VXLAN mode) for pod-to-pod traffic across nodes
- Firewall: SSH (22), HTTP/HTTPS (80/443), Kubernetes API (6443), and
  full traffic between the two VMs' IPs (required for Calico/cluster networking)

## Application
- Flask app (`04_application/`), exposing `/health` and a simple `/tasks` CRUD API
- Containerized, image hosted on GitHub Container Registry (ghcr.io)
- Deployed via a Helm chart (`09_kubernetes/myapp-chart/`)

## Traffic flow
Internet → VM public IP (NodePort) → ingress-nginx (TLS termination,
self-signed cert) → Service → App Pod

## Observability
kube-prometheus-stack (Prometheus + Grafana + Alertmanager) deployed in
the `monitoring` namespace, scraping cluster and app metrics. Two alerting
rules (KubePodCrashLooping, KubePodNotReady) tested against a deliberately
broken deployment.

## CI/CD
GitHub Actions builds, tests, and pushes the app image to GHCR on every
push to `main`. Deployment to the cluster is a manual `helm upgrade`.

## Notable constraint
Several registries (registry.k8s.io, quay.io, Docker Hub) are unreliable
from Iran. Where an accessible mirror existed, images were pulled from
there; otherwise images were mirrored to our own GHCR registry via a
GitHub Actions workflow. See `01_linux_infra/troubleshooting.md` for details.
