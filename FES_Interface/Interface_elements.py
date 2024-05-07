from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import serial.tools.list_ports
import time
import os
import sys

connected = False
#ser = None
# Función para inicializar la comunicación serial
def initialize_serial(port):
    try:
        ser = serial.Serial(port, 9600)
        return ser
    except Exception as e:
        print("Error al inicializar el puerto serial:", e)
        return None

# Función para obtener la lista de puertos disponibles
def get_available_ports():
    ports = [port.device for port in serial.tools.list_ports.comports()]
    return ports

# Función para actualizar la lista de puertos disponibles en el Combobox
def update_ports():
    ports = get_available_ports()
    port_combobox['values'] = ports

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Función para ajustar la imagen al tamaño de la pantalla
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = img_copy.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    background.config(image=photo)
    background.image = photo  # evitar que la imagen sea recolectada por el recolector de basura

# Función para conectar el puerto serial
def connect_serial():
    global ser
    try:
        # Configurar la comunicación serial con Arduino con puerto seleccionado
        selected_port = port_combobox.get()
        print(selected_port)
        ser = initialize_serial(selected_port)
        time.sleep(2)  # Espera a que se establezca la conexión
        return ser
    except Exception as e:
        print("Error al conectar con el puerto serial:", e)
        return None

# Función para enviar el estado a Arduino y actualizar el color de la etiqueta
def pin_status(state_ar, label):
    global ser
    send_state = state_ar
    # Cambiar el color de la etiqueta a verde si se activa un canal
    if state_ar.endswith("on"):
        label.config(bg='green')
    else:
        label.config(bg='red')
    try:
        #print("Trying to send:", send_state)
        # Enviar el estado a Arduino
        ser.write(send_state.encode('ascii'))

        #print("Estado enviado a Arduino con éxito", send_state)
    except Exception as e:
        print(f"Error al enviar el estado a Arduino: {str(e)}")

# Función para cerrar el programa
def exit_program():
    root.destroy()

