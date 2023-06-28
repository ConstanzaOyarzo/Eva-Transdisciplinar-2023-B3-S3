import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import re

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Trabajo mecanico")

# Obtener el tamaño de la pantalla
anPanta = ventana.winfo_screenwidth()
alPanta = ventana.winfo_screenheight()

anCuarto = anPanta // 2
alCuarto = alPanta // 2

# Crear los marcos para cada cuarto de la pantalla
marco_1 = tk.Frame(ventana, width=anCuarto, height=alCuarto, bg='#CC99FF')
marco_2 = tk.Frame(ventana, width=anCuarto, height=alCuarto)
marco_3 = tk.Frame(ventana, width=anCuarto, height=alCuarto, bg='#99CCFF')
marco_4 = tk.Frame(ventana, width=anCuarto, height=alCuarto, bg='#FFFF99')


marco_1.grid(row=0, column=0, sticky="nsew")
marco_2.grid(row=0, column=1, sticky="nsew")
marco_3.grid(row=1, column=0, sticky="nsew")
marco_4.grid(row=1, column=1, sticky="nsew")

# Configurar el peso de las filas y columnas en la cuadrícula
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)


############################################################################
info = tk.Label(marco_1, text="""Para calcular el trabajo, se necesita saber la fuerza y la desplazamiento y 
el calculo es el siguiente:
Trabajo = Fuerza * desplazamiento""")
info.pack(pady=40)

info2 = tk.Label(marco_1, text="""Presione las teclas 'a' y 'd' para aplicar trabajo
sobre la caja en pantalla""")
info2.pack()

info3 = tk.Label(marco_1, text="""PRECAUCION
Asegurese de no tener las letras mayusculas activadas
al operar el programa""")
info3.pack(pady=10)

############################################################################
#                               Caja
############################################################################

class Cajas:
    def __init__(self, marco_1): # self se utiliza para acceder y asignar atributos específicos a dicha instancia.

        # crea el cuadrado dentro del marco 1
        self.box = tk.Frame(marco_1, width=50, height=50, bg='#683343')
        self.box.pack()

    def limites(self):

        # Obtener las dimensiones del marco
        ancho_marco = marco_1.winfo_width()
        alto_marco = marco_1.winfo_height()

        # Calcular las nuevas coordenadas
        nueva_x = self.box.winfo_x()
        nueva_y = self.box.winfo_y()

        # Verificar los límites del rectángulo
        if 0 <= nueva_x <= ancho_marco - self.box.winfo_width():
            if 0 <= nueva_y <= alto_marco - self.box.winfo_height():
                self.box.place(x=nueva_x, y=nueva_y)

        marco_1.after(1, self.limites)

    def mover(self, velocidad_x, direccion_x):
        nueva_x = self.box.winfo_x() + (velocidad_x * direccion_x)
        nueva_y = self.box.winfo_y()

        self.box.place(x=nueva_x, y=nueva_y)


# Crear instancia de Cajas dentro del marco 1
caja1 = Cajas(marco_1)

