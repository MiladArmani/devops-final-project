# Kubernetes Cluster Setup

- Installed with kubeadm (v1.30) on 2 Ubuntu VMs: 1 control-plane (milad-master), 1 worker (milad-worker)
- Pod network CIDR: 192.168.0.0/16, CNI: Calico (VXLAN mode — IPIP was blocked by Arvan's firewall)
- registry.k8s.io images pulled via registry.aliyuncs.com/google_containers mirror (blocked from Iran otherwise)
- `kubectl get nodes` confirms both nodes Ready
- Namespace `myapp` created for the application
