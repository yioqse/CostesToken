# tests/test_proyecciones.py
from calculadora.proyecciones import ProcesadorCostes

def test_calculo_basico():
    # Usamos gpt-4o-mini como base (0.15 entrada, 0.60 salida por millon)
    procesador = ProcesadorCostes("gpt-4o-mini")
    resultado = procesador.calcular_detallado(1_000_000, 1_000_000)
    assert resultado["total_usd"] == 0.75