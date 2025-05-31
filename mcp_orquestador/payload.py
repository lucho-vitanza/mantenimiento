# mcp_orquestador/payload.py
from typing import Dict, Any
import uuid
from datetime import datetime

class MCPPayload:
    def __init__(self, entrada: str, usuario: str = "desconocido"):
        self.id = str(uuid.uuid4())
        self.usuario = usuario
        self.input = entrada
        self.tipo_tarea = None  # será asignado por el agente de identificación
        self.agente_asignado = None
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "usuario": self.usuario,
            "input": self.input,
            "tipo_tarea": self.tipo_tarea,
            "agente_asignado": self.agente_asignado,
            "timestamp": self.timestamp,
        }
