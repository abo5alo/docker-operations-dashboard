# Flask Nginx Deployment

A production-style deployment of a Flask application using Gunicorn as the WSGI server and Nginx as a reverse proxy on Ubuntu 24.04.

---

## Features

- Flask web application
- Gunicorn application server
- Nginx reverse proxy
- Python virtual environment
- systemd service for automatic startup
- HTML templates
- CSS styling
- Production-style deployment architecture

---

## Technologies

- Python 3.12
- Flask
- Gunicorn
- Nginx
- Ubuntu 24.04 LTS
- systemd
- HTML5
- CSS3

---

## Project Structure

```
flask-nginx-deployment/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── images/
│   └── flask-dashboard.png
├── .gitignore
└── README.md
```

---

## Deployment Architecture

```
Browser
    │
    ▼
Nginx
    │
    ▼
Gunicorn
    │
    ▼
Flask Application
```

---

## Screenshot

![Flask Dashboard](images/flask-dashboard.png)

---

## Running the Project

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install flask gunicorn
```

Run locally:

```bash
python app.py
```

Run with Gunicorn:

```bash
gunicorn app:app
```

---

## What I Learned

- Deploying Flask applications
- Managing Python virtual environments
- Configuring Gunicorn
- Creating systemd services
- Configuring Nginx as a reverse proxy
- Serving static assets
- Linux service management

---

## Author

Ahmed Emad
