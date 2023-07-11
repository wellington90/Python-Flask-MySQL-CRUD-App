#!/bin/bash

# Definir variáveis
DOCKER_IMAGE_NAME="w3ll1n9t0n"
DOCKER_IMAGE_TAG="crud_app"

# Construir a imagem Docker
docker build -t "$DOCKER_IMAGE_NAME/$DOCKER_IMAGE_TAG" .

# Enviar a imagem para o registro de container
docker push "$DOCKER_IMAGE_NAME/$DOCKER_IMAGE_TAG"

kubectl apply -f k8s/deployment.yaml  # Aplica o arquivo de configuração do Kubernetes (deployment.yaml)

kubectl delete pods -l app=app  # Deleta os pods com o rótulo "app=my-app"

watch -n 1 kubectl get pods  # Observa os pods atualizados a cada 1 segundo