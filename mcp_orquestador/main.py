from mcp_orquestador.payload import MCPPayload
from mcp_orquestador.router import seleccionar_agente
from identificador_tarea.agent import identificar_tarea  # se definirá más adelante
import json

def procesar_input(input_text: str, usuario: str = "desconocido"):
    # 1. Crear payload base
    payload = MCPPayload(entrada=input_text, usuario=usuario)

    # 2. Enviar a agente identificador (ChatGPT)
    tipo_tarea = identificar_tarea(payload.input)
    payload.tipo_tarea = tipo_tarea

    # 3. Seleccionar agente
    payload.agente_asignado = seleccionar_agente(tipo_tarea)

    # 4. (Aquí se llamaría al agente específico según payload.agente_asignado)
    print(f"[MCP] Payload generado:\n{json.dumps(payload.to_dict(), indent=2)}")
    return payload

if __name__ == "__main__":
    texto = input("🔹 Ingrese una consulta: ")
    procesar_input(texto, usuario="usuario_test")
