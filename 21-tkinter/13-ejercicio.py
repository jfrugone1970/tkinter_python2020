"""
Crear un programa que tenga:
- (hecho) Ventana
- (hecho) Tamaño Fijo
- (hecho) No redimensionable
- (hecho) Un menu (Inicio, Anadir, Info, Salir)
- (hecho) Diferentes pantallas
- (hecho) Formulario de anadir productos
- (hecho) Guardar datos temporalmente
- Mostrar los datos listados en la pantalla home
- (hecho) Opcion de salir

"""
# Crear la ventana
from tkinter import *
from tkinter import ttk
import os.path

ventana = Tk()

# icono de la ventana
icono_ventana = os.path.abspath('./imagenes/rostro.ico')

if not os.path.isfile(icono_ventana):
    icono_ventana = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(icono_ventana)

# Tamano fijo
#ventana.geometry("700x500")
ventana.minsize(500, 500)

ventana.title("Proyecto tkinter en Python | Lcdo Jose Frugone")
# No redimensianable
ventana.resizable(0, 0)

# Menu superior
menu_superior = Menu(ventana)

ventana.config(
    menu=menu_superior,
    bg="#ccc",
    bd=50
)
# variable
productos = []
nombre = StringVar()
precio = StringVar()

# Definir campos de pantalla
home_label = Label(ventana, text="Inicio.....")
agrega_label = Label(ventana, text="Agregar producto...")
add_informa = Label(ventana, text="Realizado por Lcdo. Jose Fernando Frugone Jaramillo / 2020")
productos_box = Frame(ventana, width=250)
etiqueta_separa = Label(productos_box, text="--------------------------------")
add_listado = Label(productos_box, text="Listado de productos...")
# Defini campos para listado de productos
producto_tabla = ttk.Treeview(productos_box, height=12, columns=2)
producto_tabla.heading("#0",text='Producto',anchor=NW)
producto_tabla.heading("#1",text='Precio', anchor=NW)

# Anadir productos
def add_productos():
    productos.append([
        nombre.get(),
        precio.get(),
        add_descrip_entry.get("1.0", "end-1c")
    ])

    nombre.set("")
    precio.set("")
    add_descrip_entry.delete("1.0","end-1c")

      

# Anadir campos del formulario
add_frame = Frame(ventana, width=250)

add_name_label = Label(add_frame, text="Nombre del producto")
add_name_entry = Entry(add_frame, textvariable=nombre)

add_price_label = Label(add_frame, text="Precio")
add_price_entry = Entry(add_frame, textvariable=precio)

add_descrip_label = Label(add_frame, text="Descripcion del Producto")
add_descrip_entry = Text(add_frame)

add_separador = Label(add_frame, text="--------------------------------------------")

boton = Button(add_frame, text="Guardar", command=add_productos)

# Diferentes pantallas
def home():
    home_label.config(
        bg="black",
        fg="white",
        font=("Tahoma",15),
        padx=100,
        pady=20
    )
    home_label.grid(row=0, column=0, columnspan=2, sticky=W)

    productos_box.config(
        bg="green",
        bd=10,
        relief=SOLID,
        padx=20,
        pady=20
    )

    productos_box.grid(row=1, column=0, columnspan=2, sticky=W)
    etiqueta_separa.config(
        bg="white",
        fg="red",
        font=("Tahoma",10),
        padx=10,
        pady=10
    )

    etiqueta_separa.grid(row=2, column=0, sticky=NW)

    add_listado.config(
        bg="black",
        fg="white",
        font=("Tahoma",12),
        padx=10,
        pady=10
    )

    add_listado.grid(row=3, column=0, sticky=NW)

    producto_tabla.grid(row=4, column=0, columnspan=3, sticky=NW)

       
   # for producto in productos:
   #     if len(producto) == 3:
   #         Label(productos_box, text="Producto    : "+producto[0]).grid()
   #         Label(productos_box, text="Precio      : "+producto[1]).grid()
   #         Label(productos_box, text="Descripcion : "+producto[2]).grid()
   #         Label(productos_box, text="--------------------------").grid()

    for producto in productos:
        if len(producto) == 3:
            producto.append("added")
            producto_tabla.insert('',0,text=producto[0], values = producto[1])
            
   
    # Remover los otros campos
    agrega_label.grid_remove()
    add_name_label.grid_remove()
    add_informa.grid_remove()
    add_frame.grid_remove()
    add_name_entry.grid_remove()
    add_price_label.grid_remove()
    add_price_entry.grid_remove()
    add_descrip_label.grid_remove()
    add_descrip_entry.grid_remove()
    add_separador.grid_remove()
    boton.grid_remove()
        
    return True

