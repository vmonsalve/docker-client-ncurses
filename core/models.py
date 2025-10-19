from dataclasses import dataclass

@dataclass
class DockerSocket:
    nombre: str
    path: str
    estado: bool = False  # Inactivo por defecto