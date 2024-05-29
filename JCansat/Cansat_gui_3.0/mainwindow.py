import tkinter as tk
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView
import matplotlib.figure as mpl_fig
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
import io
from tkinter import ttk  # Importación para Combobox
import serial.tools.list_ports  # Importación para listar puertos COM
import threading
import queue

# -------------------------------------------------------------------------------
# Funciones auxiliares
# -------------------------------------------------------------------------------

def ajustar_a_resolucion(x, y, width, height, target_res, current_res):
    prop_x = current_res[0] / target_res[0]
    prop_y = current_res[1] / target_res[1]
    return int(x * prop_x), int(y * prop_y), int(width * prop_x), int(height * prop_y)

def cerrar(event):
    root.destroy()

def crear_figura():
    # Crear una figura de matplotlib usando bajo nivel
    fig = mpl_fig.Figure(figsize=(4, 3), dpi=80)  # Tamaño reducido
    fig.patch.set_alpha(0)  # Establecer la transparencia del fondo de la figura
    ax = fig.add_axes([0, 0, 1, 1])  # Establecer facecolor a 'none' para fondo transparente
    return fig, ax

def listar_puertos():
    return [port.device for port in serial.tools.list_ports.comports()]

def actualizar_puertos():
    puertos = listar_puertos()
    combobox_puertos['values'] = puertos
    if puertos:
        combobox_puertos.set(puertos[0])

def conectar():
    global ser, map_widget
    seleccionado = combobox_puertos.get()
    try:
        ser = serial.Serial(seleccionado, 115200)
        # #print(f"Conectado al puerto: {seleccionado}")
        
        # Mostrar ventana emergente de "Conexión Exitosa"
        ventana_exito = tk.Toplevel(root)
        ventana_exito.title("¡Conexión Exitosa!")
        ventana_exito.geometry("300x100")
        
        label_exito = tk.Label(ventana_exito, text="¡Conexión Exitosa!", font=("Helvetica", 16))
        label_exito.pack(pady=20)
        
        # Hacer que la ventana desaparezca después de 3 segundos
        ventana_exito.after(3000, ventana_exito.destroy)
        
        # Cambiar el texto del botón a "Desconectar" y configurar su comando a desconectar()
        btn_conectar.config(text="Desconectar", command=desconectar)
        
        # Iniciar la recepción de datos en un hilo separado
        thread = threading.Thread(target=leer_puerto_serie)
        thread.daemon = True  # Permite que el hilo termine cuando se cierre la aplicación
        thread.start()
        
        # Actualizar la posición del mapa después de conectar
        latitud = 19.16018
        longitud = -100.13440
        map_widget.set_position(latitud, longitud)
        map_widget.set_zoom(12)
        
    except Exception as e:
        print(f"Error al conectar al puerto: {seleccionado}\n{e}")

def desconectar():
    global ser
    try:
        if ser and ser.is_open:
            ser.close()
            #print("Desconectado del puerto")
    except Exception as e:
        print(f"Error al desconectar del puerto: {e}")
        
    # Cambiar el texto del botón a "Conectar" y configurar su comando a conectar()
    btn_conectar.config(text="Conectar", command=conectar)

def leer_puerto_serie():
    global ser, queue_grafica1, queue_grafica2, queue_grafica3, label_dato_11, label_dato_15
    
    while ser and ser.is_open:
        try:
            if ser.in_waiting > 0:
                linea = ser.readline().decode('utf-8').strip()
                datos = linea.split(',')
                if len(datos) >= 15:
                    data1 = [float(datos[0]), float(datos[1]), float(datos[2])]
                    data2 = [float(datos[3]), float(datos[4]), float(datos[5])]
                    data3 = [float(datos[6]), float(datos[7]), float(datos[8])]
                    
                    queue_grafica1.put(data1)
                    queue_grafica2.put(data2)
                    queue_grafica3.put(data3)

                    # Actualizar el label de Pressure (dato 10)
                    root.after(0, lambda val=datos[9]: label_dato_10.config(text=f"{val}"))
                    # Actualizar el label de temperatura (dato 11)
                    root.after(0, lambda val=datos[10]: label_dato_11.config(text=f"{val}"))
                    # Actualizar el label de altitude (dato 12)
                    root.after(0, lambda val=datos[11]: label_dato_12.config(text=f"{val}"))
                    # Actualizar el label de latitude (dato 13)
                    root.after(0, lambda val=datos[12]: label_dato_13.config(text=f"{val}"))
                    # Actualizar el label de longitud (dato 14)
                    root.after(0, lambda val=datos[13]: label_dato_14.config(text=f"{val}"))
                    # Actualizar el label del battery (dato 15)
                    root.after(0, lambda val=datos[14]: label_dato_15.config(text=f"{val}"))
                    # Dentro de leer_puerto_serie
                   

                    #print(f"Dato 11: {datos[10]}, Dato 15: {datos[14]}")  # Imprimir los datos actualizados para las etiquetas

                    #print(datos)
        except Exception as e:
            print(f"Error al recibir datos: {e}")

