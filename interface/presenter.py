# interface/presenter.py

class VisualizadorConsola:
    @staticmethod
    def mostrar_reporte(resultado: dict):
        print("\n" + "·" * 40)
        print("📊 REPORTE DE PIPELINE")
        print(f"Tokens: {resultado['tokens']['in']} (in) | {resultado['tokens']['out']} (out)")
        print(f"Coste Total: ${resultado['economia']['total_usd']:.6f}")
        print("·" * 40)

    @staticmethod
    def mostrar_comparativa(lista_resultados: list):
        print("\n📈 COMPARATIVA DE ESCENARIOS")
        for r in lista_resultados:
            print(f"- {r['nombre']}: ${r['data']['economia']['total_usd']:.4f}")