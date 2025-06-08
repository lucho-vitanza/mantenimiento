# archivo: cloud/orquestador.py
import json
from datetime import datetime
from gestor_tipo_consulta import generar_payload_desde_input as ejecutar_consulta_estructurada
from gestor_tipo_consulta import clasificar_tipo_consulta
from parser_equipo import parsear_equipo
from parser_fecha import interpretar_fecha
from gestor_tipo_consulta import generar_payload_desde_input as ejecutar_consulta_estructurada

# MCP Payload base
class MCPPayload:
    def __init__(self, tipo_tarea, fuente, contenido):
        self.timestamp = datetime.now().isoformat()
        self.tipo_tarea = tipo_tarea
        self.fuente = fuente  # "estructurada" o "semantica"
        self.contenido = contenido

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "tipo_tarea": self.tipo_tarea,
            "fuente": self.fuente,
            "contenido": self.contenido
        }


def orquestar_desde_input(texto_usuario):
    tipo = clasificar_tipo_consulta(texto_usuario)

    if tipo in ["recomendacion_fabricante", "explicacion_estructura"]:
        # Construcción de payload semántico
        equipo_id, nombre_equipo = parsear_equipo(texto_usuario)
        consulta_sem = ConsultaSemantica(
            pregunta=texto_usuario,
            topico="mantenimiento",
            entidad=nombre_equipo
        )
        payload = MCPPayload(
            tipo_tarea=tipo,
            fuente="semantica",
            contenido=consulta_sem.to_dict()
        )
        agente_destino = "agente_llamaindex"

    else:
        # Construcción y ejecución de consulta estructurada
        payload_struct = ejecutar_consulta_estructurada(texto_usuario)
        payload = MCPPayload(
            tipo_tarea=tipo,
            fuente="estructurada",
            contenido=payload_struct
        )
        agente_destino = "agente_datos_struct"

    # Enviar al agente correspondiente
    ejecutar_agente(payload, agente_destino)
    return payload.to_dict()


def ejecutar_agente(payload, agente_destino):
    print(f"Enviando tarea a {agente_destino}...")
    print(json.dumps(payload.to_dict(), indent=2, ensure_ascii=False))


# Ejemplo de ejecución directa
if __name__ == "__main__":
    texto_input = input("Escribe tu consulta: ")
    resultado = orquestar_desde_input(texto_input)
    print("\nPayload final enviado:")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