def update_grafica1():
    if not queue_grafica1.empty():
        data = queue_grafica1.get()
        xdata.append(data[0])
        ydata.append(data[1])
        zdata.append(data[2])
        
        if len(xdata) > 20:
            xdata.pop(0)
        if len(ydata) > 20:
            ydata.pop(0)
        if len(zdata) > 20:
            zdata.pop(0)
        
        ax1.clear()
        ax1.fill_between(range(len(xdata)), xdata, alpha=0.3, label='X Mag', color='blue')
        ax1.fill_between(range(len(ydata)), ydata, alpha=0.3, label='Y Mag', color='green')
        ax1.fill_between(range(len(zdata)), zdata, alpha=0.3, label='Z Mag', color='red')
        ax1.legend()
        
        ax1.autoscale()  # Autoescalar los ejes

        canvas = FigureCanvasAgg(fig1)
        buf = io.BytesIO()
        canvas.print_png(buf)
        buf.seek(0)

        grafica_image = Image.open(buf)
        grafica_photo = ImageTk.PhotoImage(grafica_image)
        grafica_label1.config(image=grafica_photo)
        grafica_label1.image = grafica_photo
    
    root.after(100, update_grafica1)

def update_grafica2():
    if not queue_grafica2.empty():
        data = queue_grafica2.get()
        xdata2.append(data[0])
        ydata2.append(data[1])
        zdata2.append(data[2])
        
        if len(xdata2) > 20:
            xdata2.pop(0)
        if len(ydata2) > 20:
            ydata2.pop(0)
        if len(zdata2) > 20:
            zdata2.pop(0)
        
        ax2.clear()
        ax2.fill_between(range(len(xdata2)), xdata2, alpha=0.3, label='X Acc', color='blue')
        ax2.fill_between(range(len(ydata2)), ydata2, alpha=0.3, label='Y Acc', color='green')
        ax2.fill_between(range(len(zdata2)), zdata2, alpha=0.3, label='Z Acc', color='red')
        ax2.legend()
        
        ax2.autoscale()  # Autoescalar los ejes

        canvas = FigureCanvasAgg(fig2)
        buf = io.BytesIO()
        canvas.print_png(buf)
        buf.seek(0)

        grafica_image = Image.open(buf)
        grafica_photo = ImageTk.PhotoImage(grafica_image)
        grafica_label2.config(image=grafica_photo)
        grafica_label2.image = grafica_photo
    
    root.after(100, update_grafica2)


def update_grafica3():
    if not queue_grafica3.empty():
        data = queue_grafica3.get()
        xdata3.append(data[0])
        ydata3.append(data[1])
        zdata3.append(data[2])
        
        if len(xdata3) > 20:
            xdata3.pop(0)
        if len(ydata3) > 20:
            ydata3.pop(0)
        if len(zdata3) > 20:
            zdata3.pop(0)
        
        ax3.clear()
        ax3.fill_between(range(len(xdata3)), xdata3, alpha=0.3, label='X Gyro', color='blue')
        ax3.fill_between(range(len(ydata3)), ydata3, alpha=0.3, label='Y Gyro', color='green')
        ax3.fill_between(range(len(zdata3)), zdata3, alpha=0.3, label='Z Gyro', color='red')
        ax3.legend()
        
        ax3.autoscale()  # Autoescalar los ejes

        canvas = FigureCanvasAgg(fig3)
        buf = io.BytesIO()
        canvas.print_png(buf)
        buf.seek(0)

        grafica_image = Image.open(buf)
        grafica_photo = ImageTk.PhotoImage(grafica_image)
        grafica_label3.config(image=grafica_photo)
        grafica_label3.image = grafica_photo
    
    root.after(100, update_grafica3)

