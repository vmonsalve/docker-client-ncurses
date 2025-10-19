from pathlib import Path
from core.socket_scanner import buscar_sockets
from core.utils import socket_activo

# Buscar sockets en HOME
sockets = buscar_sockets()

# Evaluar estado activo de cada uno
for s in sockets:
    s.estado = socket_activo(s.path)
    print(f"Socket: {s.nombre}, Path: {s.path}, Activo: {s.estado}")
# Ahora puedes pasárselos al layout de curses