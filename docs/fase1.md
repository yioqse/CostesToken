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
1. Descomposición de Monolito: El código original de un solo archivo se dividió en 3 módulos lógicos dentro de calculadora/.

2. Sustitución de Dependencias de API: Se eliminó tiktoken (que requiere conexión y es propietario de OpenAI) y se implementó transformers (Hugging Face) en tokens.py para permitir el conteo de tokens en local.

3. Abstracción de Datos: Los precios se movieron a precios.py para permitir actualizaciones de tarifas sin tocar el código de cálculo.

4. Implementación de Punto de Entrada: Se creó main.py utilizando el patrón de diseño de inyección de lógica, facilitando que en el futuro se puedan cambiar los modelos de IA local sin romper el programa.

## 3. Cambios en la Lógica de Tokenización
- Antes: Dependía de `tiktoken.encoding_for_model`.
- Ahora: Utiliza `AutoTokenizer` de `transformers`, lo que permite cargar el archivo `.json` del tokenizador de cualquier modelo descargado localmente.

# Instalación de paquetes

    - pip install transformers torch
