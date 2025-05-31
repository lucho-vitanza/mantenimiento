# identificador_tarea/agent.py

def identificar_tarea(texto_input: str) -> str:
    # Simulación simple: heurística por palabras clave
    texto = texto_input.lower()
    if "fallas" in texto or "repetidas" in texto:
        return "analisis_fallas"
    elif "manual" in texto or "cómo funciona" in texto or "especificaciones" in texto:
        return "consulta_tecnica"
    elif "por qué" in texto or "debo hacer" in texto:
        return "razonamiento"
    else:
        return "consulta_tecnica"  # por defecto