# Establecer la posición inicial del cuadrado
caja1.box.place(x=anPanta//2//2, y=alPanta//2 - 55)


############################################################################
#                               Personaje
############################################################################
class Personajes:
    def __init__(self, imaP=None, caja=None):
        self.imaP_1 = imaP
        self.x = 0
        self.y = 0

        self.caja = caja

        self.velocidad_x = 5  # Velocidad en el eje x
        self.direccion_x = 1  # Dirección del movimiento (1 para derecha, -1 para izquierda)

        # Cargar las imágenes del personaje
        self.sprite_images = []
        for i in range(7):  # Numero de imágenes del personaje
            image_path = f"c{i}.png"
            image = Image.open(image_path).convert("RGBA")
            image = image.resize((50, 50))  # Ajustar el tamaño de la imagen
            self.sprite_images.append(ImageTk.PhotoImage(image))

        self.current_frame = 0  # Cuadro actual de la animación

        # Crear una etiqueta para mostrar la imagen del personaje
        self.etiqueta = tk.Label(self.imaP_1)
        self.etiqueta.config(bg='#CC99FF')
        self.etiqueta.place(x=anCuarto//2-70, y=alPanta//2 - 55)  # Colocar la etiqueta en la esquina superior izquierda de imaP_1

        # Configurar la imagen inicial del personaje
        self.etiqueta.config(image=self.sprite_images[0])

        self.move_enabled = False

        self.limites()

    def animate(self):
        if self.move_enabled:
            self.current_frame += 1
            if self.current_frame >= len(self.sprite_images):
                self.current_frame = 0

            self.etiqueta.config(image=self.sprite_images[self.current_frame])

        self.move_enabled = False
        self.imaP_1.after(2, self.animate)  # Cambiar el cuadro de la animación cada 100 milisegundos

    def limites(self):
        if self.move_enabled:
            # Obtener las dimensiones del marco
            ancho_marco = self.imaP_1.winfo_width()
            alto_marco = self.imaP_1.winfo_height()

            # Obtener las dimensiones del personaje y la caja
            ancho_personaje = self.etiqueta.winfo_width()
            alto_personaje = self.etiqueta.winfo_height()
            ancho_caja = self.caja.box.winfo_width()
            alto_caja = self.caja.box.winfo_height()

            # Calcular las nuevas coordenadas para el personaje
            nueva_x_personaje = self.etiqueta.winfo_x() + (self.velocidad_x * self.direccion_x)
            nueva_y_personaje = self.etiqueta.winfo_y() + self.y

            # Verificar los límites del personaje
            if 0 <= nueva_x_personaje <= ancho_marco - ancho_personaje - ancho_caja:
                if 0 <= nueva_y_personaje <= alto_marco - alto_personaje:
                    self.etiqueta.place(x=nueva_x_personaje, y=nueva_y_personaje)

            # Calcular las nuevas coordenadas para la caja
            nueva_x_caja = nueva_x_personaje + ancho_personaje
            nueva_y_caja = nueva_y_personaje

            # Verificar los límites de la caja
            if 0 <= nueva_x_caja <= ancho_marco - ancho_caja:
                if 0 <= nueva_y_caja <= alto_marco - alto_caja:
                    self.caja.box.place(x=nueva_x_caja, y=nueva_y_caja)

        self.move_enabled = False
        self.imaP_1.after(1, self.limites)

    # Movimiento a la izquierda
    def izquierda(self, event):
        self.velocidad_x = self.velocidad_x
        self.direccion_x = -1
        self.y = 0
        self.move_enabled = True

    # Movimiento a la derecha
    def derecha(self, event):
        self.velocidad_x = self.velocidad_x
        self.direccion_x = 1
        self.y = 0
        self.move_enabled = True


# Crear una instancia de la clase Personajes
per1 = Personajes(marco_1, caja1)

# Enlazar los eventos de teclado a los métodos de movimiento
ventana.bind("<KeyPress-a>", lambda e: per1.izquierda(e))
ventana.bind("<KeyPress-d>", lambda e: per1.derecha(e))
per1.animate()


############################################################################
#                               Tabla
############################################################################

# Crear el Treeview (tabla)
tabla = ttk.Treeview(marco_4)
tabla.pack(fill=tk.BOTH, expand=True)

# Definir las columnas de la tabla
tabla['columns'] = ("N°", "Fuerza", "Desplazamiento", "Trabajo")

# Formato de las columnas
tabla.column("#0", width=0, stretch=tk.NO)
tabla.column("N°", width=50, anchor=tk.CENTER)
tabla.column("Fuerza", width=100, anchor=tk.CENTER)
tabla.column("Desplazamiento", width=100, anchor=tk.CENTER)
tabla.column("Trabajo", width=100, anchor=tk.CENTER)

# Encabezados de las columnas
tabla.heading("#0", text="", anchor=tk.CENTER)
tabla.heading("N°", text="N°", anchor=tk.CENTER)
tabla.heading("Fuerza", text="Fuerza (N)", anchor=tk.CENTER)
tabla.heading("Desplazamiento", text="Desplazamiento (m)", anchor=tk.CENTER)
tabla.heading("Trabajo", text="Trabajo (J)", anchor=tk.CENTER)


############################################################################
#                               Calculo
############################################################################

# Crear los widgets para ingresar los datos
label_fuerza = tk.Label(marco_3, text="Fuerza (N):")
label_fuerza.pack(pady=10)

entry_fuerza = tk.Entry(marco_3, justify="center")
entry_fuerza.pack(pady=10)

label_desplazamiento = tk.Label(marco_3, text="Desplazamiento (m):")
label_desplazamiento.pack(pady=10)

entry_desplazamiento = tk.Entry(marco_3, justify="center")
entry_desplazamiento.pack(pady=10)

def validar_entrada_fuerza(text):
    if text == "":
        return True
    return re.match(r'^\d*\.?\d*$', text) is not None

def validar_entrada_desplazamiento(text):
    if text == "":
        return True
    if text.startswith('-'):
        return True
    return re.match(r'^-?\d*\.?\d*$', text) is not None

vcmd_fuerza = (ventana.register(validar_entrada_fuerza), '%P')
vcmd_desplazamiento = (ventana.register(validar_entrada_desplazamiento), '%P')

entry_fuerza.config(validate="key", validatecommand=vcmd_fuerza)
entry_desplazamiento.config(validate="key", validatecommand=vcmd_desplazamiento)

# Función para calcular el trabajo
def calcular_trabajo():
    try:
        fuerza = float(entry_fuerza.get())
        desplazamiento = float(entry_desplazamiento.get())
        
        trabajo = fuerza * desplazamiento
        
        label_resultado.config(text=f"El trabajo es: {trabajo} J")
        
        # Agregar los datos a la lista
        datos_grafico.append((fuerza, desplazamiento, trabajo))
        
        # Actualizar el gráfico y la tabla
        actualizar_grafico_tabla()
        entry_fuerza.delete(0, tk.END)
        entry_desplazamiento.delete(0, tk.END)
        
    except ValueError:
        label_resultado.config(text="Ingrese valores numéricos válidos")

# Botón para calcular el trabajo
btn_calcular = tk.Button(marco_3, text="Calcular", command=calcular_trabajo)
btn_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(marco_3, text="")
label_resultado.pack(pady=10)



############################################################################
#                               Grafico
############################################################################
# Crear la figura del gráfico
figura = Figure(figsize=(anPanta // 2 / 100, alPanta // 2 / 100), dpi=100)
grafico = figura.add_subplot(111)

# Agregar el gráfico a la ventana
canvas = FigureCanvasTkAgg(figura, master=marco_2)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Lista para almacenar los datos del gráfico y la tabla
datos_grafico = []

# Función para actualizar el gráfico y la tabla
def actualizar_grafico_tabla():
    # Limpiar el gráfico anterior
    grafico.clear()
    
    # Crear el nuevo gráfico con los datos almacenados
    fuerzas, desplazamiento, trabajos = zip(*datos_grafico)
    grafico.plot(desplazamiento, fuerzas, marker='o', linestyle='-')
    grafico.set_xlabel("Desplazamiento (m)")
    grafico.set_ylabel("Fuerza (N)")
    grafico.set_title("Gráfico de Trabajo Mecánico")
    grafico.grid(True)
    
    # Actualizar el gráfico en la interfaz
    canvas.draw()
    
    # Actualizar la tabla con los datos almacenados
    actualizar_tabla()


# Función para actualizar la tabla con los datos almacenados
def actualizar_tabla():
    # Limpiar los datos anteriores de la tabla
    tabla.delete(*tabla.get_children())
    
    # Agregar los datos a la tabla
    for i, (fuerza, desplazamiento, trabajo) in enumerate(datos_grafico, start=1):
        tabla.insert("", "end", text=str(i), values=(i, fuerza, desplazamiento, trabajo))


def limpiar_datos():
    # Borrar los datos de la tabla
    tabla.delete(*tabla.get_children())

    # Borrar los datos del gráfico
    datos_grafico.clear()

    # Limpiar el gráfico
    grafico.clear()
    canvas.draw()

# Crear el botón para limpiar los datos
btn_limpiar = tk.Button(marco_3, text="Limpiar datos", command=limpiar_datos)
btn_limpiar.pack()


# Iniciar el bucle de eventos
ventana.mainloop()