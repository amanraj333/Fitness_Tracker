import subprocess

print("=== AI Agent for EKS Operations ===")

pods = subprocess.check_output(
    ["kubectl", "get", "pods", "-A"]
).decode()

print("\n--- Current Pod Status ---")
print(pods)

if "CrashLoopBackOff" in pods:
    print("Issue: CrashLoopBackOff detected")
    print("Recommendation:")
    print("kubectl describe pod <pod> -n <namespace>")
    print("kubectl logs <pod> -n <namespace>")
elif "Pending" in pods:
    print("Issue: Pending pod detected")
    print("Recommendation:")
    print("kubectl top nodes")
    print("kubectl describe pod <pod> -n <namespace>")
else:
    print("Cluster Healthy")
    print("Suggested Commands:")
    print("kubectl get pods -A")
    print("kubectl top pods -A")