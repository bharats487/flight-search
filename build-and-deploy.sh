#!/bin/bash
set -e

echo "====== Building Flight Search Docker Image ======"
docker build -t flight-search:latest .

echo "====== Verifying Kubernetes Context ======"
kubectl config current-context

echo "====== Installing/Upgrading Flight Search Helm Chart ======"
helm upgrade --install flight-search ./helm/flight-search

echo "====== Waiting for Deployment to be Ready ======"
kubectl rollout status deployment/flight-search-flight-search

echo "====== Deployment Summary ======"
kubectl get pods,svc,ingress -l app.kubernetes.io/instance=flight-search

echo ""
echo "====== Access Information ======"
echo "To access the app, add 'flight-search.local' to your /etc/hosts file pointing to your cluster IP"
echo "Then open http://flight-search.local in your browser"
echo ""
echo "Or forward the port with:"
echo "kubectl port-forward svc/flight-search-flight-search 8080:80"
echo "And access the app at http://localhost:8080"
