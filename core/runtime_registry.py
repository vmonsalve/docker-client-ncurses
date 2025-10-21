import platform
from core.runtimes import RuntimeHandler

def is_colima(path): return ".colima" in path
def is_docker_desktop(path): return "vmnetd" in path
def is_docker_native(path): return path == "/var/run/docker.sock"

RUNTIMES = [
    RuntimeHandler("Colima", is_colima, ["colima", "start"], ["colima", "stop"]),
    RuntimeHandler("Docker Desktop", is_docker_desktop,
        ["open", "-a", "Docker"],
        ["osascript", "-e", 'quit app "Docker"']
    ),
    RuntimeHandler("Docker Native", is_docker_native,
        ["systemctl", "start", "docker"] if platform.system() == "Linux" else ["echo", "Docker no soportado"],
        ["systemctl", "stop", "docker"] if platform.system() == "Linux" else ["echo", "Docker no soportado"]
    )
]