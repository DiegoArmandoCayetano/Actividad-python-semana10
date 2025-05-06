from vista.VentanaCuestionario import VentanaCuestionario
import tkinter as tk
from tkinter import ttk

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana Principal")
        self.master.attributes('-fullscreen', True)

        # Parte superior verde
        self.top_frame = tk.Frame(self.master, bg="#74b74b", height=100)
        self.top_frame.pack(fill=tk.X)
        
        # Frame para el botón de cierre (esquina superior derecha)
        self.close_frame = tk.Frame(self.top_frame, bg="red", width=50, height=50)
        self.close_frame.place(x=self.master.winfo_width() - 60, y=10)  # Coloca el botón en la esquina superior derecha
        
        # Botón de cierre (X)
        self.btn_close = tk.Button(self.close_frame, text="X", bg="red", fg="white", font=("Arial", 16), command=self.master.destroy)
        self.btn_close.pack(fill=tk.BOTH, expand=True)

        # Menú de navegación simulado con botones
        self.menu_frame = tk.Frame(self.master, bg="#f5f5dc")
        self.menu_frame.pack(fill=tk.X, pady=10)

        botones = ["Control invernaderos", "Control de humedad", "Control de piso", "Enfermedades"]
        for texto in botones:
            btn = tk.Button(self.menu_frame, text=texto, bg="#f5f5dc", relief="groove", borderwidth=1)
            btn.pack(side=tk.LEFT, padx=2, pady=5)

        # Combobox de filtro
        self.filtro_frame = tk.Frame(self.master, bg="white")
        self.filtro_frame.pack(fill=tk.X, padx=10, pady=10, anchor="w")

        tk.Label(self.filtro_frame, text="Filtrar:", font=("Arial", 10)).pack(side=tk.LEFT, padx=(10, 5))
        self.combo = ttk.Combobox(self.filtro_frame, values=["Invernaderos", "Sensores", "Zonas"])
        self.combo.current(0)
        self.combo.pack(side=tk.LEFT)

        # Marcos vacíos con bordes verdes
        self.marcos_frame = tk.Frame(self.master, bg="white")
        self.marcos_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        marco1 = tk.LabelFrame(self.marcos_frame, bg="white", highlightbackground="green", highlightcolor="green", highlightthickness=2)
        marco1.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.5)

        marco2 = tk.LabelFrame(self.marcos_frame, bg="white", highlightbackground="green", highlightcolor="green", highlightthickness=2)
        marco2.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.5)

        # Parte inferior amarilla (opcional)
        self.bottom_frame = tk.Frame(self.master, bg="#fbbc04", height=40)
        self.bottom_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.btn_confirmar = tk.Button(self.master, text="REGISTRAR INVERNADERO", bg="#74b74b", fg="white", width=25, height=1, command=self.abrirVentanaCuestionario)
        self.btn_confirmar.pack(pady=20)
        
    def abrirVentanaCuestionario(self):
        self.master.destroy()
        rootVentanaFormulario=tk.Tk()
        VentanaCuestionario(rootVentanaFormulario)
        rootVentanaFormulario.mainloop()