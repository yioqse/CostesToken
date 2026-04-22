# main.py
from calculadora.tokens import ContadorTokens
from calculadora.proyecciones import ProcesadorCostes
from calculadora.precios import PRECIOS_MODELOS

def ejecutar_analisis():
    print("=" * 60)
    print("SISTEMA DE ANÁLISIS DE COSTES (REFACTORIZADO - LOCAL)")
    print("=" * 60)

    # 1. Inicializar componentes
    tokenizador = ContadorTokens() # Local con Transformers
    
    # 2. Ejemplo: Análisis de una consulta real
    pregunta = "¿Cuál es el presupuesto para el proyecto de IA local?"
    respuesta = "El presupuesto estimado depende de la infraestructura y el modelo elegido."
    
    modelo_a_testear = "gpt-4o-mini"
    procesador = ProcesadorCostes(modelo_a_testear)
    
    t_in = tokenizador.contar(pregunta)
    t_out = tokenizador.contar(respuesta)
    
    coste = procesador.calcular_detallado(t_in, t_out)
    
    print(f"\n[Modelo: {modelo_a_testear}]")
    print(f"Tokens detectados (Local): Input {t_in}, Output {t_out}")
    print(f"Coste de la operación: ${coste['total_usd']:.6f}")

    # 3. Ejemplo: Proyección Mensual
    print("\n[Proyección Mensual - Chatbot]")
    proyeccion = procesador.proyeccion_mensual(llamadas_dia=100, t_in=200, t_out=300)
    print(f"Llamadas al mes: {proyeccion['llamadas_totales']}")
    print(f"Gasto estimado: ${proyeccion['total_usd']:.2f} USD")

    # 4. Comparativa de modelos
    print("\n" + "-" * 30)
    print("COMPARATIVA RÁPIDA DE MODELOS")
    for mod in ["gpt-4o", "gpt-4o-mini", "claude-3-sonnet"]:
        p = ProcesadorCostes(mod).proyeccion_mensual(100, 200, 300)
        print(f"{mod.ljust(15)}: ${p['total_usd']:.2f}/mes")

if __name__ == "__main__":
    ejecutar_analisis()