# AI Weed Recognition - Kubernetes Deployment

<p align="center">
  <img src="https://github.com/Radebr/python-deep-learning-k8s/blob/main/preview.png?raw=true" alt="Project Screenshot"/>
</p>



This project is a web application that utilizes AI to recognize four common weed species found in agricultural fields in our region of El Oued - Guemar.  
The web also includes a rich library with detailed information about these weed species.  
The entire project is containerized and deployed using Kubernetes.

## Getting Started

To build and start the project, follow these steps:

1. **Build the Docker Image**:
   

```bash
   docker build -t img-kub
```
2. **Turn on Kubernetes**:
Ensure Kubernetes is enabled on your system.

3. **Deploy the Application**:
   

```bash
   kubectl apply -f deployment.yml
```

## Access Information

- **To access the web application:**:
  - Go to: http://localhost:30007/


- **To access the Kubernetes Dashboard:**:
  1. ***Deploy the Kubernetes dashboard:***:

       
  ```bash
     kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
  ```
  
    2. ***Apply admin user settings:***:


  ```bash
     kubectl apply -f dashboard-adminuser-setup.yaml
  ```
  
    3. ***Start the dashboard server:***:

       
  ```bash
     kubectl proxy
  ```
  
    4. ***Open the dashboard in your browser:***:

       

       http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
  
  
    5. ***Get the admin token:***:

       
  ```bash
     kubectl -n kubernetes-dashboard create token admin-user
  ```
  
  Copy the generated token and use it to log in to the Kubernetes dashboard.


## Features

- AI-powered weed recognition for four species 
- Rich information library about the detected weeds  
- Fully containerized and scalable with Kubernetes
- Integrated Kubernetes dashboard for monitoring and management

## Requirements

- Docker
- Kubernetes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
