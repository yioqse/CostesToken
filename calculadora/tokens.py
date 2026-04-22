"""
Módulo para la gestión y conteo de tokens utilizando librerías de Hugging Face.
Este módulo permite realizar el conteo de forma local sin depender de APIs externas.
"""
from transformers import AutoTokenizer

class ContadorTokens:
    """
    Interfaz para el conteo de tokens utilizando modelos de Hugging Face.
    
    Atributos:
        tokenizer: Instancia del tokenizador cargado.
    """
    def __init__(self, modelo_local: str = "gpt2"):
        """
        Inicializa el contador cargando un tokenizador específico.

        Args:
            modelo_local (str): Identificador del modelo o ruta local del tokenizador. 
                                Por defecto usa "gpt2".
        """
        try:
            # Esto carga el tokenizador localmente
            self.tokenizer = AutoTokenizer.from_pretrained(modelo_local)
        except Exception:
            # Fallback en caso de error
            self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

    def contar(self, texto: str) -> int:
        """
        Calcula la cantidad de tokens que contiene un texto.

        Args:
            texto (str): La cadena de texto a procesar.

        Returns:
            int: Número total de tokens.

        Raises:
            AttributeError: Si el texto proporcionado es None.
        """
        if texto is None:
            raise AttributeError("El texto no puede ser None")
        if not texto:
            return 0
        tokens = self.tokenizer.encode(texto)
        return len(tokens)