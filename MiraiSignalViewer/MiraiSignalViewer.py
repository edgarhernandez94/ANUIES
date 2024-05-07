import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import csv
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import os
import sys
import threading

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

# Configuración del gráfico
max_samples = 100000  # Número máximo de muestras en el gráfico
x_muestras = 10

# Crear la interfaz gráfica
root = Tk()
root.title("Mirai Lab: Signal Viewer")
root.configure(background='white')
root.attributes('-fullscreen', True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{int(screen_width)}x{int(screen_height)}")

# Tamaño de las gráficas en la interfaz (ancho y alto)
graph_width = int(11 * screen_width / 1920)
graph_height = int(9 * screen_height / 1080)
scale_factor = screen_width / 1920

# Espacio entre las filas de la figura
row_spacing = 0.5

# Baud rates disponibles
baud_rates = [9600, 115200]

#Inicialización de variables y contadores
global ser 
ani = None
connected = False
sampling = False
folder = False
csvfile = None
writer = None
sample_counter = 0  # Inicializar el contador de muestras

# Función para obtener la lista de puertos disponibles
def get_available_ports():
    ports = [port.device for port in serial.tools.list_ports.comports()]
    return ports

# Función para actualizar la lista de puertos disponibles en el Combobox
def update_ports():
    ports = get_available_ports()
    port_combobox['values'] = ports

# Función para conectar el puerto serial
def connect_serial():
    global connected, ser
    port_status_msg.set("Connecting")
    if not connected:
        port_status_msg.set("Connecting")
        selected_port = port_combobox.get()
        selected_baud_rate = baud_rate_combobox.get()
        print(selected_port)
        print(selected_baud_rate)
        ser = initialize_serial(selected_port, int(selected_baud_rate))

        # Esperar y verificar los datos
        def wait_for_signal():
            global connected, ser
            try:
                start_time = time.time()  # Marcar el tiempo de inicio
                timeout = 3  # Tiempo máximo de espera en segundos
                ser.timeout = 1  # Establecer un timeout breve para cada lectura

                while time.time() - start_time < timeout:
                    if ser.inWaiting() > 0:  # Verificar si hay datos esperando ser leídos
                        data = ser.readline().decode().strip()  # Leer una línea desde el serial
                        data_array = data.split(',')
                        if len(data_array) == 6:
                            # Si los datos son correctos, inicia la animación y ajusta los botones
                            print("Señal correcta recibida:", data_array)
                            start_animation()
                            connect_button.config(state="disabled")
                            disconnect_button.config(state="normal")
                            connected = True
                            port_status_msg.set("Port connected")
                            return  # Salir de la función después de recibir la señal correcta
                        else:
                            port_status_msg.set("Error in port")
                            ser.close()
                            connected = False
                    else:
                        time.sleep(0.1)  # Pequeña pausa para evitar un uso intensivo del CPU

                # Si se llega aquí, significa que el tiempo se agotó sin recibir el formato correcto
                print("Señal incorrecta o timeout. Desconectando...")
                port_status_msg.set("Error in port")
                ser.close()
                connected = False
            except Exception as e:
                print("Error al leer del serial:", e)
                port_status_msg.set("Error in port")
                ser.close()
                connected = False

        # Iniciar la espera de señal en un hilo separado para no bloquear la interfaz de usuario
        threading.Thread(target=wait_for_signal).start()

# Función para inicializar la comunicación serial
def initialize_serial(port, baud_rate):
    global ser
    ser = serial.Serial(port, baud_rate)
    ser.flushInput()
    return ser

# Función para desconectar el puerto serial
def disconnect_serial():
    global connected
    if connected:
        ser.close()
        print('Serial connection closed.')
        disconnect_button.config(state="disabled")
        connect_button.config(state="normal")
        connected = False
        port_status_msg.set("No port")

# Función para leer datos de la comunicación serial
def M5data():
    global values
    print(ser)
    try:
        line = ser.readline().decode().strip()
        values = tuple(map(float, line.split(',')))
        print(values)
    except KeyboardInterrupt:
        ser.close()
        print('Serial connection closed.')
        exit()
    return values

# Función para seleccionar la carpeta de destino
def select_folder():
    global folder_selected, folder
    folder_selected = filedialog.askdirectory()
    update_selected_folder_label()
    if folder_selected != None:
        folder = True

def start_test():
    global sampling, csvfile, writer, sample_counter
    if connected and not sampling:
        if folder:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{folder_selected}/test_data_{timestamp}.csv"
            csvfile = open(filename, 'w', newline='')
            fieldnames = ["Sample", "Gyroscope X", "Gyroscope Y", "Gyroscope Z", "Accelerometer X", "Accelerometer Y", "Accelerometer Z"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            sampling = True
            sample_counter = 0  # Reiniciar el contador de muestras
            start_test_button.config(state="disabled")
            end_test_button.config(state="normal")
        else:
            messagebox.showinfo(title="Error", message="Please select a folder first.")

# Función para detener el test y guardar el archivo CSV
def end_test():
    global sampling, csvfile
    if sampling:
        csvfile.close()
        sampling = False
        start_test_button.config(state="normal")
        end_test_button.config(state="disabled")

# Función de animación para actualizar los datos en el gráfico
def animate(i):
    global sample_counter
    data = M5data()
    print(data)

    for j in range(num_lines):
        amplitude = int(data[j])
        x_data[j].append(i)
        y_data[j].append(amplitude)

        x_data_window = x_data[j][-x_muestras:]
        y_data_window = y_data[j][-x_muestras:]

        if j < 3:
            lines[j].set_data(x_data_window, y_data_window)
        else:
            lines2[j-3].set_data(x_data_window, y_data_window)

    ax1.set_xlim(max(0, i - x_muestras), i)
    ax2.set_xlim(max(0, i - x_muestras), i)

    if sampling:
        sample_counter += 1  # Incrementar el contador de muestras si el muestreo está activo
        sample_data = {"Sample": sample_counter, "Gyroscope X": data[0], "Gyroscope Y": data[1], "Gyroscope Z": data[2], 
                       "Accelerometer X": data[3], "Accelerometer Y": data[4], "Accelerometer Z": data[5]}
        writer.writerow(sample_data)

    return lines + lines2

# Función para iniciar la animación
def start_animation():
    global ani
    ani = animation.FuncAnimation(fig, animate, frames=max_samples, interval=1, blit=True)

# Función para cerrar el programa
def exit_program():
    root.destroy()

# # Cargar la imagen
# img = tk.PhotoImage(file="background_mirai.png")

# # Crear un Canvas para la imagen de fondo
# background = tk.Label(root, image=img, bd=0)
# background.pack()

# Cargar la imagen con Pillow
img = Image.open(resource_path("background_mirai.png"))
img_copy = img.copy()
photo = ImageTk.PhotoImage(img)

# Crear un widget Label para mostrar la imagen de fondo
background = Label(root, image=photo)
background.bind('<Configure>', resize_image)  # Ajustar el tamaño de la imagen cuando se cambia el tamaño de la ventana
background.pack(fill=BOTH, expand=True)

# Crear la figura y los subgráficos, ajustando el tamaño basado en el tamaño de la pantalla
plt_style = 'seaborn-whitegrid'
fig_size = (screen_width / 170, screen_height / 120)  # Ajustar estos valores según sea necesario
dpi = 100  # DPI para la figura, ajustar según sea necesario

font_resize_factor = screen_width / 1850 #Factor de escalamiento según tamaño de ventana detectado

fig = Figure(figsize=fig_size, dpi=dpi) #Declarar dimensiones de la gráfica
plt.style.use(plt_style) #Implementar estilo de gráfico
fig.subplots_adjust(hspace = font_resize_factor*0.4) #Ajuste de espacio entre subplots
ax1 = fig.add_subplot(211)  # Primer subplot
ax2 = fig.add_subplot(212)  # Segundo subplot

# Agregar las gráficas a la interfaz de Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
# Colocar el canvas en la posición deseada, ajustando según sea necesario
canvas_widget.place(x=0, y=screen_height * 0.09)

#Declaración de posiciones para elementos
x_position_initial = screen_width * 0.587
x_position_subtitles = x_position_initial-(15 * scale_factor)
x_position_baud = screen_width * 0.758
y_position_combobox = screen_height * 0.33
y_position_buttons1 = screen_height * 0.47
y_position_buttons2 = y_position_buttons1 + (230 * scale_factor)
y_position_folder = y_position_buttons2 + (85 * scale_factor)
# Declaración de posiciones para elementos, ajustadas según el factor de escala
x_position_select = x_position_initial + (35 * scale_factor)
x_position_buttons2 = x_position_select + (80 * scale_factor)
# Ajustar los incrementos según el factor de escala
x_position_start = x_position_select + (230 * scale_factor)
x_position_end = x_position_start + (200 * scale_factor)

# Añadir título a la interfaz
title_label = Label(root, text="Mirai Lab: Signal Stick Viewer", font=("Calibri", int(35 * (font_resize_factor))))
title_label.configure(background='white')
title_label.place(x=screen_width * 0.35, y=screen_height * 0.0324)

# Añadir título para Initial Settings
initial_label = Label(root, text="Initial Settings", font=("Calibri", int(20 * (font_resize_factor))))
initial_label.configure(background='white')
initial_label.place(x=x_position_subtitles, y=screen_height * 0.21)

# Añadir texto al lado del Combobox de Communication port
port_label =  Label(root, text="Communication port:", font=("Calibri", int(18 * (font_resize_factor))))
port_label.configure(background='white')
port_label.place(x=x_position_initial, y=screen_height * 0.269)

# Crear Combobox para seleccionar el puerto serial
port_combobox = ttk.Combobox(root, state="readonly", font=("Calibri", int(17 * (font_resize_factor))))
port_combobox.place(x=x_position_initial, y=y_position_combobox)

# Añadir texto al lado del Combobox de baud rate
baud_rate_label =  Label(root, text="Baud rate:", font=("Calibri", int(18 * (font_resize_factor))))
baud_rate_label.configure(background='white')
baud_rate_label.place(x=x_position_baud, y=screen_height * 0.269)

# Crear Combobox para seleccionar el baud rate
baud_rate_combobox = ttk.Combobox(root, state="readonly", values=baud_rates, font=("Calibri", int(17 * (font_resize_factor))))
baud_rate_combobox.place(x=x_position_baud, y=y_position_combobox)
baud_rate_combobox.current(0)  # Selecciona el primer baud rate por defecto

# Actualizar la lista de puertos disponibles
update_ports()

#Botón "Update ports" para actualizar los puertos disponibles
update_ports_button =  Button(root, text="Update ports", command=update_ports, font=("Calibri", int(17 * (font_resize_factor))))
update_ports_button.place(x=x_position_end, y=y_position_buttons1)

# Mensaje "Port status" para indicar estado del puerto
port_status_msg =  StringVar()
port_status_msg.set("No port")
port_status_text =  Label(root, textvariable=port_status_msg, font=("Calibri", int(19 * (font_resize_factor))))
port_status_text.configure(background='white')
port_status_text.place(x=x_position_initial + (130 * scale_factor), y=y_position_buttons1-(69 * scale_factor))

# Label "Port status" para indicar estado del puerto
port_status_label =  Label(root, text="- Port status:", font=("Calibri", int(17 * (font_resize_factor))))
port_status_label.configure(background='white')
port_status_label.place(x=x_position_initial, y=y_position_buttons1-(70 * scale_factor))

# Botón "Connect" para iniciar la comunicación serial
connect_button =  Button(root, text="Connect", command=connect_serial, font=("Calibri", int(17 * (font_resize_factor))))
connect_button.place(x=x_position_select+(15 * scale_factor), y=y_position_buttons1)

# Botón "Disconnect" para detener la comunicación serialx_position_start
disconnect_button =  Button(root, text="Disconnect", command=disconnect_serial, state="disabled", font=("Calibri", int(17 * (font_resize_factor))))
disconnect_button.place(x=x_position_start-(10 * scale_factor), y=y_position_buttons1)

# Añadir título para testing
test_label =  Label(root, text="Testing Hub", font=("Calibri", int(20 * (font_resize_factor))))
test_label.configure(background='white')
test_label.place(x=x_position_subtitles, y=screen_height * 0.6)

# Botón "Select folder" para seleccionar la carpeta de destino
select_folder_button =  Button(root, text="Select folder", font=("Calibri", int(17 * (font_resize_factor))), command=select_folder)
select_folder_button.place(x=x_position_select, y=y_position_buttons2)

# Crear Label para mostrar el contenido de la carpeta seleccionada
selected_folder_label =  Label(root, text="- Folder path:", font=("Calibri", int(17 * (font_resize_factor))), background='white')
selected_folder_label.place(x=x_position_initial, y=y_position_folder)
updated_folder_label =  Label(root, text="", font=("Calibri", int(15 * (font_resize_factor))), background='white')
updated_folder_label.place(x=x_position_buttons2+(20 * scale_factor), y=y_position_folder+(3 * scale_factor))

# Función para actualizar el contenido del Label con la carpeta seleccionada
def update_selected_folder_label():
    updated_folder_label.config(text=folder_selected)

# Botón "Start test" para iniciar el muestreo de datos en un archivo CSV
start_test_button =  Button(root, text="Start test", font=("Calibri", int(17 * (font_resize_factor))), command=start_test)
start_test_button.place(x=x_position_start, y=y_position_buttons2)

# Botón "End test" para detener el muestreo de datos en el archivo CSV
end_test_button =  Button(root, text="End test", font=("Calibri", int(17 * (font_resize_factor))), command=end_test, state="disabled")
end_test_button.place(x=x_position_end, y=y_position_buttons2)

# Botón "Exit" para cerrar el programa
exit_button =  Button(root, text="Exit", height= 1, width=8, font=("Calibri", int(20 * (font_resize_factor))), command=exit_program)
exit_button.place(x=screen_width * 0.865, y=y_position_buttons2 + (160 * scale_factor))

# Evento de teclado para la tecla "Esc"
root.bind("<Escape>", lambda event: root.destroy())

# Configuración de las líneas
num_lines = 6
x_data, y_data = [[] for _ in range(num_lines)], [[] for _ in range(num_lines)]

# Títulos de las subgráficas
ax1.set_title('Gyroscope', fontsize= int(17 * (font_resize_factor)))
ax2.set_title('Accelerometer', fontsize= int(17 * (font_resize_factor)))
ax1.set_ylabel('Amplitude', fontsize= int(15 * (font_resize_factor)))
ax2.set_ylabel('Amplitude', fontsize= int(15 * (font_resize_factor)))
ax1.set_xlabel('Time', fontsize=int(15 * (font_resize_factor)))
ax2.set_xlabel('Time', fontsize=int(15 * (font_resize_factor)))

# Configurar límites de los ejes
ax1.set_ylim(-1000, 1000)
ax2.set_ylim(-4, 4)

# Configuración de las líneas
lines = [ax1.plot([], [], lw=2, linestyle='-')[0] for _ in range(3)]  # Primeras 3 líneas en la primera subgráfica
lines2 = [ax2.plot([], [], color='C{}'.format(i+4), lw=2, linestyle='-')[0] for i in range(3)]  # Últimas 3 líneas en la segunda subgráfica

#Ventana not resizable
# root.resizable(0, 0) 

root.mainloop()