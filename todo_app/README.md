Create cluster with k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
Deploy with kubectl apply -f manifests/
Responds with current hash on localhost:8081
