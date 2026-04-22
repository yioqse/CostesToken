import pytest
from services.pipeline import PipelineCostes
from calculadora.proyecciones import ProcesadorCostes # <-- CORREGIDO

@pytest.fixture
def pipeline():
    return PipelineCostes(modelo_ia="gpt-4o-mini", modelo_tokenizer="gpt2")

def test_flujo_completo_pipeline(pipeline):
    resultado = pipeline.procesar_texto("Hola", "Mundo")
    assert "tokens" in resultado
    assert resultado["economia"]["total_usd"] > 0

def test_pipeline_texto_vacio(pipeline):
    resultado = pipeline.procesar_texto("", "")
    assert resultado["tokens"]["in"] == 0
    assert resultado["economia"]["total_usd"] == 0.0

def test_pipeline_cambio_modelo(pipeline):
    # Ahora 'ProcesadorCostes' ya está importado y no dará NameError
    pipeline.procesador = ProcesadorCostes("gpt-4o")
    resultado = pipeline.procesar_texto("Hola", "Adiós")
    assert resultado["economia"]["total_usd"] > 0