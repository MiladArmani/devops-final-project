# Troubleshooting Log

## registry.k8s.io / quay.io / Docker Hub blocked from Iran
Multiple image pulls (kubeadm images, ingress-nginx, kube-prometheus-stack)
failed or timed out. Fixed per-case using accessible mirrors
(registry.aliyuncs.com/google_containers, docker.arvancloud.ir) or, when no
mirror existed, by mirroring the images to our own GHCR registry via a
GitHub Actions workflow (GitHub's runners have unrestricted internet access).

## Calico IPIP blocked between nodes
Pod-to-pod traffic across nodes timed out even with the firewall opened for
all ports, because Calico defaulted to the IPIP protocol. Switched Calico to
VXLAN mode (UDP, port 4789), which resolved it.

## Worker VM running out of memory
Running Ingress + the app + the full kube-prometheus-stack together caused
repeated OOMKilled events on the 4GB worker VM, destabilizing the node
itself. Fixed by resizing the worker to 8GB RAM, setting explicit memory
limits on each component, and pinning Prometheus/Alertmanager to the
master node.
