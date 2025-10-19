import socket
import os

def socket_activo(ruta_socket: str) -> bool:
    """Verifica si el socket UNIX en ruta_socket está activo y acepta conexiones."""
    if not os.path.exists(ruta_socket):
        return False

    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect(ruta_socket)
        sock.close()
        return True
    except (socket.error, OSError):
        return False