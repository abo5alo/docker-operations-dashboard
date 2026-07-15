from flask import Flask, render_template
import platform
import docker

app = Flask(__name__)

# Connect to Docker
try:
    client = docker.from_env()
except Exception:
    client = None


@app.route("/")
def home():

    # Docker information
    try:
        docker_version = client.version()["Version"] if client else "Unavailable"
        running_containers = len(client.containers.list()) if client else 0
        total_images = len(client.images.list()) if client else 0
        total_networks = len(client.networks.list()) if client else 0
        total_volumes = len(client.volumes.list()) if client else 0
    except Exception:
        docker_version = "Unavailable"
        running_containers = 0
        total_images = 0
        total_networks = 0
        total_volumes = 0

    dashboard = {
        "os": f"{platform.system()} {platform.release()}",
        "docker_version": docker_version,
        "framework": "Flask",
        "runtime": f"Python {platform.python_version()}",
        "container_name": platform.node(),
        "status": "Running",

        # Live Docker Metrics
        "running_containers": running_containers,
        "total_images": total_images,
        "total_networks": total_networks,
        "total_volumes": total_volumes,
    }

    return render_template("index.html", **dashboard)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