# Crear la interfaz gráfica
root = Tk()
root.title("FEP Control Interface")
root.configure(background='white')
root.attributes('-fullscreen', True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{int(screen_width)}x{int(screen_height)}")

scale_factor = screen_width / 1920
font_resize_factor = screen_width / 1850 #Factor de escalamiento según tamaño de ventana detectado

# Cargar la imagen con Pillow
img = Image.open(resource_path("background_fes.png"))
img_copy = img.copy()
photo = ImageTk.PhotoImage(img)

# Crear un widget Label para mostrar la imagen de fondo
background = Label(root, image=photo)
background.bind('<Configure>', resize_image)  # Ajustar el tamaño de la imagen cuando se cambia el tamaño de la ventana
background.pack(fill=BOTH, expand=True)

#Position labels
x_position1 =screen_width * 0.07
y_position1 =screen_height * 0.21
x_position_c1 = screen_width * 0.1
x_position_c2 = screen_width * 0.3
x_position_c3 = screen_width * 0.5
x_position_c4 = screen_width * 0.7

# Añadir título a la interfaz
title_label = Label(root, text="FES Control Interface", font=("Calibri", int(35 * (font_resize_factor))))
title_label.configure(background='white')
title_label.place(x=screen_width * 0.38, y=screen_height * 0.0324)

# Añadir título para Initial Settings
initial_label = Label(root, text="Port selection", font=("Calibri", int(25 * (font_resize_factor))))
initial_label.configure(background='white')
initial_label.place(x=x_position1, y=y_position1)

# Añadir texto al lado del Combobox de Communication port
port_label =  Label(root, text="Please select a communication port:", font=("Calibri", int(18 * (font_resize_factor))))
port_label.configure(background='white')
port_label.place(x=x_position1, y=screen_height * 0.269)

# Crear Combobox para seleccionar el puerto serial
port_combobox = ttk.Combobox(root, state="readonly", font=("Calibri", int(17 * (font_resize_factor))))
port_combobox.place(x=x_position1, y=screen_height * 0.33)

# Botón "Connect" para cerrar el programa
connect_button =  Button(root, text="Connect", command=connect_serial, font=("Calibri", int(17 * (font_resize_factor))))
connect_button.place(x=x_position1 + (430*scale_factor), y=screen_height * 0.321)

# Actualizar la lista de puertos disponibles
update_ports()

#Botón "Update ports" para actualizar los puertos disponibles
update_ports_button =  Button(root, text="Update ports", command=update_ports, font=("Calibri", int(17 * (font_resize_factor))))
update_ports_button.place(x=x_position1 + (590*scale_factor) , y=screen_height * 0.321)


# Añadir título para Initial Settings
channel_label = Label(root, text="FES channel activation", font=("Calibri", int(25 * (font_resize_factor))))
channel_label.configure(background='white')
channel_label.place(x=x_position1, y=y_position1+(300*scale_factor))

# Botón para activar Channel 1
channel1_button =  Button(root, text="Channel 1", height= 3, width=10, font=("Calibri", int(19 * (font_resize_factor))))
channel1_button.place(x=x_position_c1, y=screen_height * 0.6)

# Botón para desactivar Channel 1
disconnect1_button =  Button(root, text="Disconnect", height= 1, width=8, font=("Calibri", int(16 * (font_resize_factor))))
disconnect1_button.place(x=x_position_c1 + (20*scale_factor), y=screen_height * 0.75 + (40*scale_factor))

# Botón para activar Channel 2
channel2_button =  Button(root, text="Channel 2", height= 3, width=10, font=("Calibri", int(19 * (font_resize_factor))))
channel2_button.place(x=x_position_c2, y=screen_height * 0.6)

# Botón para desactivar Channel 2
disconnect2_button =  Button(root, text="Disconnect", height= 1, width=8, font=("Calibri", int(16 * (font_resize_factor))))
disconnect2_button.place(x=x_position_c2 + (20*scale_factor), y=screen_height * 0.75 + (40*scale_factor))

# Botón para activar Channel 3
channel3_button =  Button(root, text="Channel 3", height= 3, width=10, font=("Calibri", int(19 * (font_resize_factor))))
channel3_button.place(x=x_position_c3, y=screen_height * 0.6)

# Botón para desactivar Channel 1
disconnect3_button =  Button(root, text="Disconnect", height= 1, width=8, font=("Calibri", int(16 * (font_resize_factor))))
disconnect3_button.place(x=x_position_c3 + (20*scale_factor), y=screen_height * 0.75 + (40*scale_factor))

# Botón para activar Channel 4
channel4_button =  Button(root, text="Channel 4", height= 3, width=10, font=("Calibri", int(19 * (font_resize_factor))))
channel4_button.place(x=x_position_c4, y=screen_height * 0.6)

# Botón para desactivar Channel 1
disconnect4_button =  Button(root, text="Disconnect", height= 1, width=8, font=("Calibri", int(16 * (font_resize_factor))))
disconnect4_button.place(x=x_position_c4 + (20*scale_factor), y=screen_height * 0.75 + (40*scale_factor))

# Botón para activar Channel 4
onchannels_button =  Button(root, text="Activate all", font=("Calibri", int(17 * (font_resize_factor))))
onchannels_button.place(x=screen_width * 0.857, y=screen_height * 0.72)

# Botón para desactivar Channel 1
offchannels_button =  Button(root, text="Disconnect all", font=("Calibri", int(17 * (font_resize_factor))))
offchannels_button.place(x=screen_width * 0.85, y=screen_height * 0.79)

# Crear etiquetas para indicar el estado de cada canal
channel1_status_label = Label(root, bg="red", width=15, height=1)
channel1_status_label.place(x=x_position_c1, y=screen_height * 0.72)

channel2_status_label = Label(root, bg="red", width=15, height=1)
channel2_status_label.place(x=x_position_c2, y=screen_height * 0.72)

channel3_status_label = Label(root, bg="red", width=15, height=1)
channel3_status_label.place(x=x_position_c3, y=screen_height * 0.72)

channel4_status_label = Label(root, bg="red", width=15, height=1)
channel4_status_label.place(x=x_position_c4, y=screen_height * 0.72)

# Asignar la función de cambio de color a cada botón de activación
channel1_button.config(command=lambda: pin_status('1', channel1_status_label))
channel2_button.config(command=lambda: pin_status('2', channel2_status_label))
channel3_button.config(command=lambda: pin_status('3', channel3_status_label))
channel4_button.config(command=lambda: pin_status('4', channel4_status_label))
onchannels_button.config(command=lambda: pin_status('5', channel4_status_label))

# Asignar la función de cambio de color a cada botón de desactivación
disconnect1_button.config(command=lambda: pin_status('a', channel1_status_label))
disconnect2_button.config(command=lambda: pin_status('b', channel2_status_label))
disconnect3_button.config(command=lambda: pin_status('c', channel3_status_label))
disconnect4_button.config(command=lambda: pin_status('d', channel4_status_label))
offchannels_button.config(command=lambda: pin_status('0', channel4_status_label))

# Botón "Exit" para cerrar el programa
exit_button =  Button(root, text="Exit", height= 1, width=8, font=("Calibri", int(20 * (font_resize_factor))), command=exit_program)
exit_button.place(x=screen_width * 0.865, y=screen_height * 0.47)

# Evento de teclado para la tecla "Esc"
root.bind("<Escape>", lambda event: root.destroy())

root.mainloop()