# -------------------------------------------------------------------------------
# Configuración inicial de la ventana principal
# -------------------------------------------------------------------------------

# Crear la ventana principal
global root
root = tk.Tk()
ser = None
map_widget = None
xdata = []
ydata = []
zdata = []
xdata2 = []
ydata2 = []
zdata2 = []
xdata3 = []
ydata3 = []
zdata3 = []
queue_grafica1 = queue.Queue()
queue_grafica2 = queue.Queue()
queue_grafica3 = queue.Queue()

# Establecer el tamaño de pantalla completa
root.attributes('-fullscreen', True)

# Obtener la resolución de pantalla actual
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
resolucion_actual = (screen_width, screen_height)

# Resolución deseada (4K)
resolucion_4k = (3840, 2160)

# -------------------------------------------------------------------------------
# Configuración de la imagen de fondo
# -------------------------------------------------------------------------------

# Cargar la imagen de fondo
background_image = Image.open("by.png")
background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Establecer la imagen como fondo
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Mantener referencia a la imagen de fondo para evitar garbage collection
background_label.image = background_photo

# Crear el estilo para mejorar la estética
style = ttk.Style()

# Estilo para Combobox
style.configure('TCombobox', padding=5, relief='flat', background='#ffffff')

# Estilo para Botón
style.configure('TButton', padding=5, relief='flat', background='#0078d7', foreground='#0078d7')

# -------------------------------------------------------------------------------
# Configuración del cuadro de puertos COM
# -------------------------------------------------------------------------------
# Crear el Label para "CONEXIÓN" con estilos mejorados
label_conexion = tk.Label(root, text="CONEXIÓN", bg="#0078d7", fg="white", font=("Helvetica", 12, "bold"), anchor="center")
label_conexion.place(x=1450, y=200, width=100, height=30)
# Crear el Label para mostrar el Temperatura
label_dato_11 = tk.Label(root, text="", font=("Helvetica", 24, "bold"), bg="#ffffff")
label_dato_11.place(x=235, y=500)
# Crear el Label para mostrar el Pressure
label_dato_10 = tk.Label(root, text="", font=("Helvetica", 24, "bold"), bg="#ffffff")
label_dato_10.place(x=235, y=710)
# # Crear el Label para mostrar el Altitud
label_dato_12 = tk.Label(root, text="", font=("Helvetica", 24, "bold"), bg="#ffffff")
label_dato_12.place(x=235, y=920)
# # Crear el Label para mostrar el Battery
label_dato_15 = tk.Label(root, text="", font=("Helvetica", 24, "bold"), bg="#ffffff")
label_dato_15.place(x=230, y=1130)  # Ajusta la posición según sea necesario

# Crear el Combobox para los puertos COM
combobox_puertos = ttk.Combobox(root, style='TCombobox')
combobox_puertos.place(x=1550, y=200, width=200, height=30)

# Botón para actualizar la lista de puertos COM
btn_actualizar = ttk.Button(root, text="Actualizar", style='TButton', command=actualizar_puertos)
btn_actualizar.place(x=1760, y=200, width=100, height=30)

# Botón para conectar al puerto COM seleccionado
btn_conectar = ttk.Button(root, text="Conectar", style='TButton', command=conectar)
btn_conectar.place(x=1760, y=240, width=100, height=30)

# Inicializar la lista de puertos COM
actualizar_puertos()

# -------------------------------------------------------------------------------
# Configuración del widget del mapa
# -------------------------------------------------------------------------------

# Ajustar la posición y tamaño del widget del mapa
posicion_x, posicion_y, ancho_widget, alto_widget = ajustar_a_resolucion(
    734, 600, 1574, 1416, resolucion_4k, resolucion_actual
)

