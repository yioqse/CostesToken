# calculadora/tokens.py
from transformers import AutoTokenizer

class ContadorTokensLocal:
    def __init__(self, modelo_path: str = "gpt2"): 
        # "gpt2" es un tokenizador genérico pequeño si no tienes uno descargado
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(modelo_path)
        except:
            print(f"Advertencia: No se pudo cargar {modelo_path}, usando gpt2 por defecto.")
            self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

    def estimar(self, texto: str) -> int:
        return len(self.tokenizer.encode(texto))