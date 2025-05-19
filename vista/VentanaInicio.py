from vista.VentanaPrincipal import VentanaPrincipal
from controlador.Controlador import Controlador
import tkinter as tk

class VentanaInicio:
    def __init__(self, master):
        self.master = master
        self.master.title("Viveros El Zulia")
        self.master.attributes('-fullscreen', True)

        # Parte superior verde
        self.top_frame = tk.Frame(self.master, bg="#74b74b", height=100)
        self.top_frame.pack(fill=tk.X)

        self.titulo = tk.Label(self.top_frame, text="VIVEROS EL ZULIA", font=("Arial", 20), bg="#74b74b", fg="white")
        self.titulo.pack(pady=30)

        # Cuerpo central
        self.body_frame = tk.Frame(self.master, bg="white")
        self.body_frame.pack(fill=tk.BOTH, expand=True)

        self.lbl_inicio = tk.Label(self.body_frame, text="Iniciar Sesión", font=("Arial", 14), bg="white", bd=1, relief="solid", width=20)
        self.lbl_inicio.pack(pady=10)

        self.lbl_usuario = tk.Label(self.body_frame, text="Usuario", bg="#b4d7a8", width=20)
        self.lbl_usuario.pack(pady=5)
        self.txt_usuario = tk.Entry(self.body_frame, bd=1, relief="solid", width=30)
        self.txt_usuario.pack(pady=5)

        self.lbl_contra = tk.Label(self.body_frame, text="Contraseña", bg="#b4d7a8", width=20)
        self.lbl_contra.pack(pady=5)
        self.txt_contra = tk.Entry(self.body_frame, bd=1, relief="solid", show="*", width=30)
        self.txt_contra.pack(pady=5)

        self.btn_confirmar = tk.Button(self.body_frame, text="CONFIRMAR", bg="#74b74b", fg="white", width=15, height=1, command=self.abrirVentanaPrincipal)
        self.btn_confirmar.pack(pady=20)

        # Parte inferior amarilla
        self.bottom_frame = tk.Frame(self.master, bg="#fbbc04", height=40)
        self.bottom_frame.pack(fill=tk.X)

    def abrirVentanaPrincipal(self):
        self.master.destroy()
        nuevaRoot=tk.Tk()
        VentanaPrincipal(nuevaRoot)
        nuevaRoot.mainloop()