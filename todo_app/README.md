Create cluster with k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
Create the directory on the container with docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube
Deploy with kubectl apply -f ../persistent_volume/ and then manifests/
Responds with a new picture every 10 minutes on localhost:8081
