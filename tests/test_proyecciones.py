from calculadora.proyecciones import CalculadoraCostes

def test_calculo_basico():
    calc = CalculadoraCostes("gpt-4o-mini")
    resultado = calc.calcular_costes(1000000, 1000000)
    assert resultado["coste_total_usd"] == 0.75 # 0.15 + 0.60