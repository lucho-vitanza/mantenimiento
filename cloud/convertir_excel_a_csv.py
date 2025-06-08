# archivo: convertir_excel_a_csv.py
import pandas as pd
import os

EQUIPOS_EXCEL_PATH = "data/lista_equipos_26-05-25.xlsx"
EQUIPOS_CSV_PATH = "data/equipos.csv"

if not os.path.exists(EQUIPOS_EXCEL_PATH):
    raise FileNotFoundError(f"No se encuentra el archivo: {EQUIPOS_EXCEL_PATH}")

# Cargar columnas específicas del Excel
columnas_necesarias = ["Denominación", "Equipo"]
df = pd.read_excel(EQUIPOS_EXCEL_PATH, usecols=columnas_necesarias, dtype=str)

# Renombrar columnas para uso posterior

# 'Denominación' => nombre_equipo
# 'Equipo' => equipo_id
df.columns = ["nombre_equipo", "equipo_id"]

# Guardar como CSV para uso liviano en parseo
os.makedirs("data", exist_ok=True)
df.to_csv(EQUIPOS_CSV_PATH, index=False)

print(f"✅ Conversión completada: {EQUIPOS_CSV_PATH}")
