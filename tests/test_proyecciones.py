import pytest
from calculadora.proyecciones import ProcesadorCostes

@pytest.fixture
def procesador_mini():
    return ProcesadorCostes("gpt-4o-mini")

def test_calculo_exacto_un_millon(procesador_mini):
    resultado = procesador_mini.calcular_detallado(1_000_000, 1_000_000)
    assert resultado["total_usd"] == 0.75

def test_coste_cero_tokens(procesador_mini):
    resultado = procesador_mini.calcular_detallado(0, 0)
    assert resultado["total_usd"] == 0.0

def test_proyeccion_mensual_coherencia(procesador_mini):
    # 100 llamadas/día * 30 días * 1000 tokens = 3,000,000 tokens totales
    # (3,000,000 / 1,000,000) * 0.75 (precio combinado) = 2.25
    resultado = procesador_mini.proyeccion_mensual(100, 1000, 1000, dias=30)
    assert resultado["llamadas_totales"] == 3000
    assert pytest.approx(resultado["total_usd"]) == 2.25 # <-- CORREGIDO