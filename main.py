from modelo.Conexion import crear_tablas
import tkinter as tk
from vista.VentanaInicio import VentanaInicio

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaInicio(root)
    crear_tablas()
    root.mainloop()
