import tkinter as tk
from tkinter import ttk, messagebox
# Importamos la lógica refactorizada
from services.pipeline import PipelineCostes
from calculadora.proyecciones import ProcesadorCostes
from calculadora.precios import PRECIOS_MODELOS

class CalculadoraGUI:
    """
    Réplica de la interfaz corporativa corregida.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Costes de APIs de IA")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")

        # Fuentes
        self.font_bold = ("Segoe UI", 11, "bold")
        self.font_std = ("Segoe UI", 10)
        
        self.setup_ui()

    def setup_ui(self):
        # 1. Selector de Modelo
        tk.Label(self.root, text="Modelo de IA", bg="#f0f0f0", font=self.font_bold, fg="#444").pack(anchor="w", padx=30, pady=(20, 0))
        self.combo_modelo = ttk.Combobox(self.root, values=list(PRECIOS_MODELOS.keys()), state="readonly", font=self.font_std)
        self.combo_modelo.set("gpt-4o")
        self.combo_modelo.pack(fill="x", padx=30, pady=5)

        # 2. Entrada de Texto
        tk.Label(self.root, text="Texto a analizar", bg="#f0f0f0", font=self.font_bold, fg="#444").pack(anchor="w", padx=30, pady=(15, 0))
        self.txt_input = tk.Text(self.root, height=6, font=self.font_std, relief="flat", borderwidth=1)
        self.txt_input.pack(fill="x", padx=30, pady=5)

        # 3. Botonera
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(fill="x", padx=30, pady=20)

        # Botón Calcular (Enlazado correctamente)
        self.btn_calc = tk.Button(btn_frame, text="Calcular Costes", bg="#2c3e50", fg="white", 
                                  font=self.font_bold, relief="flat", width=15, 
                                  command=self.ejecutar_calculo)
        self.btn_calc.pack(side="left", padx=5)

        # Botón Limpiar
        self.btn_clear = tk.Button(btn_frame, text="Limpiar", bg="#7f8c8d", fg="white", 
                                   font=self.font_bold, relief="flat", width=10, 
                                   command=self.limpiar)
        self.btn_clear.pack(side="left", padx=5)

        # Botón Salir
        self.btn_exit = tk.Button(btn_frame, text="Salir", bg="#e74c3c", fg="white", 
                                  font=self.font_bold, relief="flat", width=10, 
                                  command=self.root.quit)
        self.btn_exit.pack(side="left", padx=5)

        # 4. Resultados: Tokens (Verde)
        self.frame_tokens = tk.LabelFrame(self.root, text=" ◊  Tokens ", bg="#dff2bf", font=self.font_bold, fg="#4f8a10", relief="flat")
        self.frame_tokens.pack(fill="x", padx=30, pady=10)
        
        self.lbl_tokens_in = tk.Label(self.frame_tokens, text="📥 Entrada: 0 tokens", bg="#dff2bf", font=self.font_std)
        self.lbl_tokens_in.pack(anchor="w", padx=10, pady=2)
        self.lbl_tokens_out = tk.Label(self.frame_tokens, text="📤 Salida (estimada): 200 tokens", bg="#dff2bf", font=self.font_std)
        self.lbl_tokens_out.pack(anchor="w", padx=10, pady=2)
        self.lbl_tokens_total = tk.Label(self.frame_tokens, text="📊 Total: 0 tokens", bg="#dff2bf", font=self.font_bold)
        self.lbl_tokens_total.pack(anchor="w", padx=10, pady=(2, 10))

        # 5. Resultados: Costes (Azul)
        self.frame_costes = tk.LabelFrame(self.root, text=" 🧮  Costes ", bg="#d9eaf7", font=self.font_bold, fg="#31708f", relief="flat")
        self.frame_costes.pack(fill="x", padx=30, pady=10)

        self.lbl_euro = tk.Label(self.frame_costes, text="💶 Euros:  0.000000 €", bg="#d9eaf7", font=self.font_std)
        self.lbl_euro.pack(anchor="w", padx=10, pady=2)
        self.lbl_dolar = tk.Label(self.frame_costes, text="💵 Dólar:  0.000000 $", bg="#d9eaf7", font=self.font_std)
        self.lbl_dolar.pack(anchor="w", padx=10, pady=2)
        self.lbl_cents = tk.Label(self.frame_costes, text="¢ Céntimos: 0.0000 cts", bg="#d9eaf7", font=self.font_std)
        self.lbl_cents.pack(anchor="w", padx=10, pady=(2, 10))

    def ejecutar_calculo(self):
        """
        Punto de enlace principal.
        Corregido el error de 'end-1.c' por tk.END
        """
        try:
            modelo_seleccionado = self.combo_modelo.get()
            # CORRECCIÓN AQUÍ: Usamos tk.END para evitar el error de índice
            texto_usuario = self.txt_input.get("1.0", tk.END).strip()

            if not texto_usuario:
                messagebox.showwarning("Atención", "Escribe un texto antes de calcular.")
                return

            # Llamada al Pipeline
            pipeline = PipelineCostes(modelo_ia=modelo_seleccionado)
            resultado = pipeline.procesar_texto(texto_usuario, "salida")
            
            # Datos para la función calcular_detallado(t_in, t_out)
            t_entrada = resultado["tokens"]["in"]
            t_salida = 200 # Valor fijo solicitado por la imagen corporativa
            
            # LLAMADA DIRECTA A TU FUNCIÓN EN proyecciones.py
            # Asegúrate que el objeto se llama 'procesador' en tu Pipeline
            datos_finales = pipeline.procesador.calcular_detallado(t_in=t_entrada, t_out=t_salida)
            
            # ACTUALIZACIÓN DE LA INTERFAZ
            self.lbl_tokens_in.config(text=f"📥 Entrada: {t_entrada} tokens")
            self.lbl_tokens_out.config(text=f"📤 Salida (estimada): {t_salida} tokens")
            self.lbl_tokens_total.config(text=f"📊 Total: {t_entrada + t_salida} tokens")
            
            dolar = datos_finales["total_usd"]
            euro = dolar * 0.92 
            
            self.lbl_dolar.config(text=f"💵 Dólar:  {dolar:.6f} $")
            self.lbl_euro.config(text=f"💶 Euros:  {euro:.6f} €")
            self.lbl_cents.config(text=f"¢ Céntimos: {datos_finales['total_cent']:.4f} cts")

        except Exception as e:
            messagebox.showerror("Error de Procesamiento", f"No se pudo completar el cálculo: {str(e)}")

    def limpiar(self):
        self.txt_input.delete("1.0", tk.END)
        self.lbl_tokens_in.config(text="📥 Entrada: 0 tokens")
        self.lbl_tokens_total.config(text="📊 Total: 0 tokens")
        self.lbl_dolar.config(text="💵 Dólar:  0.000000 $")
        self.lbl_euro.config(text="💶 Euros:  0.000000 €")
        self.lbl_cents.config(text="¢ Céntimos: 0.0000 cts")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()