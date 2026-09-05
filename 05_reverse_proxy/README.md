# Reverse Proxy (Ingress + TLS)

## Ingress Controller
- ingress-nginx, installed via Helm into the `ingress-nginx` namespace
- Images pulled from registry.cn-hangzhou.aliyuncs.com/google_containers
  (registry.k8s.io is unreliable from Iran)
- Exposed as a NodePort service (no cloud LoadBalancer available on Arvan)

## TLS
- Self-signed certificate (no domain name used, VM public IP only)
  generated with openssl and stored as a Kubernetes TLS secret (`myapp-tls`)
  in the `myapp` namespace
- The app's Ingress resource references this secret and `className: nginx`

## Access

curl -k https://<VM-public-IP>:<NodePort>/health

`-k` is required since the certificate is self-signed and not trusted by
default.
