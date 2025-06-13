import os
import pandas as pd

path_carpeta = './data/'

def unir_excels_con_nombre(path_carpeta):
    archivos = [f for f in os.listdir(path_carpeta) if f.endswith('.xlsx')]
    df_total = pd.DataFrame()

    for archivo in archivos:
        ruta = os.path.join(path_carpeta, archivo)
        nombre_archivo = os.path.splitext(archivo)[0]

        # Leer archivo
        df = pd.read_excel(ruta)

        # Insertar la columna al principio
        df.insert(0, 'archivo_origen', nombre_archivo)

        # Concatenar
        df_total = pd.concat([df_total, df], ignore_index=True)

    return df_total

def main():
    df_total = unir_excels_con_nombre(path_carpeta)
    df_total.to_excel('./total.xlsx', index=False)

if __name__ == '__main__':
    main()
