from tkinter import *
from tkinter import messagebox
from clase_conexion import conexion

class ModuloCliente:
    def __init__(self):
        self.con = conexion().hacer_conexion()
        self.ventana = Toplevel()
        self.ventana.title("Modulo Clientes")
        self.ventana.geometry("400x400")

        Label(self.ventana, text="Nombre").pack()
        self.nombre = Entry(self.ventana)
        self.nombre.pack()

        Label(self.ventana, text="Apellidos").pack()
        self.apellidos = Entry(self.ventana)
        self.apellidos.pack()

        Label(self.ventana, text="Email").pack()
        self.email = Entry(self.ventana)
        self.email.pack()

        Label(self.ventana, text="Historial Compras").pack()
        self.historial = Entry(self.ventana)
        self.historial.pack()

        Button(self.ventana, text="Guardar", command=self.guardar_cliente).pack(pady=5)
        Button(self.ventana, text="Total compras clientes", command=self.total_compras).pack(pady=5)

    def guardar_cliente(self):
        cursor = self.con.cursor()
        query = "INSERT INTO cliente(nombre, apellidos, email, historial_compras) VALUES (%s, %s, %s, %s)"
        valores = (self.nombre.get(), self.apellidos.get(), self.email.get(), self.historial.get())
        cursor.execute(query, valores)
        self.con.commit()
        messagebox.showinfo("Info", "Cliente guardado")

    def total_compras(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT SUM(historial_compras) FROM cliente")
        total = cursor.fetchone()[0]
        messagebox.showinfo("Total Compras", f"Valor total: {total}")
