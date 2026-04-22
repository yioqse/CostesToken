import pytest
from services.pipeline import PipelineCostes

def test_pipeline_calculo_correcto():
    # Inicializamos pipeline con modelo mini (precios conocidos)
    pipeline = PipelineCostes(modelo_ia="gpt-4o-mini")
    
    # Datos de prueba
    prompt = "Hola" 
    respuesta = "Mundo" # 2 tokens aprox cada uno
    
    resultado = pipeline.procesar_texto(prompt, respuesta)
    
    # Validaciones
    assert "tokens" in resultado
    assert "economia" in resultado
    assert resultado["tokens"]["in"] > 0
    assert resultado["economia"]["total_usd"] > 0

def test_modelo_inexistente_fallback():
    # Si el modelo no existe, debería usar el fallback de gpt-4o-mini
    pipeline = PipelineCostes(modelo_ia="modelo-inventado")
    assert pipeline.procesador.precios["input"] == 0.15