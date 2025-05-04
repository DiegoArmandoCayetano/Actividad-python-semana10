from tkinter import *
from clase_modulo_cliente import ModuloCliente
from clase_modulo_producto import ModuloProducto

ventana = Tk()
ventana.title("Gestión de Tienda")
ventana.geometry("300x200")

Button(ventana, text="Clientes", command=ModuloCliente).pack(pady=10)
Button(ventana, text="Productos", command=ModuloProducto).pack(pady=10)

ventana.mainloop()
