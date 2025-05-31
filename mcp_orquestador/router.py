# mcp_orquestador/router.py

def seleccionar_agente(tipo_tarea: str) -> str:
    mapping = {
        "consulta_tecnica": "agente_llamaindex",
        "analisis_fallas": "agente_datos_struct",
        "razonamiento": "agente_razonador",
    }
    return mapping.get(tipo_tarea, "agente_desconocido")
