from core.runtime_registry import RUNTIMES
from core.models import DockerSocket

def get_handler_for(sock: DockerSocket):
    for handler in RUNTIMES:
        if handler.matches(sock.path):
            return handler
    return None

def levantar_socket(sock: DockerSocket):
    handler = get_handler_for(sock)
    if handler:
        return handler.start()
    else:
        print(f"No hay handler para: {sock.path}")
        return False

def bajar_socket(sock: DockerSocket):
    handler = get_handler_for(sock)
    if handler:
        return handler.stop()
    else:
        print(f"No hay handler para: {sock.path}")
        return False