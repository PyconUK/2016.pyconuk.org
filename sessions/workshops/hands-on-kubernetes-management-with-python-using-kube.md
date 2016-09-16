title: Hands on Kubernetes management with Python using Kube
speaker: david-charles
---
Kubernetes (K8s) is the Google Borg inspired control plane for Docker containers that everyone is talking about. It has a great API but needs a load of HTTP client code and JSON processing to use it from Python. This workshop will quickly get you up to speed on using Kube, a Python wrapper around the K8s API. You'll learn how to connect to the API server for your K8s cluster; and how to view, create, update and delete resources within it. You'll also learn about Kube's support for the 'Watch' API which enables your code to respond to resource updates in you K8s cluster.

In preparation for the workshop you should install minikube 0.9.0 on your laptop (in my experience this was very easy).  minikube enables you to run a single node Kubernetes cluster - you will be interacting with it using kube.  The installation instructions for minikube are on GitHub:

<https://github.com/kubernetes/minikube/releases>

Installation is possible on Linux and OSX, however Windows is still experimental.

To save time you should also `pip install kube`. You'll need Python 3.4, other Python 3 variants should work too.
