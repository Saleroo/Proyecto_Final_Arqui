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
2) crear chart(parado en la carpeta del proyecto): helm create buildachart
3) crear las imagenes de los dockers (pararse en la carpeta donde esten los docker files de cada uno): docker build . -t app1 y docker build . -t app2
4) crear la imagen de postgrest: 
5) instalar las imagenes con helm para subir a kubernetes: helm install app1 buildachart --values buildachart/values.yaml
