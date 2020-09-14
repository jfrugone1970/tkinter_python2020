# Cargamos la libreria de tkinter
from tkinter import *
import os.path

ventana = Tk()

ventana.geometry("800x400")

ventana.title("Ejercicia 11 | Lcdo. Jose Fernando Frugone Jaramillo")

ruta_imagen = os.path.abspath('./imagenes/rostro.ico')

if not os.path.isfile(ruta_imagen):
    ruta_imagen = os.path.abspath('./21-tkinter/imagenes/rostro.ico')

ventana.iconbitmap(ruta_imagen)

# Encabezado
encabezado = Label(ventana, text="Formulario 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Tahoma",14)
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=N)

texto = Label(ventana, text="A que te dedicas?")
texto.config(
    bg="green",
    fg="red",
    font=("Tahoma",10)
)
texto.grid(row=1, column=0, sticky=N)




# Botones check
def mostrarProfesion():
    texto = ""

    if web.get():
        texto += "Desarrollo web"

    if mobil.get():
        if web.get():
            texto += "\n"
            texto += "y Desarrollo mobil"
        else:
            texto += "Desarrollo mobil"    


    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
        )    

web = IntVar()
mobil = IntVar()

Checkbutton(
    ventana,
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
    ).grid(row=2, column=0)
Checkbutton(
    ventana,
    text="Desarrollo mobil",
    variable=mobil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
    ).grid(row=3, column=0)


mostrar = Label(ventana, text="", bg="green")
mostrar.grid(row=4, column=0)

# Radio Botton
def marcar():
    marcado.config(
        text=opcion1.get(),
        bg="green",
        fg="white",
        font=("Tahoma",10)
    )


opcion1 = StringVar()
opcion1.set(None)
texto = Label(ventana, text="Cual es tu genero?")
texto.config(
    bg="green",
    fg="red",
    font=("Tahoma",10)
)
texto.grid(row=5, column=0, sticky=N)

Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion1,
    command=marcar
    ).grid(row=6)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion1,
    command=marcar
    ).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8, column=0)


# Option Menu
def escoger():
    escogido.config(
        text=opcion.get(),
        bg="green",
        fg="white",
        font=("Tahoma",10)
    )

opcion = StringVar()


texto = Label(ventana, text="Selecciona una opcion")
texto.config(
    bg="red",
    fg="green",
    font=("Tahoma",12)
)
texto.grid(row=10, column=1)

selecciona = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
selecciona.grid(row=11, column=1)

escogido = Label(ventana)
boton = Button(ventana, text="ver",command=escoger)
boton.config(
    bg="green",
    fg="white",
    font=("Tahoma",10)
)
boton.grid(row=12, column=1)
escogido.grid(row=13, column=1)


ventana.mainloop()
