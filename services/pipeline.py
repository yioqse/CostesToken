# services/pipeline.py
from calculadora.tokens import ContadorTokens
from calculadora.proyecciones import ProcesadorCostes

class PipelineCostes:
    """Orquesta el flujo de datos desde texto bruto hasta resultados económicos"""
    
    def __init__(self, modelo_ia: str, modelo_tokenizer: str = "gpt2"):
        self.contador = ContadorTokens(modelo_tokenizer)
        self.procesador = ProcesadorCostes(modelo_ia)

    def procesar_texto(self, texto_input: str, texto_output: str) -> dict:
        """Pipeline: Texto -> Tokens -> Coste"""
        t_in = self.contador.contar(texto_input)
        t_out = self.contador.contar(texto_output)
        
        datos_coste = self.procesador.calcular_detallado(t_in, t_out)
        
        # Extensibilidad: Podríamos añadir aquí análisis de sentimiento o detección de idioma
        return {
            "metadata": {"modelo": self.procesador.precios},
            "tokens": {"in": t_in, "out": t_out},
            "economia": datos_coste
        }