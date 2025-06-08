# archivo: cloud/test_orquestador.py
import json
from orquestador import orquestar_desde_input

def test_payload_generacion():
    prompt = "¿Qué tareas recomienda el fabricante para el compresor principal CMP-AIR-01?"
    payload = orquestar_desde_input(prompt)

    assert isinstance(payload, dict), "El payload debe ser un diccionario"
    assert "tipo_tarea" in payload, "Falta tipo_tarea en el payload"
    assert "fuente" in payload, "Falta fuente en el payload"
    assert "contenido" in payload, "Falta contenido en el payload"
    assert payload["tipo_tarea"] == "recomendacion_fabricante", "Clasificación incorrecta"

    print("Payload generado correctamente:")
    print(json.dumps(payload, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    test_payload_generacion()
