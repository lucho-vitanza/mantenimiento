# main.py
from .logic import analizar_datos

def procesar(payload: dict) -> str:
    resultado = analizar_datos(payload)
    return resultado

if __name__ == "__main__":
    payload_simulado = {
        "input": "¿Qué equipo tuvo más fallas?",
        "tipo_tarea": "analisis_fallas",
        "usuario": "luciano",
    }
    print(procesar(payload_simulado))
