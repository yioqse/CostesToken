# Arquitectura del Sistema - Calculadora Local

## Diseño por Capas
El sistema sigue un diseño de arquitectura limpia dividido en:

1.  **Capa de Dominio (calculadora/):** Contiene la lógica pura. 
    - `precios.py`: Fuente de verdad de las tarifas.
    - `tokens.py`: Motor de tokenización local (Hugging Face).
    - `proyecciones.py`: Cálculos matemáticos financieros.
2.  **Capa de Servicio (services/):** Orquesta el flujo de datos.
    - `pipeline.py`: Convierte entradas de texto en informes económicos.
3.  **Capa de Interfaz (interface/):** Maneja la salida de datos.
    - `presenter.py`: Formateo de consola.
4.  **Infraestructura (tests/ y .github/):** Asegura la calidad y el despliegue continuo.

## Decisiones Técnicas
- **Independencia de API:** Se eligió `transformers` para permitir el conteo de tokens sin latencia de red ni costes de API.
- **Extensibilidad:** El sistema permite añadir nuevos modelos simplemente actualizando `precios.py`.