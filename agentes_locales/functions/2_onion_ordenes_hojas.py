import pandas as pd

def unir_ordenes_y_hojas():
    # 1. Cargar órdenes de trabajo
    print("📥 Cargando './ordenes_trabajo.xlsx'...")
    df_ordenes = pd.read_excel("./ordenes_trabajo.xlsx")
    

    # 2. Cargar dataframe enriquecido con operaciones teóricas
    print("📥 Cargando './df_total_unido.xlsx'...")
    df_total = pd.read_excel("./df_total_unido.xlsx")


    # 3. Verificar que las columnas necesarias existan
    col_hoja_ordenes = "notificaciones_ordenes.Gpo.hojas ruta"
    col_oper_ordenes = "notificaciones_ordenes.notificaciones.Operación"
    col_hoja_total = "archivo_origen"
    col_oper_total = "Operación"

    print("\n🔍 Verificando existencia de columnas clave:")
    print(f"- {col_hoja_ordenes} en df_ordenes: {col_hoja_ordenes in df_ordenes.columns}")
    print(f"- {col_oper_ordenes} en df_ordenes: {col_oper_ordenes in df_ordenes.columns}")
    print(f"- {col_hoja_total} en df_total: {col_hoja_total in df_total.columns}")
    print(f"- {col_oper_total} en df_total: {col_oper_total in df_total.columns}")

    # 🧼 Normalización clave 'archivo_origen' de df_total
    df_total[col_hoja_total] = (
    df_total[col_hoja_total]
    .astype(str)
    .str.strip()
    .str.zfill(5)
    )
    df_ordenes[col_hoja_ordenes] = (
    df_ordenes[col_hoja_ordenes]
    .astype(str)           # convertir todo a string
    .str.extract(r'(\d+)') # extraer solo números (quita .0 y NaNs)
    [0]                    # extraer el primer grupo
    .fillna('')            # evitar errores
    .str.zfill(5)          # agregar ceros a la izquierda
    )

    # 4. Asegurar tipos compatibles
    
    # 4.1 Convertir a string, limpiar espacios, y rellenar ceros a la izquierda (5 dígitos como ejemplo)
    df_ordenes[col_hoja_ordenes] = df_ordenes[col_hoja_ordenes].astype(str).str.strip().str.zfill(5)
    df_total[col_hoja_total] = df_total[col_hoja_total].astype(str).str.strip().str.zfill(5)

    # Operaciones también se normalizan
    df_ordenes[col_oper_ordenes] = df_ordenes[col_oper_ordenes].astype(str).str.strip()
    df_total[col_oper_total] = df_total[col_oper_total].astype(str).str.strip()


    # 4.2 Verificar coincidencias exactas
    print("\n🔎 Coincidencias exactas por clave:")
    coinciden_hojas = df_ordenes[col_hoja_ordenes].isin(df_total[col_hoja_total]).sum()
    coinciden_operaciones = df_ordenes[col_oper_ordenes].isin(df_total[col_oper_total]).sum()
    total_filas = len(df_ordenes)

    print(f"- Hojas de ruta que coinciden: {coinciden_hojas}/{total_filas}")
    print(f"- Operaciones que coinciden: {coinciden_operaciones}/{total_filas}")

    print("\n🔍 Valores únicos de 'archivo_origen':")
    print(df_total["archivo_origen"].drop_duplicates().sort_values().head(20))

    print("\n🔍 Valores únicos de 'notificaciones_ordenes.Gpo.hojas ruta':")
    print(df_ordenes["notificaciones_ordenes.Gpo.hojas ruta"].drop_duplicates().sort_values().head(20))


    # 5. Merge muchos-a-muchos por hoja de ruta y operación
    print("\n🔗 Realizando merge...")
    df_completo = pd.merge(
        df_ordenes,
        df_total,
        left_on=[col_hoja_ordenes, col_oper_ordenes],
        right_on=[col_hoja_total, col_oper_total],
        how='left',
        indicator=True
    )

    # 6. Crear columna "match"
    df_completo["match"] = df_completo["_merge"] == "both"

    # 7. Guardar resultados
    df_completo.to_excel("./ordenes_con_hojas_unidas.xlsx", index=False)
    print("✅ Archivo unido guardado: ./ordenes_con_hojas_unidas.xlsx")

    # 8. Filtrar no matcheados
    sin_match = df_completo[df_completo["match"] == False]
    if not sin_match.empty:
        sin_match.to_excel("./ordenes_sin_match_hoja_op.xlsx", index=False)
        print(f"⚠️ Se encontraron {len(sin_match)} órdenes sin coincidencia. Guardadas en './ordenes_sin_match_hoja_op.xlsx'")
    else:
        print("🎉 Todas las órdenes encontraron su operación en la hoja de ruta.")

if __name__ == "__main__":
    unir_ordenes_y_hojas()
