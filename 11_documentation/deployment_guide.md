# Deployment Guide

## 1. Provision VMs
Create 2 Ubuntu 22.04 VMs on Arvan Cloud (2+ vCPU, 4GB+ RAM — worker
should have 8GB if running the full monitoring stack). Open firewall
ports 22, 80, 443, 6443, and full traffic between the two VMs' IPs.
Details: `01_linux_infra/server_info.md`

## 2. Provision nodes with Ansible

cd 06_ansible
ansible-playbook -i inventory.ini site.ym

This installs containerd, kubeadm/kubelet/kubectl, and prepares the OS
(swap off, kernel modules, sysctl) on both nodes.

## 3. Initialize the cluster
On the master:

sudo kubeadm init --pod-network-cidr=192.168.0.0/16
--image-repository registry.aliyuncs.com/google_containers
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/calico.yaml
kubectl patch ippool default-ipv4-ippool --type=merge -p '{"spec": {"ipipMode": "Never", "vxlanMode": "Always"}}'

On the worker, run the `kubeadm join` command printed above.
Copy `/etc/kubernetes/admin.conf` to `~/.kube/config` on your workstation.

## 4. Build and push the app image

cd 04_application
docker build -t myapp:v1 .
docker tag myapp:v1 ghcr.io/miladarmani/myapp:v1
docker push ghcr.io/miladarmani/myapp:v1

## 5. Install Ingress

helm install ingress-nginx ingress-nginx/ingress-nginx
--namespace ingress-nginx --create-namespace
--set controller.image.registry=registry.cn-hangzhou.aliyuncs.com
--set controller.image.image=google_containers/nginx-ingress-controller
--set controller.image.digest=""
--set controller.admissionWebhooks.patch.image.registry=registry.cn-hangzhou.aliyuncs.com
--set controller.admissionWebhooks.patch.image.image=google_containers/kube-webhook-certgen
--set controller.admissionWebhooks.patch.image.digest=""
kubectl patch svc ingress-nginx-controller -n ingress-nginx -p '{"spec": {"type": "NodePort"}}'


## 6. Deploy the app

kubectl create namespace myapp
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout myapp-tls.key -out myapp-tls.crt -subj "/CN=myapp/O=myapp"
kubectl create secret tls myapp-tls --cert=myapp-tls.crt --key=myapp-tls.key -n myapp
helm install myapp 09_kubernetes/myapp-chart -n myapp


## 7. Install monitoring

helm install monitoring prometheus-community/kube-prometheus-stack
-n monitoring --create-namespace -f 08_observability/monitoring-values.yaml


## 8. Verify

curl -k https://<VM-public-IP>:<NodePort>/health

Should return `{"status":"ok"}`.
