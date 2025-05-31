# IA_LEAR - Arquitectura Inteligente para Mantenimiento Predictivo

## 🎯 Objetivo

Orquestar un sistema de análisis e interpretación de datos industriales mediante una arquitectura modular basada en MCP (Model Control Protocol), integrando:

- Entrada por bot de Telegram
- Orquestador local MCP
- LLM local para identificación de tareas
- Agentes especializados (estructura, visión, razonamiento)
- Recuperación semántica con LlamaIndex
- Explicación natural con GPT-3.5-turbo
- Automatización de entrada/salida con n8n

---

## 🧱 Componentes del sistema

### 📲 Entrada / UI
- `bot_telegram/`: recibe preguntas del usuario, las formatea y reenvía al orquestador.

### 🔁 Orquestación
- `mcp_orquestador/`: núcleo del sistema, construye `mcp_payload`, enruta según tipo de tarea.

### 🧠 Identificador de tareas
- `identificador_tarea/`: modelo LLM local (llama-cpp-python) que clasifica intenciones del usuario.

### 🧩 Agentes locales
- `agentes_locales/agente_datos_struct`: procesa históricos estructurados (pandas/SQL).
- `agente_razonador`: lógica por reglas.
- `agente_vision`: opcional para análisis visual.

### 🔍 Agente semántico
- `agente_llamaindex/`: utiliza LlamaIndex con FAISS/Chroma para consultar documentos técnicos vectorizados.

### 📢 Agente explicador
- Usa `OpenAI GPT-3.5-turbo` para transformar el resultado en explicaciones comprensibles.

### ⚙️ Utilidades compartidas
- `shared/`: funciones comunes, loggers, modelos base, utilidades de formateo.

---

## 🛠️ Automación
- `n8n`: gestiona los flujos entrada/salida (Telegram/email/API), dispara el orquestador local vía Webhook o CLI.

---

## 🔐 Seguridad
- `.env`: contiene claves API, rutas de modelos y configuración sensible.

---

## 📂 Estructura de carpetas

