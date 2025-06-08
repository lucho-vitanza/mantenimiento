# archivo: agentes_locales/agente_datos_struct/consulta.py
from datetime import datetime
import pandas as pd

class ConsultaEstructurada:
    def __init__(self, tabla, filtros=None, agrupaciones=None, operaciones=None):
        self.tabla = tabla
        self.filtros = filtros or []
        self.agrupaciones = agrupaciones or []
        self.operaciones = operaciones or []

    def ejecutar(self, df):
        """
        Ejecuta la consulta sobre un DataFrame dado.
        """
        df_resultado = df.copy()

        # Aplicar filtros
        for f in self.filtros:
            campo = f["campo"]
            condicion = f["condicion"]
            valor = f["valor"]

            if condicion == "equals":
                df_resultado = df_resultado[df_resultado[campo] == valor]
            elif condicion == "startswith":
                df_resultado = df_resultado[df_resultado[campo].str.startswith(valor)]
            elif condicion == "fecha_mayor_igual":
                df_resultado[campo] = pd.to_datetime(df_resultado[campo], errors="coerce")
                df_resultado = df_resultado[df_resultado[campo] >= pd.to_datetime(valor)]
            elif condicion == "fecha_menor_igual":
                df_resultado[campo] = pd.to_datetime(df_resultado[campo], errors="coerce")
                df_resultado = df_resultado[df_resultado[campo] <= pd.to_datetime(valor)]

        # Agrupar y aplicar operaciones
        if self.agrupaciones:
            df_grouped = df_resultado.groupby(self.agrupaciones)

            resultados = {}
            for op in self.operaciones:
                if op == "count":
                    resultados["count"] = df_grouped.size().reset_index(name="total")
                # Agregar otras operaciones si es necesario
            return resultados

        return df_resultado


class ConsultaSemantica:
    def __init__(self, pregunta, topico=None, entidad=None):
        self.pregunta = pregunta
        self.topico = topico
        self.entidad = entidad
        self.timestamp = datetime.now().isoformat()

    def to_prompt(self):
        """
        Prepara un prompt contextual para el agente RAG o LLM.
        """
        contexto = f"Pregunta: {self.pregunta}\n"
        if self.topico:
            contexto += f"Tópico: {self.topico}\n"
        if self.entidad:
            contexto += f"Entidad referida: {self.entidad}\n"
        return contexto.strip()

    def to_dict(self):
        return {
            "pregunta": self.pregunta,
            "topico": self.topico,
            "entidad": self.entidad,
            "timestamp": self.timestamp
        }