# Crear el widget del mapa con las dimensiones y posición ajustadas
map_widget = TkinterMapView(root, width=ancho_widget, height=alto_widget, corner_radius=101)
map_widget.place(x=posicion_x, y=posicion_y)

# Establecer una posición inicial para el mapa en Osaka
latitud_inicial = 34.69374
longitud_inicial = 135.50218
map_widget.set_position(latitud_inicial, longitud_inicial)
map_widget.set_zoom(10)

# -------------------------------------------------------------------------------
# Configuración de las gráficas de matplotlib
# -------------------------------------------------------------------------------

# Crear las figuras de matplotlib
fig1, ax1 = crear_figura()
fig2, ax2 = crear_figura()
fig3, ax3 = crear_figura()

# Crear los Labels para mostrar las imágenes de las gráficas
pos_x_grafica1, pos_y_grafica1, width_grafica1, height_grafica1 = ajustar_a_resolucion(
    2460, 1120, 600, 400, resolucion_4k, resolucion_actual
)
grafica_label1 = tk.Label(root)
grafica_label1.place(x=pos_x_grafica1, y=pos_y_grafica1, width=width_grafica1, height=height_grafica1)

pos_x_grafica2, pos_y_grafica2, width_grafica2, height_grafica2 = ajustar_a_resolucion(
    2450 + 750, 1120, 600, 400, resolucion_4k, resolucion_actual
)
grafica_label2 = tk.Label(root)
grafica_label2.place(x=pos_x_grafica2, y=pos_y_grafica2, width=width_grafica2, height=height_grafica2)

pos_x_grafica3, pos_y_grafica3, width_grafica3, height_grafica3 = ajustar_a_resolucion(
    2450 + 360, 1110 + 440, 600, 400, resolucion_4k, resolucion_actual
)
grafica_label3 = tk.Label(root)
grafica_label3.place(x=pos_x_grafica3, y=pos_y_grafica3, width=width_grafica3, height=height_grafica3)

# Crear las etiquetas de título para las gráficas con estilos mejorados
titulo_grafica1 = tk.Label(root, text="Magnetometer", font=("Helvetica", 14, "bold"), bg="#0078d7", fg="white", bd=2, relief="solid", padx=5, pady=5)
titulo_grafica1.place(x=pos_x_grafica1, y=pos_y_grafica1 - 30, width=width_grafica1, height=30)

titulo_grafica2 = tk.Label(root, text="Accelerometer", font=("Helvetica", 14, "bold"), bg="#0078d7", fg="white", bd=2, relief="solid", padx=5, pady=5)
titulo_grafica2.place(x=pos_x_grafica2, y=pos_y_grafica2 - 30, width=width_grafica2, height=30)

titulo_grafica3 = tk.Label(root, text="Gyroscope", font=("Helvetica", 14, "bold"), bg="#0078d7", fg="white", bd=2, relief="solid", padx=5, pady=5)
titulo_grafica3.place(x=pos_x_grafica3, y=pos_y_grafica3 - 30, width=width_grafica3, height=30)



# -------------------------------------------------------------------------------
# Iniciar la animación
# -------------------------------------------------------------------------------

root.after(0, update_grafica1)
root.after(0, update_grafica2)
root.after(0, update_grafica3)

# -------------------------------------------------------------------------------
# Configuración de etiquetas de los ejes
# -------------------------------------------------------------------------------

# etiqueta_tiempo = tk.Label(root, text="Tiempo")
# etiqueta_tiempo.place(x=pos_x_grafica1 + (width_grafica1 // 2), y=pos_y_grafica1 + height_grafica1 - 50, anchor="center")

# etiqueta_posicion = tk.Label(root, text="Posición")
# etiqueta_posicion.place(x=pos_x_grafica1 + 100, y=pos_y_grafica1 + (height_grafica1 // 2), anchor="e")

# -------------------------------------------------------------------------------
# Enlazar la tecla ESC a la función de cerrar y ejecutar el main loop
# -------------------------------------------------------------------------------

root.bind("<Escape>", cerrar)

# Main loop
root.mainloop()
