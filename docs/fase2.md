# Prompt para Generación de Tests Unitarios

Este documento contiene el prompt optimizado para solicitar a un modelo de lenguaje (LLM) la generación de la suite de pruebas para el proyecto de Calculadora de Costes.

---

## Bloque de Prompt (Copiar a continuación)

**Rol:** Actúa como un Ingeniero de QA Senior especializado en Python y Testing.

**Contexto del Proyecto:**
Tengo un proyecto de "Calculadora de Costes de IA" refactorizado en módulos. El sistema es 100% local y utiliza la librería `transformers` de Hugging Face para el conteo de tokens y lógica matemática para calcular costes de API.

**Arquitectura del Código:**
1. `calculadora/precios.py`: Contiene un diccionario `PRECIOS_MODELOS` con tarifas por millón de tokens.
2. `calculadora/tokens.py`: Clase `ContadorTokens` que usa `AutoTokenizer` (Hugging Face).
3. `calculadora/proyecciones.py`: Clase `ProcesadorCostes` que realiza cálculos de USD y proyecciones mensuales.
4. `services/pipeline.py`: Clase `PipelineCostes` que conecta el texto bruto con los resultados finales.

**Tarea:**
Genera los tests unitarios completos para estos módulos utilizando `pytest`. Por cada módulo, debes cubrir:

1. **Casos Felices (Happy Path):** 
   - Procesamiento de textos estándar.
   - Modelos de IA existentes en el diccionario.
   - Cálculos con volúmenes de tokens normales.
2. **Casos Borde (Edge Cases):**
   - Strings vacíos (`""`).
   - Textos con caracteres especiales o muy largos.
   - Valores de tokens en cero o extremadamente altos (billones).
3. **Casos de Error y Resiliencia:**
   - Nombres de modelos que no existen (verificar que el sistema use el modelo por defecto).
   - Manejo de entradas inesperadas (tipos de datos incorrectos).

**Requisitos Técnicos:**
- Usa **fixtures** de `pytest` para evitar la duplicación de código en la inicialización de clases.
- Emplea **docstrings** detallados en cada función de test explicando el objetivo.
- Asegúrate de que las importaciones sigan la estructura: `from calculadora.modulo import Clase`.
- 
**Ejecucion de testst**
$env:PYTHONPATH = "."
pytest tests/
========================== test session starts ===========================
platform win32 -- Python 3.11.9, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\Users\IA\Documents\CostesToken
plugins: anyio-4.13.0, mock-3.15.1
collected 6 items                                                         

tests\test_pipeline.py ...                                          [ 50%]
tests\test_proyecciones.py ...                                      [100%]

=========================== 6 passed in 9.04s ============================