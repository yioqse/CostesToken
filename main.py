# main.py
from services.pipeline import PipelineCostes
from interface.presenter import VisualizadorConsola

def run():
    # Configuración del Pipeline
    pipeline = PipelineCostes(modelo_ia="gpt-4o-mini")
    ui = VisualizadorConsola()

    # Datos de entrada
    prompt = "Genera un resumen de este código refactorizado."
    respuesta = "El código ha sido modularizado siguiendo principios SOLID..."

    # Ejecución del Pipeline
    resultado = pipeline.procesar_texto(prompt, respuesta)
    
    # Presentación
    ui.mostrar_reporte(resultado)

    # Ejemplo de extensibilidad: Comparar múltiples modelos rápidamente
    comparativa = []
    for m in ["gpt-4o", "gpt-4o-mini", "claude-3-sonnet"]:
        pipe = PipelineCostes(modelo_ia=m)
        res = pipe.procesar_texto(prompt, respuesta)
        comparativa.append({"nombre": m, "data": res})
    
    ui.mostrar_comparativa(comparativa)

if __name__ == "__main__":
    run()