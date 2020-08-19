#!/usr/bin/env bash
kubectl apply -f deployment/deployment.yaml
kubectl get pods -n ml
kubectl apply -f deployment/service.yaml