# calculadora/tokens.py
from transformers import AutoTokenizer

class ContadorTokens:
    """Usa modelos de Hugging Face para conteo local de tokens"""
    def __init__(self, modelo_local: str = "gpt2"):
        # gpt2 es un tokenizador estándar que funciona offline
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(modelo_local)
        except Exception:
            # Fallback en caso de no tener internet la primera vez
            print("Cargando tokenizador de emergencia...")
            self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

    def contar(self, texto: str) -> int:
        tokens = self.tokenizer.encode(texto)
        return len(tokens)