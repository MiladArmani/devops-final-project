#!/bin/bash

# ---- Config: adjust these to your environment ----
MASTER_IP="95.38.185.190"
WORKER_IP="37.32.36.78"
HTTPS_NODEPORT="30886"   # the port we found earlier via kubectl get svc
APP_NAMESPACE="myapp"
# ---------------------------------------------------

echo "=== Node status ==="
kubectl get nodes

echo ""
echo "=== Pod status (all namespaces) ==="
kubectl get pods -A

echo ""
echo "=== App health check (via Ingress, HTTPS) ==="
response=$(curl -sk -o /dev/null -w "%{http_code}" "https://${MASTER_IP}:${HTTPS_NODEPORT}/health")
if [ "$response" == "200" ]; then
    echo "OK: /health returned HTTP $response"
else
    echo "FAILED: /health returned HTTP $response"
fi

echo ""
echo "=== Checking for non-Running pods ==="
not_running=$(kubectl get pods -A --no-headers | grep -v "Running\|Completed")
if [ -z "$not_running" ]; then
    echo "OK: all pods are Running"
else
    echo "WARNING: some pods are not healthy:"
    echo "$not_running"
fi
