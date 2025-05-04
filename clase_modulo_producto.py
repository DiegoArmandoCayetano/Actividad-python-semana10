from tkinter import *
from tkinter import messagebox
from clase_conexion import conexion

class ModuloProducto:
    def __init__(self):
        self.con = conexion().hacer_conexion()
        self.ventana = Toplevel()
        self.ventana.title("Modulo Productos")
        self.ventana.geometry("400x500")

        Label(self.ventana, text="Nombre").pack()
        self.nombre = Entry(self.ventana)
        self.nombre.pack()

        Label(self.ventana, text="Precio").pack()
        self.precio = Entry(self.ventana)
        self.precio.pack()

        Label(self.ventana, text="Stock").pack()
        self.stock = Entry(self.ventana)
        self.stock.pack()

        Label(self.ventana, text="Categoría").pack()
        self.categoria = Entry(self.ventana)
        self.categoria.pack()

        Button(self.ventana, text="Guardar", command=self.guardar_producto).pack(pady=5)
        Button(self.ventana, text="Valor total inventario", command=self.total_inventario).pack(pady=5)
        Button(self.ventana, text="Valor por categoría", command=self.valor_categoria).pack(pady=5)
        Button(self.ventana, text="Productos con bajo stock", command=self.stock_bajo).pack(pady=5)

    def guardar_producto(self):
        cursor = self.con.cursor()
        query = "INSERT INTO producto(nombre, precio, stock, categoria) VALUES (%s, %s, %s, %s)"
        valores = (self.nombre.get(), self.precio.get(), self.stock.get(), self.categoria.get())
        cursor.execute(query, valores)
        self.con.commit()
        messagebox.showinfo("Info", "Producto guardado")

    def total_inventario(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT SUM(precio * stock) FROM producto")
        total = cursor.fetchone()[0]
        messagebox.showinfo("Total Inventario", f"Total: {total}")

    def valor_categoria(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT categoria, SUM(precio * stock) FROM producto GROUP BY categoria")
        resultados = cursor.fetchall()
        mensaje = ""
        for cat, val in resultados:
            mensaje += f"{cat}: {val}\n"
        messagebox.showinfo("Valor por Categoría", mensaje)

    def stock_bajo(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT nombre, stock FROM producto WHERE stock < 5")
        productos = cursor.fetchall()
        mensaje = ""
        for nom, stk in productos:
            mensaje += f"{nom} - Stock: {stk}\n"
        messagebox.showinfo("Stock Bajo", mensaje)
