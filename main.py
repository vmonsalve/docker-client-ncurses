from core.socket_scanner import buscar_sockets
from core.controller import levantar_socket
from core.utils import socket_activo

def main():
    sockets = buscar_sockets()

    print("\n🔍 Sockets disponibles:")
    for i, s in enumerate(sockets):
        s.estado = socket_activo(s.path)
        estado_str = "🟢 Activo" if s.estado else "🔴 Inactivo"
        print(f"[{i}] {s.nombre:<25} {estado_str:<10} → {s.path}")

    try:
        opcion = int(input("\n👉 Ingresa el número del socket que deseas levantar: "))
        socket_seleccionado = sockets[opcion]

        if socket_seleccionado.estado:
            print("⚠️ Ya está activo.")
        else:
            print(f"🚀 Levantando: {socket_seleccionado.nombre}")
            exito = levantar_socket(socket_seleccionado)
            print("✅ Levantado" if exito else "❌ Falló al levantar")

    except (ValueError, IndexError):
        print("❌ Opción inválida.")

if __name__ == "__main__":
    main()