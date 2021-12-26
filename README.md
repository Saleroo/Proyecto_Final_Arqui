# Proyecto_Final_Arqui

# -----Eliminar pods -------
kubectl get deployments --all-namespaces 
kubectl delete -n NAMESPACE deployment DEPLOYMENT

# ----Eliminar charts ------
helm uninstall 'nombre_del_chart'

# Subir apps a kubernetes
0) usar minikube(?): eval $(minikube docker-env)
1) crear la imagen de la app
2) confirurar el achivo .yaml
3) hacer el comando: kubectl apply -f k8s.yaml
4) luego se puede verificar los pods en kubernetes con: kubectl get pods
# Instalar las apps con helm
0) usar minikube(?): eval $(minikube docker-env)
1) decargar helm:
  curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
  chmod 700 get_helm.sh
  ./get_helm.sh
2) crear chart(parado en la carpeta del proyecto): helm create buildachart
3) crear las imagenes de los dockers (pararse en la carpeta donde esten los docker files de cada uno): docker build . -t app1 y docker build . -t app2
4) instalar las imagen del app2 con helm para subir a kubernetes: helm install app2 buildachart2 --values buildachart2/values.yaml
5) export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=buildachart2,app.kubernetes.io/instance=app2" -o jsonpath="{.items[0].metadata.name}")
6) export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
7) kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
8) instalar las imagen del app1 con helm para subir a kubernetes: helm install app1 buildachart --values buildachart/values.yaml
9) crear la imagen de postgrest: 
