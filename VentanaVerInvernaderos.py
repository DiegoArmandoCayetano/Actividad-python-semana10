import tkinter as tk
from tkinter import ttk
from controlador.Controlador import Controlador

class VentanaVerInvernaderos(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True, fill=tk.BOTH)

        self.tabla = ttk.Treeview(self, columns=(
            "ID", "Nombre", "Capacidad", "Superficie", "Riego", "Cultivo", "Fecha", "Responsable"
        ), show="headings")

        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor=tk.CENTER)

        self.tabla.pack(expand=True, fill=tk.BOTH)

        self.controlador = Controlador()
        self.controlador.cargar_invernaderos()
        self.mostrar_datos()

    def mostrar_datos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for inv in self.controlador.listado.obtener_todos():
            self.tabla.insert("", "end", values=(
                inv.id_invernadero,
                inv.nombre,
                inv.capacidad,
                inv.superficie,
                inv.riego,
                inv.cultivo,
                inv.fecha,
                inv.responsable
            ))
