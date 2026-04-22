# calculadora/tokens.py
from transformers import AutoTokenizer

class ContadorTokens:
    """Usa modelos de Hugging Face para conteo local de tokens"""
    def __init__(self, modelo_local: str = "gpt2"):
        try:
            # Esto carga el tokenizador localmente
            self.tokenizer = AutoTokenizer.from_pretrained(modelo_local)
        except Exception:
            # Fallback en caso de error
            self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

    def contar(self, texto: str) -> int:
        if texto is None:
            raise AttributeError("El texto no puede ser None")
        if not texto:
            return 0
        tokens = self.tokenizer.encode(texto)
        return len(tokens)