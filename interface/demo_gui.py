import tkinter as tk
from tkinter import ttk, messagebox
from services.pipeline import PipelineCostes
from calculadora.precios import PRECIOS_MODELOS

class CalculadoraGUI:
    """
    Réplica de la interfaz de usuario para la Calculadora de Costes de IA.
    Conecta la lógica de Transformers local con una interfaz gráfica moderna.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Costes de APIs de IA")
        self.root.geometry("650x750")
        self.root.configure(bg="#ececec")

        # Configuración de estilos y fuentes
        self.font_title = ("Segoe UI", 12, "bold")
        self.font_label = ("Segoe UI", 11)
        self.font_result = ("Consolas", 11)
        
        self.setup_ui()

    def setup_ui(self):
        """Define la estructura visual de la aplicación."""
        
        # --- SECCIÓN: MODELO DE IA ---
        tk.Label(self.root, text="Modelo de IA", bg="#ececec", font=self.font_title, fg="#555").pack(anchor="w", padx=30, pady=(20, 5))
        self.combo_modelo = ttk.Combobox(self.root, values=list(PRECIOS_MODELOS.keys()), state="readonly", font=self.font_label)
        self.combo_modelo.set("gpt-4o")
        self.combo_modelo.pack(fill="x", padx=30, pady=5)

        # --- SECCIÓN: TEXTO A ANALIZAR ---
        tk.Label(self.root, text="Texto a analizar", bg="#ececec", font=self.font_title, fg="#555").pack(anchor="w", padx=30, pady=(15, 5))
        self.txt_input = tk.Text(self.root, height=5, font=self.font_label, relief="flat", padx=10, pady=10)
        self.txt_input.pack(fill="x", padx=30, pady=5)

        # --- SECCIÓN: BOTONES ---
        btn_frame = tk.Frame(self.root, bg="#ececec")
        btn_frame.pack(fill="x", padx=30, pady=20)

        # Botón Calcular
        btn_calc = tk.Button(btn_frame, text="Calcular Costes", bg="#2c3e50", fg="white", 
                             font=self.font_title, relief="flat", width=15, command=self.ejecutar_calculo)
        btn_calc.pack(side="left", padx=5)

        # Botón Limpiar
        btn_clear = tk.Button(btn_frame, text="Limpiar", bg="#7f8c8d", fg="white", 
                              font=self.font_title, relief="flat", width=12, command=self.limpiar)
        btn_clear.pack(side="left", padx=5)

        # Botón Salir
        btn_exit = tk.Button(btn_frame, text="Salir", bg="#e74c3c", fg="white", 
                             font=self.font_title, relief="flat", width=12, command=self.root.quit)
        btn_exit.pack(side="left", padx=5)

        # --- RESULTADOS: TOKENS (Fondo Verde) ---
        self.frame_tokens = tk.LabelFrame(self.root, text=" ◊  Tokens ", bg="#dff2bf", font=self.font_title, fg="#4f8a10", relief="flat")
        self.frame_tokens.pack(fill="x", padx=30, pady=10)
        
        self.lbl_tokens_in = tk.Label(self.frame_tokens, text="📥 Entrada: 0 tokens", bg="#dff2bf", font=self.font_label)
        self.lbl_tokens_in.pack(anchor="w", padx=10, pady=2)
        self.lbl_tokens_out = tk.Label(self.frame_tokens, text="📤 Salida (estimada): 200 tokens", bg="#dff2bf", font=self.font_label)
        self.lbl_tokens_out.pack(anchor="w", padx=10, pady=2)
        self.lbl_tokens_total = tk.Label(self.frame_tokens, text="📊 Total: 0 tokens", bg="#dff2bf", font=self.font_label, fg="#333")
        self.lbl_tokens_total.pack(anchor="w", padx=10, pady=(2, 10))

        # --- RESULTADOS: COSTES (Fondo Azul) ---
        self.frame_costes = tk.LabelFrame(self.root, text=" 🧮  Costes ", bg="#d9eaf7", font=self.font_title, fg="#31708f", relief="flat")
        self.frame_costes.pack(fill="x", padx=30, pady=10)

        self.lbl_euro = tk.Label(self.frame_costes, text="💶 Euros:  0.000000 €", bg="#d9eaf7", font=self.font_label)
        self.lbl_euro.pack(anchor="w", padx=10, pady=2)
        self.lbl_dolar = tk.Label(self.frame_costes, text="💵 Dólar:  0.000000 $", bg="#d9eaf7", font=self.font_label)
        self.lbl_dolar.pack(anchor="w", padx=10, pady=2)
        self.lbl_cents = tk.Label(self.frame_costes, text="¢ Céntimos: 0.0000 cts", bg="#d9eaf7", font=self.font_label)
        self.lbl_cents.pack(anchor="w", padx=10, pady=(2, 10))

    def ejecutar_calculo(self):
        """Lógica para conectar con el Pipeline de Transformers."""
        try:
            modelo = self.combo_modelo.get()
            texto = self.txt_input.get("1.0", "end-1.c")
            
            if not texto.strip():
                messagebox.showwarning("Atención", "Por favor, introduce algún texto para analizar.")
                return

            # Instanciar el pipeline con el modelo seleccionado
            pipeline = PipelineCostes(modelo_ia=modelo)
            
            # Simulamos una salida de 200 tokens como en la imagen corporativa
            resultado = pipeline.procesar_texto(texto, "Simulación de respuesta de salida")
            # Ajustamos la salida a 200 tokens fijos para cumplir con el requisito visual de la demo
            t_in = resultado["tokens"]["in"]
            t_out = 200 
            
            # Recalcular costes con los tokens finales
            eco = pipeline.procesador.calcular_detallado(t_in, t_out)
            
            # Actualizar Interfaz
            self.lbl_tokens_in.config(text=f"📥 Entrada: {t_in} tokens")
            self.lbl_tokens_out.config(text=f"📤 Salida (estimada): {t_out} tokens")
            self.lbl_tokens_total.config(text=f"📊 Total: {t_in + t_out} tokens")
            
            # Conversión simple a Euro (ejemplo 0.92)
            dolares = eco["total_usd"]
            euros = dolares * 0.92
            
            self.lbl_dolar.config(text=f"💵 Dólar:  {dolares:.6f} $")
            self.lbl_euro.config(text=f"💶 Euros:  {euros:.6f} €")
            self.lbl_cents.config(text=f"¢ Céntimos: {eco['total_cent']:.4f} cts")

        except Exception as e:
            messagebox.showerror("Error", f"Hubo un fallo en el procesamiento local: {str(e)}")

    def limpiar(self):
        """Limpia los campos de entrada y resultados."""
        self.txt_input.delete("1.0", "end")
        self.lbl_tokens_in.config(text="📥 Entrada: 0 tokens")
        self.lbl_tokens_total.config(text="📊 Total: 0 tokens")
        self.lbl_dolar.config(text="💵 Dólar:  0.000000 $")
        self.lbl_euro.config(text="💶 Euros:  0.000000 €")
        self.lbl_cents.config(text="¢ Céntimos: 0.0000 cts")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()