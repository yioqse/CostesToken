# creacion de estructura
comando de linea única para crear la estructura de ficheros

New-Item -ItemType Directory docs, services, interface; New-Item -Force calculadora/proyecciones.py, calculadora/tokens.py, calculadora/precios.py, tests/test_proyecciones.py, tests/test_tokens.py, tests/test_precios.py, .github/workflows/ci.yml

# Auditoria
# Informe de Auditoría y Refactorización - Fase 1

## 1. Análisis del Código Heredado
- **Estado Original:** Un único archivo script con lógica mezclada (datos de precios, cálculo y conteo de tokens).
- **Dependencias Críticas:** `openai`, `tiktoken` (específico para modelos GPT).
- **Limitación:** El código está diseñado para APIs de pago, no para modelos locales.

## 2. Acciones Realizadas
1. **Desacoplamiento:** Se ha separado la lógica en tres módulos: `precios.py` (datos), `tokens.py` (conteo local) y `proyecciones.py` (cálculos).
2. **Migración a Local:** Se ha sustituido `tiktoken` por la librería `transformers` de Hugging Face. Esto permite usar tokenizadores de modelos locales como Llama 3, Mistral o Phi-3.
3. **Abstracción de Precios:** Se movieron los precios a un diccionario independiente para facilitar actualizaciones sin tocar la lógica de cálculo.

## 3. Cambios en la Lógica de Tokenización
- Antes: Dependía de `tiktoken.encoding_for_model`.
- Ahora: Utiliza `AutoTokenizer` de `transformers`, lo que permite cargar el archivo `.json` del tokenizador de cualquier modelo descargado localmente.

# Instalación de paquetes

    - pip install transformers torch
