# DevOps Final Project — Kubernetes on Arvan Cloud

A simple Flask API deployed on a self-managed Kubernetes cluster
(kubeadm) running on Arvan Cloud VMs, with Helm, Ingress+TLS, Ansible,
CI/CD, and full observability (Prometheus/Grafana/Alertmanager).

## Quick start
See `11_documentation/deployment_guide.md` for full step-by-step
instructions. Summary:

1. Provision 2 Arvan Cloud VMs → `01_linux_infra/`
2. Provision nodes: `cd 06_ansible && ansible-playbook -i inventory.ini site.yml`
3. Bootstrap cluster: `kubeadm init` + Calico (see deployment_guide.md)
4. Build & push app image: `cd 04_application && docker build ...`
5. Install Ingress: `helm install ingress-nginx ...`
6. Deploy app: `helm install myapp 09_kubernetes/myapp-chart -n myapp`
7. Install monitoring: `helm install monitoring prometheus-community/kube-prometheus-stack ...`
8. Verify: `curl -k https://<VM-IP>:<NodePort>/health`

## Project structure
- `01_linux_infra/` — VM setup, firewall, troubleshooting notes
- `04_application/` — Flask app source, Dockerfile, image build notes
- `06_ansible/` — node provisioning automation
- `08_observability/` — Prometheus/Grafana values, runbook
- `09_kubernetes/` — Helm chart, cluster setup notes
- `10_cicd_gitops/` — CI/CD pipeline docs
- `11_documentation/` — architecture, deployment guide, lessons learned

## Notes
- Several upstream registries are unreliable from Iran; see
  `01_linux_infra/troubleshooting.md` for the mirrors/workarounds used.
