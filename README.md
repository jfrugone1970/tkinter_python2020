En este archivo vamos a explicar lo que tkinter en Python que es: La mayoría de ustedes escribe un código y lo ejecuta en una terminal de línea de comandos o un IDE (Entorno de desarrollo integrado), y el código produce una salida basada en lo que espera de él, ya sea en la terminal o en el IDE mismo. Sin embargo, ¿qué sucede si desea que su sistema tenga una interfaz de usuario elegante o tal vez su aplicación (caso de uso) requiera que tenga una GUI?

La GUI no es más que una aplicación de escritorio que le proporciona una interfaz que le ayuda a interactuar con las computadoras y enriquece su experiencia de dar un comando (entrada de línea de comandos) a su código. Se utilizan para realizar diferentes tareas en equipos de escritorio, portátiles y otros dispositivos electrónicos, etc.

Algunas de las aplicaciones donde se utiliza el poder de la GUI son:

- Crear una calculadora que tendría una interfaz de usuario y funcionalidades que persisten en una calculadora.
- Los editores de texto, IDE para codificación están en una aplicación GUI.
- Sudoku, Ajedrez, Solitario, etc., son juegos a los que puedes jugar y son aplicaciones GUI.
- Chrome, Firefox, Microsoft Edge, etc., que se utiliza para navegar por Internet es una aplicación GUI.

Veamos algunos de los marcos que proporciona Python para desarrollar una GUI:

- PyQT es uno de los enlaces de Python multiplataforma preferidos que implementan la biblioteca Qt para el marco de desarrollo de aplicaciones Qt. Nokia posee principalmente Qt. Actualmente, PyQT está disponible para casi todos los sistemas operativos como Unix / Linux, Windows, Mac OS X. Combina lo mejor de Python y Qt y brinda flexibilidad al programador para decidir si crear un programa escribiendo un código Python puro o usarlo. Qt Designer para crear diálogos visuales.

- Kivy es para la creación de nuevas interfaces de usuario y es un marco acelerado OpenGL ES 2. Al igual que PyQt , Kivy también es compatible con casi todas las plataformas como Windows, MacOSX, Linux, Android, iOS. Es un marco de código abierto y viene con más de 20 widgets precargados en su kit de herramientas.

Jython es un puerto de Python para Java, que brinda a los scripts de Python un acceso perfecto a las bibliotecas de clases de Java en la máquina local.

- WxPython , inicialmente conocido como WxWindows (ahora como una biblioteca WxWidgets), es un contenedor de nivel abstracto de código abierto para la biblioteca GUI multiplataforma. Está implementado como un módulo de expansión de Python. Con WxPython, usted, como desarrollador, puede crear aplicaciones nativas para Windows, Mac OS y Unix.

- PyGUI es un marco multiplataforma de aplicaciones gráficas para Unix, Macintosh y Windows. En comparación con otros marcos de GUI, PyGUI es, con mucho, el más simple y liviano de todos, ya que la API está puramente sincronizada con Python. PyGUI inserta muy menos código entre la plataforma GUI y la aplicación Python; por lo tanto, la pantalla de la aplicación generalmente muestra la GUI natural de la plataforma.
¡Y finalmente, el marco que es la discusión para el tutorial de hoy Tkinter !

Tkinter comúnmente viene incluido con Python, usando Tk y es el marco de GUI estándar de Python. Es famoso por su simplicidad e interfaz gráfica de usuario. Es de código abierto y está disponible bajo la licencia de Python.

Tkinter : Tkinter es la interfaz de Python para el kit de herramientas de la GUI de Tk que se envía con Python. Buscaríamos esta opción en este capítulo.

wxPython : esta es una interfaz Python de código abierto para el kit de herramientas GUI wxWidgets. Puede encontrar un tutorial completo sobre WxPython aquí .

PyQt : también es una interfaz de Python para una popular biblioteca Qt GUI multiplataforma. TutorialsPoint tiene un muy buen tutorial sobre PyQt aquí .

JPython : JPython es un puerto de Python para Java, que brinda a los scripts de Python un acceso perfecto a las bibliotecas de clases de Java en la máquina local http://www.jython.org .

Veamos un primer ejemplo de ejercicio con uso de tkinter, en la que una ventana, que va a tener una geometry("1350x500"), se lo pasa por parametros a una clase que se va a llamar programa, que va a tener un constructor con el evento __init__(); va a inicializar los parametros de la ventana.

Va a tener 3 metodos (cargar, addTexto, mostrar). En cargar se va a especificar las propiedades de la ventana, y el icono de la ventana, addtexto (texto de la ventana), mostrar para mostrar la ventana (todos esto es una clase programa que se lo llama por medio de instanciar a la clase programa), que se pasa los valores y se llama al metodo mostrar

Programa "01-ventanas.py" (nota para el icono del bitmap debes de descargar un archivo de una carpeta específica de tipo .ico desde www.google.com)

# Tkinter_
# Es un módulo para crear interfaz gráficas de usuario
from tkinter import *
# Importamos la libreria de la ruta para comprobar donde
# esta el archivo de imagen
import os.path
# crear la lventa razi
class Programa:

    def __init__(self, title, icon, icon_alt, size, resizable):
        self.title = title
        self.icon = icon
        self.icon_alt = icon_alt
        self.size = size
        self.resizable = resizable
  
    def cargar(self):

        ventana = Tk()

        self.ventana = ventana
        # Titulo de la ventana
        ventana.title(self.title)


        #Comprobar si existe el archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(self.icon):
            ruta_icono = os.path.abspath(self.icon_alt)


        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)
        #Cambio tamaño de la ventana
        ventana.geometry(self.size)

        #Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)

        else:
            ventana.resizable(0,0)   

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()
    

# Instanciar mi programa mediante la clase
programa = Programa('Curso de Master en Python con Victor Robles','./imagenes/07_linkedin.ico','./21-tkinter/imagenes/07_linkedin.ico','1350x500',FALSE)
programa.cargar()
programa.addTexto("Hola! Soy Jose Fernando Frugone Jaramillo")
programa.addTexto("soy Lcdo en Informatica")
programa.addTexto("graduado en la Universidad de Guayaquil")
programa.addTexto("Facultad de Filosofia")
programa.addTexto("tambien realice estudio de Programacion de Microcomputadoras")
programa.addTexto("En la ESPOL")
programa.addTexto("tengo conocimiento de algunos lenguajes como Java, Laravel, Visual Basic.NET")
programa.addTexto("Fox fox, Visual Fox Pro 9, Python y otras herramientas")
programa.mostrar()

A continuación muestro una pantalla de la ejecución del programa "01-ventanas.py"








