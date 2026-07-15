# Docker Operations Dashboard

A Docker monitoring dashboard built with Flask, Docker, and the Docker SDK for Python.

The application displays live information from the Docker Engine, including container statistics, Docker version, networks, images, volumes, and system information through a clean web interface.

---

## Overview

This project demonstrates how to build a Docker-aware web application using the official Docker SDK for Python. Instead of executing shell commands, the application communicates directly with the Docker Engine API to retrieve live information.

---

## Features

- Live Docker Engine version
- Running container count
- Docker image count
- Docker network count
- Docker volume count
- Python runtime information
- Linux operating system information
- Responsive dashboard interface
- Docker SDK integration
- Dockerized deployment

---

## Technologies Used

- Python 3
- Flask
- Docker
- Docker SDK for Python
- Jinja2
- HTML5
- CSS3

---

## Project Structure

```text
docker-operations-dashboard/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/abo5alo/docker-operations-dashboard.git
cd docker-operations-dashboard
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Build the Docker image:

```bash
docker build -t docker-operations-dashboard .
```

Run the application:

```bash
docker run \
-p 5000:5000 \
-v /var/run/docker.sock:/var/run/docker.sock \
docker-operations-dashboard
```

Open your browser and navigate to:

```text
http://localhost:5000
```

---

## Dashboard Information

The dashboard displays live information including:

- Docker Engine Version
- Running Containers
- Docker Images
- Docker Networks
- Docker Volumes
- Python Runtime
- Linux Operating System
- Container Hostname

---

## Screenshots

Add screenshots of the dashboard here.

Example:

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

## What I Learned

Through this project I gained hands-on experience with:

- Building Docker images
- Writing Dockerfiles
- Developing Flask applications
- Using the Docker SDK for Python
- Communicating with the Docker Engine API
- Containerized application deployment
- Rendering dynamic data using Jinja2 templates

---

## Future Improvements

- Display running container details
- CPU and memory usage monitoring
- Container uptime information
- Docker Compose integration
- Authentication for the dashboard

---

## Author

Ahmed Emad
