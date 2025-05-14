import tkinter as tk
from tkinter import ttk

class VentanaVerInvernaderos:
  def __init__(self,master):
    self.master=master
    self.master.title("Lista de Invernaderos")
    self.master.geometry("900x500")
    self.master.configure(bg="white")

  # Título
  titulo = tk.Label(master, text="INVERNADEROS REGISTRADOS", font=("Arial", 18, "bold"), bg="white", fg="green")
  titulo.pack(pady=10)

  # Se crea una tabla para visualizar los invernaderos
  self.tree = ttk.Treeview(master, columns=("nombre", "superficie", "cultivo", "fecha", "responsable", "capacidad", "riego"), show="headings")
  self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

  # Encabezados de la tabla con sus dimensiones
  encabezados = ["Nombre", "Superficie", "Tipo de Cultivo", "Fecha", "Responsable", "Capacidad", "Sistema de Riego"]
  for i, col in enumerate(self.tree["columns"]):
    self.tree.heading(col, text=encabezados[i])
    self.tree.column(col, anchor="center", width=120)

  # Cargar datos
  self.cargar_datos()

  # Botón cerrar
  btn_cerrar = tk.Button(master, text="Cerrar", command=master.destroy, bg="red", fg="white", font=("Arial", 12))
  btn_cerrar.pack(pady=10)
  
  self.cargarDatos(self):
    conexion = Conexion()
    invernaderos = conexion.obtenerInvernaderos()

  for inv in invernaderos:
    self.tree.insert("", tk.END, values=(
      inv.nombre,
      inv.superficie,
      inv.tipo_cultivo,
      inv.fecha_creacion,
      inv.responsable,
      inv.capacidad,
      inv.sistema_riego
        ))
