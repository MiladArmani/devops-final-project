# Network & Security

## Firewall rules (Arvan Cloud Security Group)
Applied to both VMs (master and worker):
- TCP 22 (SSH) — key-based auth only, no password
- TCP 80, 443 (HTTP/HTTPS) — Ingress traffic
- TCP 6443 (Kubernetes API)
- Full TCP/UDP traffic between the two VMs' own IPs — required for Calico
  pod-to-pod networking (VXLAN uses UDP port 4789)

## SSH access
- Key-based only (ed25519), no password authentication
- Non-root user `deploy` with passwordless sudo (`/etc/sudoers.d/deploy`)

## Notes
Arvan's firewall blocks unlisted traffic by default; Calico's default
IPIP encapsulation was silently dropped even with ports open, since it's
a different protocol, not a port — see `01_linux_infra/troubleshooting.md`.
