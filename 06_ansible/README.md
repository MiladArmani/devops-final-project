# Ansible

## Run



## Roles
- `common`: updates packages, configures the deploy user, installs general-purpose tools
- `k8s_node`: prepares a node for Kubernetes (swap, kernel modules, containerd, installs kubeadm/kubelet/kubectl)

## Idempotency
On the second run of the playbook, only 1 task showed `changed` (an intentional restart of the containerd service) — everything else was unchanged.
