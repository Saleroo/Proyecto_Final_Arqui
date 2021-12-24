# Proyecto_Final_Arqui


# Subir apps a kubernetes
0) usar minikube(?): eval $(minikube docker-env)
1) crear la imagen de la app
2) confirurar el achivo .yaml
3) hacer el comando: kubectl apply -f k8s.yaml
4) luego se puede verificar los pods en kubernetes con: kubectl get pods
# Instalar las apps con helm
1) decargar helm:
  curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
  chmod 700 get_helm.sh
  ./get_helm.sh
