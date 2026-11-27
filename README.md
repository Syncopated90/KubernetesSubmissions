How to run the project:
- Go into the todo_app directory and follow the readme there.

Setup monitoring: follow the readme in monitoring/.

Apply gateway.yaml in the root directory if gateways are used. You also need to setup the relevant databases, scripts for this are found in dbscript.txt in the todo and pingpong directories.

Google Kubernetes Engine:
Build the cluster with 

gcloud container clusters create dwk-cluster --zone=europe-north2-a --cluster-version=1.36 --disk-size=32 --num-nodes=2 --machine-type=e2-small

If necessary, move to the cluster with

gcloud container clusters get-credentials dwk-cluster --zone=europe-north2-a

When not in use, delete the cluster with

gcloud container clusters delete dwk-cluster --zone=europe-north2-a

To scale down the cluster when not in use, use

gcloud container clusters resize dwk-cluster --node-pool default-pool --num-nodes 0 --zone europe-north2-a

Activate the gateway API with

gcloud container clusters update dwk-cluster --location=europe-north2-a --gateway-api=standard



# Exercise submissions for Devops with Kubernetes on MOOC.fi, from Helsinki university
## Chapter 2
- [1.1] https://github.com/Syncopated90/KubernetesSubmissions/releases/tag/1_1
- [1.2] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.2
- [1.3] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.3
- [1.4] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.4
- [1.5] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.5
- [1.6] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.6
- [1.7] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.7
- [1.8] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.8
- [1.9] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.9
- [1.10] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.10
- [1.11] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.11
- [1.12] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.12
- [1.13] https://github.com/Syncopated90/KubernetesSubmissions/tree/1.13
## Chapter 3
- [2.1] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.1
- [2.2] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.2
- [2.3] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.3
- [2.4] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.4
- [2.5] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.5
- [2.6] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.6
- [2.7] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.7
- [2.8] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.8
- [2.9] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.9
- [2.10] https://github.com/Syncopated90/KubernetesSubmissions/tree/2.10
## Chapter 4
- [3.1] https://github.com/Syncopated90/KubernetesSubmissions/tree/3.1
- [3.2] https://github.com/Syncopated90/KubernetesSubmissions/tree/3.2
- [3.3] https://github.com/Syncopated90/KubernetesSubmissions/tree/3.3
- [3.4] https://github.com/Syncopated90/KubernetesSubmissions/tree/3.4