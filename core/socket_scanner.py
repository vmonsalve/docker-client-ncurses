# core/socket_scanner.py

import os
import stat
from pathlib import Path
from core.models import DockerSocket


# Nombres exactos que nos interesan
SOCKETS_DOCKER_VALIDOS = {
    "docker.sock",
    "default/docker.sock",
    "com.docker.vmnetd.sock",
}


def es_socket_unix(path: str) -> bool:
    try:
        mode = os.stat(path).st_mode
        return stat.S_ISSOCK(mode)
    except (FileNotFoundError, PermissionError):
        return False


def es_docker_socket(path: str) -> bool:
    """
    Verifica si el socket es uno de los esperados,
    sin depender de una ruta absoluta fija.
    """
    path = path.lower()

    for esperado in SOCKETS_DOCKER_VALIDOS:
        if path.endswith(esperado):
            return True

    return False


def buscar_sockets():
    rutas = [
        str(Path.home() / ".colima"),
        "/var/run",
        "/run",
        "/tmp"
    ]

    encontrados = []

    for ruta_base in rutas:
        if not os.path.exists(ruta_base):
            continue

        for root, _, files in os.walk(ruta_base):
            for nombre in files:
                full_path = os.path.join(root, nombre)
                if not es_socket_unix(full_path):
                    continue

                if not es_docker_socket(full_path):
                    continue

                encontrados.append(DockerSocket(
                    nombre=nombre,
                    path=full_path,
                    estado=False
                ))

    return encontrados