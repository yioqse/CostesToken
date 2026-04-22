# Guía de Uso

## Instalación
Requiere Python 3.10+ y las siguientes librerías:
```powershell
pip install transformers torch pytest

## Ejecución

Para ver una demostración del sistema:
```powershell
    python main.py

**Pruebas**
Para validar que los cálculos son correctos:
```powershell
    $env:PYTHONPATH = "."
    pytest tests/