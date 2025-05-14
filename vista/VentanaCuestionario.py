import tkinter as tk
from tkinter import ttk
import vista.VentanaVerInvernaderos from VentanaVerInvernaderos

class VentanaCuestionario:
    def __init__(self, master):
        self.master = master
        self.master.title("Registrar Invernadero")
        self.master.attributes('-fullscreen', True)  # Hacer la ventana en pantalla completa
        self.master.configure(bg="white")
        self.btn_guardar.config(comand=self.guardarDatos)

        # Parte superior verde
        self.top_frame = tk.Frame(self.master, bg="#74b74b", height=100)
        self.top_frame.pack(fill=tk.X, side=tk.TOP)

        # Actualizar tareas para que el tamaño de la ventana se considere
        self.top_frame.update_idletasks()

        # Frame para el botón de cierre (esquina superior derecha)
        self.close_frame = tk.Frame(self.top_frame, bg="red", width=50, height=50)
        # Ajustamos la posición del botón "X"
        self.close_frame.place(x=self.master.winfo_width() - 60, y=10)

        # Botón de cierre (X)
        self.btn_close = tk.Button(self.close_frame, text="X", bg="red", fg="white", font=("Arial", 16), command=self.master.destroy)
        self.btn_close.pack(fill=tk.BOTH, expand=True)

        # Título
        self.titulo = tk.Label(self.top_frame, text="FORMULARIO DE INVERNADEROS", font=("Arial", 20), bg="#74b74b", fg="white")
        self.titulo.pack(pady=30)
        
        # Frame principal para los formularios
        self.frame = tk.Frame(self.master, bg="white")
        self.frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Nombre del invernadero
        tk.Label(self.frame, text="Nombre del invernadero", bg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_nombre = tk.Entry(self.frame, width=30, bd=2, relief="groove")
        self.entry_nombre.grid(row=1, column=0, padx=10, pady=5)

        # Capacidad de producción
        tk.Label(self.frame, text="Capacidad de producción", bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=5)
        self.entry_capacidad = tk.Entry(self.frame, width=30, bd=2, relief="groove")
        self.entry_capacidad.grid(row=1, column=1, padx=10, pady=5)

        # Superficie
        tk.Label(self.frame, text="Superficie (m²)", bg="white").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.entry_superficie = tk.Entry(self.frame, width=30, bd=2, relief="groove")
        self.entry_superficie.grid(row=3, column=0, padx=10, pady=5)

        # Sistema de riego
        tk.Label(self.frame, text="Sistema de riego", bg="white").grid(row=2, column=1, sticky="w", padx=10, pady=5)
        self.combo_riego = ttk.Combobox(self.frame, values=["Manual", "Automatizado", "Por goteo"], width=28)
        self.combo_riego.grid(row=3, column=1, padx=10, pady=5)

        # Tipo de cultivo
        tk.Label(self.frame, text="Tipo de cultivo", bg="white").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.combo_cultivo = ttk.Combobox(self.frame, values=["Flores", "Hortalizas", "Frutas"], width=28)
        self.combo_cultivo.grid(row=5, column=0, padx=10, pady=5)

        # Fecha de creación
        tk.Label(self.frame, text="Fecha de creación", bg="white").grid(row=4, column=1, sticky="w", padx=10, pady=5)
        self.entry_fecha = tk.Entry(self.frame, width=30, bd=2, relief="groove")
        self.entry_fecha.grid(row=5, column=1, padx=10, pady=5)

        # Responsable del invernadero
        tk.Label(self.frame, text="Responsable del invernadero", bg="white").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.entry_responsable = tk.Entry(self.frame, width=30, bd=2, relief="groove")
        self.entry_responsable.grid(row=7, column=0, padx=10, pady=5)

        # Botones
        self.btn_guardar = tk.Button(self.frame, text="Guardar", bg="green", fg="white", width=10)
        self.btn_guardar.grid(row=8, column=0, pady=20)

        self.btn_cancelar = tk.Button(self.frame, text="Cancelar", bg="red", fg="white", width=10)
        self.btn_cancelar.grid(row=8, column=1, pady=20)

        # Parte inferior amarilla
        self.bottom_frame = tk.Frame(self.master, bg="#fbbc04", height=40)
        self.bottom_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.btn_confirmar = tk.Button(self.master, text="REGRESAR", bg="#74b74b", fg="white", width=25, height=1, command=self.abrirVentanaPrincipal)
        self.btn_confirmar.pack(pady=20)

        self.btn_ver = tk.Button(self.frame, text="Ver Invernaderos", bg="blue", fg="white", command=self.abrir_lista_invernaderos)
        self.btn_ver.grid(row=9, column=0, pady=10)

    
    def abrir_lista_invernaderos(self):
        from vista.VentanaVerInvernaderos import VentanaVerInvernaderos
        nueva_ventana = tk.Toplevel(self.master)
        VentanaVerInvernaderos(nueva_ventana)


    def abrirVentanaPrincipal(self):
        # ✅ Importación local con acceso por módulo (evita ImportError por ciclo)
        import vista.VentanaPrincipal
        self.master.destroy()
        rootVentanaPrincipal = tk.Tk()
        vista.VentanaPrincipal.VentanaPrincipal(rootVentanaPrincipal)  # uso completo del nombre del módulo
        rootVentanaPrincipal.mainloop()

    def guardarDatos(self):
        datos=[
        self.entry_nombre.get(),
        self.entry_capacidad.get(),
        self.combo_cultivo.get(),
        self.entry_fecha.get(),
        self.entry_responsable.get(),
        self.entry_capacidad.get(),
        self.combo_riego.get()
        ]
        conexion= Conexion()
        conexion.registrarInvernadero(datos)
