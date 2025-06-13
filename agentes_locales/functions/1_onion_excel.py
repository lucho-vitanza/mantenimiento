import pandas as pd

def main():
    # 1. Cargar el DataFrame principal
    print("📥 Cargando './total.xlsx'...")
    df_total = pd.read_excel("./total.xlsx")

    # 2. Cargar el archivo maestro
    print("📥 Cargando './Tabla_maestra_equipos.xlsx'...")
    df_info = pd.read_excel("./Tabla_maestra_equipos.xlsx")

    # 3. Extraer las columnas clave por índice
    col_df_total = df_total.columns[0]     # ejemplo: 'archivo_origen'
    col_df_info = df_info.columns[5]       # columna índice 6 del maestro

    print(f"🔑 Clave en df_total: {col_df_total}")
    print(f"🔑 Clave en df_info: {col_df_info}")

    # 4. Asegurar mismo tipo (int o str)
    try:
        df_total[col_df_total] = df_total[col_df_total].astype(int)
        df_info[col_df_info] = df_info[col_df_info].astype(int)
    except Exception as e:
        print(f"⚠️ Conversión a int fallida: {e}")
        print("➡ Convirtiendo ambas claves a string...")
        df_total[col_df_total] = df_total[col_df_total].astype(str)
        df_info[col_df_info] = df_info[col_df_info].astype(str)

    # 5. Merge 1:* usando left join
    print("🔗 Realizando merge...")
    df_unido = pd.merge(
        df_total,
        df_info,
        left_on=col_df_total,
        right_on=col_df_info,
        how='left'
    )

    # 6. Detectar filas sin match
    sin_match = df_unido[df_unido.isnull().any(axis=1)]
    print(f"⚠ Filas sin coincidencia: {len(sin_match)}")

    if not sin_match.empty:
        sin_match.to_excel('./filas_sin_match.xlsx', index=False)
        print("📝 Filas sin match guardadas en './filas_sin_match.xlsx'")

    # 7. Eliminar columna duplicada si es distinta de la clave izquierda
    if col_df_info != col_df_total:
        df_unido.drop(columns=[col_df_info], inplace=True)

    # 8. Guardar resultado final
    output_path = './df_total_unido.xlsx'
    df_unido.to_excel(output_path, index=False)
    print(f"✅ Archivo final guardado en: {output_path}")

if __name__ == "__main__":
    main()
