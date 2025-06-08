from datetime import datetime, timedelta
import re


def interpretar_fecha(texto):
    texto = texto.lower()
    hoy = datetime.today()

    # Último mes calendario
    if "último mes" in texto:
        primer_dia_mes_anterior = (hoy.replace(day=1) - timedelta(days=1)).replace(day=1)
        ultimo_dia_mes_anterior = hoy.replace(day=1) - timedelta(days=1)
        return primer_dia_mes_anterior.strftime("%Y-%m-%d"), ultimo_dia_mes_anterior.strftime("%Y-%m-%d")

    # Últimos N meses
    match_n_meses = re.search(r"últimos (\d+) meses", texto)
    if match_n_meses:
        n = int(match_n_meses.group(1))
        fecha_inicio = (hoy.replace(day=1) - timedelta(days=1)).replace(day=1) - timedelta(days=30 * (n - 1))
        return fecha_inicio.strftime("%Y-%m-%d"), hoy.strftime("%Y-%m-%d")

    # Este año
    if "este año" in texto:
        return f"{hoy.year}-01-01", hoy.strftime("%Y-%m-%d")

    # Año pasado
    if "año pasado" in texto:
        return f"{hoy.year - 1}-01-01", f"{hoy.year - 1}-12-31"

    # Si no se puede identificar
    return None, None