def agrega():
    agrega_label.config(
        bg="black",
        fg="white",
        font=("Tahoma",15),
        padx=100,
        pady=20
    )
    agrega_label.grid(row=0, column=0, columnspan=2, sticky=W)
    # Anadir Marco
    add_frame.config(
        bg="white",
        bd=10,
        relief=SOLID,
        padx=25,
        pady=25
    )
    add_frame.grid(row=1, column=0, columnspan=2, sticky=NW)
    # campos del formulario
    add_name_label.config(
        bg="green",
        fg="white",
        font=("Tahoma",10)
    )
    add_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=NW)

    add_name_entry.grid(row=2, column=1, sticky=W)
    #Otro campo
    add_price_label.config(
        bg="green",
        fg="white",
        font=("Tahoma",10)
    )
    add_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)

    add_price_entry.grid(row=3, column=1, sticky=W)
    #Otro campo
    add_descrip_label.config(
        bg="green",
        fg="white",
        font=("Tahoma",10)
    )
    add_descrip_label.grid(row=4, column=0, padx=5, pady=5, sticky=NW)

    add_descrip_entry.config(
        width=30,
        height=5,
        bg="#ccc",
        fg="black",
        font=("Tahoma",10),
        padx=15,
        pady=15 
    )

    add_descrip_entry.grid(row=4, column=1, sticky=W)

    # Separador
    add_separador.config(
        bg="white",
        fg="red",
        font=("Tahoma",10),
        padx=10,
        pady=10
    )
    add_separador.grid(row=5, column=1, sticky=W)

    # Anadir boton
    boton.config(
        bg="cyan",
        fg="red",
        padx=15,
        pady=5,
        font=("Tahoma",10)
    )
    boton.grid(row=7, column=1, sticky=NW)

    home_label.grid_remove()
    add_listado.grid_remove()
    add_informa.grid_remove()
    productos_box.grid_remove()
    producto_tabla.grid_remove()
    etiqueta_separa.grid_remove()
    add_listado.grid_remove()
               
    return True


def info():
    # Remover las pantallas
    home_label.grid_remove()
    add_listado.grid_remove()
    productos_box.grid_remove()
    producto_tabla.grid_remove()
    etiqueta_separa.grid_remove()
    agrega_label.grid_remove()
    add_frame.grid_remove()
    add_name_label.grid_remove()
    add_name_entry.grid_remove()
    add_name_label.grid_remove()
    add_price_label.grid_remove()
    add_price_entry.grid_remove()
    add_descrip_label.grid_remove()
    add_descrip_entry.grid_remove()
    add_separador.grid_remove()
    boton.grid_remove()
  
    # Mostrar mensaje de quien lo realizo
    add_informa.config(
        bg="black",
        fg="white",
        font=("Arial",16),
        padx=20,
        pady=20
    )

    add_informa.grid(row=10, column=0, sticky=E)
    

# Cargar pantalla de inicio
home()


op = Menu(ventana, tearoff=0)
op.add_command(label="Inicio", command=home)
op.add_command(label="Anadir", command=agrega)
op.add_command(label="Info...", command=info)

fin = Menu(ventana, tearoff=0)
fin.add_command(label="Salir", command=ventana.quit)

menu_superior.add_cascade(label="Opciones", menu=op)
menu_superior.add_cascade(label="Terminar", menu=fin)


ventana.mainloop()
