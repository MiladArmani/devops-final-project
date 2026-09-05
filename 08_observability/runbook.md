# Alert Runbook

## KubePodCrashLooping
**What it means:** A pod is crashing repeatedly (more than usual) and Kubernetes keeps restarting it.

**Investigation steps:**
1. `kubectl get pods -n <namespace>` — find the problem pod
2. `kubectl logs <pod-name> -n <namespace> --previous` — see the logs from before the crash
3. `kubectl describe pod <pod-name> -n <namespace>` — check Events and Last State (e.g. OOMKilled or a code error)

**Common fixes:**
- If `OOMKilled` → increase `resources.limits.memory` in values.yaml
- If a code/config error → fix the bug in the image, rebuild and push a new version
- If temporary (e.g. an upgrade in progress) → wait and keep monitoring

## KubeDeploymentReplicasMismatch
**What it means:** The number of pods actually running doesn't match the desired replica count in the Deployment.

**Investigation steps:**
1. `kubectl get deployment <name> -n <namespace>` — check READY vs DESIRED
2. `kubectl describe deployment <name> -n <namespace>` — find the reason (e.g. insufficient resources, ImagePullBackOff)
3. `kubectl get pods -n <namespace>` — find which pods didn't come up

**Common fixes:**
- Check cluster resources (`kubectl describe nodes`, the Allocated resources section)
- Check that the image/tag is correct
