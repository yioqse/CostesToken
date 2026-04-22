# calculadora/proyecciones.py
from .precios import PRECIOS_MODELOS

class ProcesadorCostes:
    def __init__(self, modelo: str):
        self.precios = PRECIOS_MODELOS.get(modelo, PRECIOS_MODELOS["gpt-4o-mini"])

    def calcular_detallado(self, t_in: int, t_out: int) -> dict:
        coste_in = (t_in / 1_000_000) * self.precios["input"]
        coste_out = (t_out / 1_000_000) * self.precios["output"]
        total = coste_in + coste_out
        return {
            "total_usd": total,
            "total_cent": total * 100,
            "in_usd": coste_in,
            "out_usd": coste_out
        }

    def proyeccion_mensual(self, llamadas_dia: int, t_in: int, t_out: int, dias: int = 30):
        total_llamadas = llamadas_dia * dias
        total_in = t_in * total_llamadas
        total_out = t_out * total_llamadas
        
        resultado = self.calcular_detallado(total_in, total_out)
        resultado["llamadas_totales"] = total_llamadas
        resultado["coste_por_llamada"] = resultado["total_usd"] / total_llamadas
        return resultado