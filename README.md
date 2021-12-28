# Proyecto_Final_Arqui


### ----Eliminar charts ----
`helm uninstall 'nombre_del_chart'`

### ----para conectarse a la base de datos desde fuera del cluester ejecutar los comandos: ----

    kubectl port-forward --namespace default svc/my-release-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432

## Instalar las apps con helm
0) usar minikube: `eval $(minikube docker-env)`
1) decargar helm:
     `curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3`
     `chmod 700 get_helm.sh`
     `./get_helm.sh`
2) crear chart(parado en la carpeta del proyecto): `helm create nombre_del_chart`
3) crear las imagenes de los dockers (pararse en la carpeta donde esten los docker files de cada uno): `docker build . -t app1` y `docker build . -t app2`
4) instalar las imagen del app2 con helm para subir a kubernetes: `helm install app2 buildachart2 --values buildachart2/values.yaml`
5) `export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=buildachart2,app.kubernetes.io/instance=app2" -o jsonpath="{.items[0].metadata.name}")`
6) `export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")`
7) `kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT`
8) instalar las imagen del app1 con helm para subir a kubernetes: `helm install app1 buildachart --values buildachart/values.yaml`
9) `export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=buildachart,app.kubernetes.io/instance=app1" -o jsonpath="{.items[0].metadata.name}")`
10) `export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")`
11) `kubectl --namespace default port-forward $POD_NAME 4444:$CONTAINER_PORT`
11) instalar postgrest con heml: 
      `helm repo add bitnami https://charts.bitnami.com/bitnami`
      `helm install my-release bitnami/postgresql`
      
## Crear cronjob
0) usar minikube: `eval $(minikube docker-env)`
1) `helm install nombre_del_cronjob .` ( debes estar dentro de la carpeta del chart creado del cronjob)
2) `helm uninstall nombre_del_cronjob` ( desinstalar el cronjob una ves ya termino su trabajo) (recomendado)
### mirar el log de un pod cronjob
`kubectl logs -f nombre_del_pod`
## Crear observabilidad 
0) Se debe crear el APM server ubicado en la pagina web de elasticsearch, para ello se debe tener una cuenta en ella (recomendado registrarse con cuenta de google) https://www.elastic.co/
1) Buscar APM y darle a "Add data" y si es la primera vez crear un APM siguiendo los pasos de la pagina
