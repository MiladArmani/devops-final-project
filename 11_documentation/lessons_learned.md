# Lessons Learned

## What was hard
- Several container registries (registry.k8s.io, quay.io, Docker Hub) are
  unreliable or blocked from Iran. This affected almost every phase:
  kubeadm init, Ingress installation, and the full monitoring stack all
  needed workarounds (accessible mirrors, or mirroring images ourselves
  to GHCR via GitHub Actions).
- Calico's default IPIP mode was silently blocked by Arvan's firewall even
  with "allow all" rules — it took a while to realize the protocol itself
  (not the ports) was the issue. Switching to VXLAN fixed it.
- Running the full observability stack (Prometheus, Grafana, Alertmanager)
  alongside the app and Ingress overloaded a 4GB worker VM, causing
  cascading OOMKilled crashes across unrelated pods. Diagnosing this
  required checking `dmesg` on the node itself, not just `kubectl describe`.

## What I learned
- How to bootstrap a Kubernetes cluster with kubeadm from scratch
- How Helm chart values map to real Kubernetes resources (images, probes,
  resources, Ingress)
- How to write and test idempotent Ansible playbooks
- How to debug pod failures methodically: events → logs → node-level checks
- Practical tricks for working around regional network restrictions
  (registry mirrors, using CI runners as a bridge)
