import pandas as pd
import os

EQUIPOS_CSV_PATH = "data/equipos.csv"  # generado por convertir_excel_a_csv.py


def _cargar_dataframe():
    if not os.path.exists(EQUIPOS_CSV_PATH):
        raise FileNotFoundError(f"No se encuentra el archivo: {EQUIPOS_CSV_PATH}")
    
    df = pd.read_csv(EQUIPOS_CSV_PATH, dtype=str)
    columnas = list(df.columns)

    if len(columnas) < 2:
        raise ValueError("El archivo CSV debe contener al menos dos columnas.")

    df.rename(columns={columnas[0]: "equipo_id", columnas[1]: "nombre_equipo"}, inplace=True)
    return df


def obtener_nombre_desde_id(equipo_id):
    """
    Dado un ID de equipo, devuelve el nombre del equipo. Si no se encuentra, retorna None.
    """
    df = _cargar_dataframe()
    fila = df[df["equipo_id"] == str(equipo_id)]
    if not fila.empty:
        return fila.iloc[0]["nombre_equipo"]
    return None


def obtener_id_desde_nombre(nombre_equipo):
    """
    Dado el nombre de un equipo, devuelve el ID del equipo. Si no se encuentra, retorna None.
    """
    df = _cargar_dataframe()
    fila = df[df["nombre_equipo"].str.lower() == nombre_equipo.lower()]
    if not fila.empty:
        return fila.iloc[0]["equipo_id"]
    return None


def parsear_equipo(texto_usuario):
    """
    Determina si el texto contiene un ID de equipo o un nombre. Devuelve (equipo_id, nombre_equipo).
    Si no se encuentra nada, retorna (None, None).
    """
    texto = texto_usuario.lower()
    df = _cargar_dataframe()

    # Intentar por ID
    for _, fila in df.iterrows():
        if str(fila["equipo_id"]).lower() in texto:
            return fila["equipo_id"], fila["nombre_equipo"]

    # Intentar por nombre
    for _, fila in df.iterrows():
        if str(fila["nombre_equipo"]).lower() in texto:
            return fila["equipo_id"], fila["nombre_equipo"]

    return None, None
