# archivo: agentes_locales/agente_datos_struct/gestor_tipo_consulta.py
import json
from datetime import datetime
from consulta import ConsultaEstructurada
from parser_fecha import interpretar_fecha
from parser_equipo import parsear_equipo
from config import LOGS_PATH


def clasificar_tipo_consulta(texto_usuario):
    """
    Clasificación monolítica de tipo de consulta basado en reglas básicas.
    """
    texto = texto_usuario.lower()

    if any(p in texto for p in ["manual", "fabricante", "recomendación"]):
        return "recomendacion_fabricante"
    elif any(p in texto for p in ["diferencia", "qué es", "explicación"]):
        return "explicacion_estructura"
    elif any(p in texto for p in ["historial", "fallas", "intervenciones"]):
        return "historico_equipo"
    elif any(p in texto for p in ["tareas", "plan", "preventivo", "hoja de ruta"]):
        return "actividad_preventiva"
    elif any(p in texto for p in ["qué pasó", "último mes", "problema"]):
        return "consulta_mixta"
    else:
        return "analisis_operacional"


def generar_payload_desde_input(texto_usuario):
    tipo_consulta = clasificar_tipo_consulta(texto_usuario)
    equipo_id, nombre_equipo = parsear_equipo(texto_usuario)
    fecha_inicio, fecha_fin = interpretar_fecha(texto_usuario)

    filtros = []
    if equipo_id:
        filtros.append({"campo": "equipo_id", "condicion": "equals", "valor": equipo_id})
    if fecha_inicio:
        filtros.append({"campo": "fecha", "condicion": "fecha_mayor_igual", "valor": fecha_inicio})
    if fecha_fin:
        filtros.append({"campo": "fecha", "condicion": "fecha_menor_igual", "valor": fecha_fin})

    consulta_obj = ConsultaEstructurada(
        tabla="ordenes_trabajo",
        filtros=filtros,
        agrupaciones=["equipo_id"] if equipo_id else [],
        operaciones=["count"]
    )

    payload = {
        "timestamp": datetime.now().isoformat(),
        "input_usuario": texto_usuario,
        "tipo_consulta": tipo_consulta,
        "equipo": equipo_id,
        "nombre_equipo": nombre_equipo,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "payload_consulta": consulta_obj.__dict__
    }

    # Guardar log en disco
    nombre_log = f"payload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(f"{LOGS_PATH}/{nombre_log}", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    return payload
