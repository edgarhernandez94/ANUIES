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

font_resize_factor = screen_width / 1850 #Factor de escalamiento según tamaño de ventana detectado
# Espacio entre las filas de la figura en MOVEMENT VIEW
row_spacing1 = font_resize_factor*0.4
# Espacio entre las filas de la figura en HEALTH VIEW
row_spacing2 = font_resize_factor*0.35

# Baud rates disponibles
baud_rates = [9600, 115200]

#Inicialización de variables y contadores
global ser 
move_ani = None
connected = False
sampling = False
pro_view = False
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
                        if len(data_array) == 10:
                            # Si los datos son correctos, inicia la animación y ajusta los botones
                            print("Señal correcta recibida:", data_array)
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
            fieldnames = ["Sample", "Gyroscope X", "Gyroscope Y", "Gyroscope Z", "Accelerometer X", "Accelerometer Y", "Accelerometer Z", "Heartrate", "GSR", "Temperature", "SPO2"]
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
def animate_move_data(i):
    global sample_counter
    data = M5data()
    print(data)

    for j in range(num_lines):
        amplitude = int(data[j])
        x_data[j].append(i)
        y_data[j].append(amplitude)

        x_data_window = x_data[j]
        y_data_window = y_data[j]

        if j < 3:
            lines[j].set_data(x_data_window, y_data_window)
        else:
            lines2[j-3].set_data(x_data_window, y_data_window)

    ax1.set_xlim(max(0, i - x_muestras), i)
    ax2.set_xlim(max(0, i - x_muestras), i)

    if sampling:
        sample_counter += 1  # Incrementar el contador de muestras si el muestreo está activo
        csv_data_write()

    return lines + lines2

def ani_move_view():
    global ani_move_fig
    # Iniciar la animación dentro de la función display_movement_view
    ani_move_fig = animation.FuncAnimation(move_fig, animate_move_data, frames=None, interval=1, blit=True)


# Función para animar los datos de salud
def animate_health_data(i):
    x_muestras_hr = 30
    global sample_counter
    data = M5data()  # Obtener los datos de salud desde M5data()
    health_data_1 = data[6]  # Primer dato de salud
    health_data_2 = data[7]  # Segundo dato de salud

    x_data_health.append(i)  # Añadir la nueva muestra al eje x
    
    # Añadir los nuevos datos al eje y
    y_data_health_1.append(health_data_1)
    y_data_health_2.append(health_data_2)

    # Limitar los datos a las últimas 'x_muestras' muestras
    x_data_health_window = x_data_health[-x_muestras_hr:]
    y_data_health_1_window = y_data_health_1[-x_muestras_hr:]
    y_data_health_2_window = y_data_health_2[-x_muestras_hr:]

    # Actualizar las líneas en los subgráficos correspondientes
    lines3[0].set_data(x_data_health_window, y_data_health_1_window)
    lines4[0].set_data(x_data_health_window, y_data_health_2_window)

    # Actualizar los límites de los ejes x
    ax3.set_xlim(max(0, min(x_data_health_window)), max(x_data_health_window))
    ax4.set_xlim(max(0, min(x_data_health_window)), max(x_data_health_window))


    # Incrementar el contador de muestras si el muestreo está activo
    if sampling:
        sample_counter += 1
        csv_data_write()

    # Agregar dos Label debajo de las gráficas
    label_text_temperature = f"Temperature: {data[8]}°C"
    label_text_spo2 = f"Oxygen saturation: {data[9]}%"
    label_temperature = Label(root, text=label_text_temperature, font=("Calibri", subtitle_font_size))
    label_spo2 = Label(root, text=label_text_spo2, font=("Calibri", subtitle_font_size))
    label_temperature.place(x=x_position_temperature, y=y_position_health)
    label_spo2.place(x=x_position_temperature+(500*scale_factor), y=y_position_health)

    return lines3 + lines4

def ani_health_view():
    global ani_health_fig
    # Iniciar la animación dentro de la función display_health_view
    ani_health_fig = animation.FuncAnimation(health_fig, animate_health_data, frames=None, interval=1, blit=True)

# Función de animación para actualizar los datos en el gráfico Pro View
def animate_pro_data(i):
    global sample_counter
    data = M5data()
    print(data)

    for j in range(num_lines):
        amplitude = int(data[j])
        x_data[j].append(i)
        y_data[j].append(amplitude)

        x_data_window = x_data[j]
        y_data_window = y_data[j]

        if j < 3:
            lines5[j].set_data(x_data_window, y_data_window)
        else:
            lines6[j-3].set_data(x_data_window, y_data_window)

    ax5.set_xlim(max(0, i - x_muestras), i)
    ax6.set_xlim(max(0, i - x_muestras), i)
    
    # Actualizar datos de salud (Heartrate y Galvanic Skin Response)
    x_data_health.append(i)
    y_data_health_1.append(data[6])
    y_data_health_2.append(data[7])

    x_data_health_window = x_data_health[-x_muestras:]
    y_data_health_1_window = y_data_health_1[-x_muestras:]
    y_data_health_2_window = y_data_health_2[-x_muestras:]

    lines7[0].set_data(x_data_health_window, y_data_health_1_window)
    lines8[0].set_data(x_data_health_window, y_data_health_2_window)

    # Actualizar los límites de los ejes x
    ax5.set_xlim(max(0, i - x_muestras), i)
    ax6.set_xlim(max(0, i - x_muestras), i)
    ax7.set_xlim(max(0, min(x_data_health_window)), max(x_data_health_window))
    ax8.set_xlim(max(0, min(x_data_health_window)), max(x_data_health_window))

    # Agregar dos Label debajo de las gráficas
    label_text_temperature = f"Temperature: {data[8]}°C"
    label_text_spo2 = f"Oxygen saturation: {data[9]}%"
    label_temperature = Label(root, text=label_text_temperature, font=("Calibri", subtitle_font_size))
    label_spo2 = Label(root, text=label_text_spo2, font=("Calibri", subtitle_font_size))
    label_temperature.place(x=x_position_temperature, y=y_position_health)
    label_spo2.place(x=x_position_temperature+(500*scale_factor), y=y_position_health)

    # Incrementar el contador de muestras si el muestreo está activo
    if sampling:
        sample_counter += 1
        csv_data_write()

    return lines5 + lines6 + lines7 + lines8


def ani_pro_view():
    # Animar las gráficas de pro_view
    animation.FuncAnimation(pro_view_fig, animate_pro_data, frames=None, interval=1, blit=True)

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
fig_size = (screen_width / 140, screen_height / 120)  # Ajustar estos valores según sea necesario
dpi = 100  # DPI para la figura, ajustar según sea necesario

move_fig = Figure(figsize=fig_size, dpi=dpi) #Declarar dimensiones de la gráfica
plt.style.use(plt_style) #Implementar estilo de gráfico
move_fig.subplots_adjust(hspace = row_spacing1) #Ajuste de espacio entre subplots
ax1 = move_fig.add_subplot(211)  # Primer subplot
ax2 = move_fig.add_subplot(212)  # Segundo subplot

# Colocar la nueva figura y subgráficas
health_fig = Figure(figsize=fig_size, dpi=dpi)
health_fig.subplots_adjust(hspace=row_spacing2)  # Ajustar espacio entre subgráficas
ax3 = health_fig.add_subplot(211)  # Primer subplot para datos de salud
ax4 = health_fig.add_subplot(212)  # Segundo subplot para datos de salud

# Crear la figura y los subgráficos para Pro View
pro_view_fig = Figure(figsize=fig_size, dpi=dpi)
pro_view_fig.subplots_adjust(hspace=row_spacing1, wspace=row_spacing2)  # Ajustar espacio entre subgráficas
# Añadir subgráficas para los datos de movimiento en la primera columna
ax5 = pro_view_fig.add_subplot(221)  # Primer subplot para datos de movimiento (Gyroscope)
ax6 = pro_view_fig.add_subplot(222)  # Segundo subplot para datos de movimiento (Accelerometer)
# Añadir subgráficas para los datos de salud en la segunda columna
ax7 = pro_view_fig.add_subplot(223)  # Tercer subplot para datos de salud (Heartrate)
ax8 = pro_view_fig.add_subplot(224)  # Cuarto subplot para datos de salud (Galvanic Skin Response)

def display_movement_view():
    global move_fig, lines, lines2, ani_move_fig
    # Agregar gráficas de MOVEMENT VIEW
    canvas_fig = FigureCanvasTkAgg(move_fig, master=root)
    canvas_move_fig_widget = canvas_fig.get_tk_widget()
    # Colocar el canvas en la posición deseada, ajustando según sea necesario
    canvas_move_fig_widget.place(x=screen_width*0.28, y=screen_height * 0.09)
    threading.Thread(target=ani_move_view).start()
    
# Función para visualizar la salud
def display_health_view():
    global health_fig, lines3, lines4,ani_health_fig
    #Agregar gráficas de HEALTH VIEW
    canvas_fig = FigureCanvasTkAgg(health_fig, master=root)
    canvas_health_fig_widget = canvas_fig.get_tk_widget()
    canvas_health_fig_widget.place(x=screen_width * 0.28, y=screen_height * 0.02)
    threading.Thread(target=ani_health_view).start()

# Función para crear un nuevo canvas con 4 gráficas divididas en 2 columnas y 2 filas
def display_pro_view():
    global pro_view_fig

    # Agregar la figura al canvas y mostrarla
    canvas_fig = FigureCanvasTkAgg(pro_view_fig, master=root)
    canvas_pro_view_fig_widget = canvas_fig.get_tk_widget()
    # Colocar el canvas en la posición deseada, ajustando según sea necesario
    canvas_pro_view_fig_widget.place(x=screen_width * 0.28, y=screen_height * 0.05)
    #Iniciar la animación de las lineas
    threading.Thread(target=ani_pro_view).start()

def csv_data_write():
    data = M5data()
    sample_data = {"Sample": sample_counter, "Gyroscope X": data[0], "Gyroscope Y": data[1], "Gyroscope Z": data[2], 
                    "Accelerometer X": data[3], "Accelerometer Y": data[4], "Accelerometer Z": data[5], "Heartrate": data[6], "GSR": data[7], "Temperature": data[8], "SPO2": data[9]}
    writer.writerow(sample_data)

# Función para actualizar el contenido del Label con la carpeta seleccionada
def update_selected_folder_label():
    updated_folder_label.config(text=folder_selected)

# Declaración de posiciones para elementos alineados a la izquierda
x_position_left_column = 40*scale_factor  # Ajusta según sea necesario
y_position_top = 50*scale_factor   # Ajusta según sea necesario
y_position_increment = 40*scale_factor   # Ajusta según sea necesario
y_position_buttons1 = y_position_top + (480*scale_factor)
y_position_buttons2 = y_position_top + (760*scale_factor)
y_position_buttons3 = y_position_top + (620 * scale_factor)
# Declaración de posiciones para elementos en Health view
x_position_temperature = 850*scale_factor  # Ajusta según sea necesario
y_position_health = 935*scale_factor   # Ajusta según sea necesario

#Declaración de tamaños de fuentes
subtitle_font_size = int(19 * (font_resize_factor))
label_font_size = int(16 * (font_resize_factor))
button_font_size = int(15 * (font_resize_factor))
graph_title_size = int(17 * (font_resize_factor))

# Añadir título a la interfaz
title_label = Label(root, text="Mirai Lab: Pro Signal Viewer", font=("Calibri", int(28 * (font_resize_factor))))
title_label.configure(background='white')
title_label.place(x=x_position_left_column, y=y_position_top+(120*scale_factor))

# Añadir título para Initial Settings
initial_label = Label(root, text="Initial Settings", font=("Calibri", subtitle_font_size))
initial_label.configure(background='white')
initial_label.place(x=x_position_left_column, y=y_position_top + (190*scale_factor))

# Añadir texto al lado del Combobox de Communication port
port_label = Label(root, text="Communication port:", font=("Calibri", label_font_size))
port_label.configure(background='white')
port_label.place(x=x_position_left_column, y=y_position_top + (240*scale_factor))

# Crear Combobox para seleccionar el puerto serial
port_combobox = ttk.Combobox(root, state="readonly", font=("Calibri", button_font_size))
port_combobox.place(x=x_position_left_column, y=y_position_top + (290*scale_factor))

# Añadir texto al lado del Combobox de baud rate
baud_rate_label = Label(root, text="Baud rate:", font=("Calibri", label_font_size))
baud_rate_label.configure(background='white')
baud_rate_label.place(x=x_position_left_column, y=y_position_top + (340*scale_factor))

# Crear Combobox para seleccionar el baud rate
baud_rate_combobox = ttk.Combobox(root, state="readonly", values=baud_rates, font=("Calibri", button_font_size))
baud_rate_combobox.place(x=x_position_left_column, y=y_position_top + (380*scale_factor))
baud_rate_combobox.current(0)  # Selecciona el primer baud rate por defecto

# Mensaje "Port status" para indicar estado del puerto
port_status_msg =  StringVar()
port_status_msg.set("No port")
port_status_text =  Label(root, textvariable=port_status_msg, font=("Calibri", button_font_size))
port_status_text.configure(background='white')
port_status_text.place(x=x_position_left_column+(120*scale_factor), y=y_position_top + (431*scale_factor))

# Label "Port status" para indicar estado del puerto
port_status_label =  Label(root, text="- Port status:", font=("Calibri", button_font_size))
port_status_label.configure(background='white')
port_status_label.place(x=x_position_left_column, y=y_position_top + (430*scale_factor))

# Botón "Connect" para iniciar la comunicación serial
connect_button = Button(root, text="Connect", command=connect_serial, font=("Calibri", button_font_size))
connect_button.place(x=x_position_left_column, y=y_position_buttons1)

# Botón "Disconnect" para detener la comunicación serial
disconnect_button = Button(root, text="Disconnect", command=disconnect_serial, state="disabled", font=("Calibri", button_font_size))
disconnect_button.place(x=x_position_left_column+ (105*scale_factor), y=y_position_buttons1)

# Botón "Update ports" para actualizar los puertos disponibles
update_ports_button = Button(root, text="Update ports", command=update_ports, font=("Calibri", button_font_size))
update_ports_button.place(x=x_position_left_column+ (230*scale_factor), y=y_position_buttons1)

# Añadir título para Initial Settings
view_label = Label(root, text="View Selection", font=("Calibri", subtitle_font_size))
view_label.configure(background='white')
view_label.place(x=x_position_left_column, y=y_position_top + (560*scale_factor))

# Botón para visualizar el movimiento
movement_view_button = Button(root, text="Movement view", font=("Calibri", button_font_size), command=display_movement_view)
movement_view_button.place(x=x_position_left_column, y=y_position_buttons3)

# Botón para visualizar datos de salud
health_view_button = Button(root, text="Health view", font=("Calibri", button_font_size), command=display_health_view)
health_view_button.place(x=x_position_left_column + (160 * scale_factor), y=y_position_buttons3)

# Botón para Pro View
pro_view_button = Button(root, text="Pro view", font=("Calibri", button_font_size), command=display_pro_view)
pro_view_button.place(x=x_position_left_column + (290 * scale_factor), y=y_position_buttons3)

# Añadir título para testing
test_label = Label(root, text="Testing Hub", font=("Calibri", subtitle_font_size))
test_label.configure(background='white')
test_label.place(x=x_position_left_column, y=y_position_top + (700*scale_factor))

# Botón "Select folder" para seleccionar la carpeta de destino
select_folder_button = Button(root, text="Select folder", font=("Calibri", button_font_size), command=select_folder)
select_folder_button.place(x=x_position_left_column, y=y_position_buttons2)

# Crear Label para mostrar el contenido de la carpeta seleccionada
selected_folder_label = Label(root, text="- Folder path:", font=("Calibri", button_font_size), background='white')
selected_folder_label.place(x=x_position_left_column, y=y_position_buttons2+(60*scale_factor))
updated_folder_label = Label(root, text="", font=("Calibri", button_font_size), background='white')
updated_folder_label.place(x=x_position_left_column+(120*scale_factor), y=y_position_buttons2+(60*scale_factor))

# Botón "Start test" para iniciar el muestreo de datos en un archivo CSV
start_test_button = Button(root, text="Start test", font=("Calibri", button_font_size), command=start_test)
start_test_button.place(x=x_position_left_column+(147*scale_factor), y=y_position_buttons2)

# Botón "End test" para detener el muestreo de datos en el archivo CSV
end_test_button = Button(root, text="End test", font=("Calibri", button_font_size), command=end_test, state="disabled")
end_test_button.place(x=x_position_left_column+(270*scale_factor), y=y_position_buttons2)

# Botón "Exit" para cerrar el programa
exit_button = Button(root, text="Exit", height=1, width=8, font=("Calibri", int(20 * (font_resize_factor))), command=exit_program)
exit_button.place(x=x_position_left_column, y=y_position_top + 710)

# Actualizar la lista de puertos disponibles
update_ports()

# Evento de teclado para la tecla "Esc"
root.bind("<Escape>", lambda event: root.destroy())

# Configuración de las líneas
num_lines = 6
x_data, y_data = [[] for _ in range(num_lines)], [[] for _ in range(num_lines)]
# Configuración de las líneas y datos de salud
x_data_health, y_data_health_1, y_data_health_2 = [], [], []

#MOVEMENT VIEW GRAPH ELEMENTS
ax1.set_title('Gyroscope', fontsize= graph_title_size)
ax2.set_title('Accelerometer', fontsize= graph_title_size)
ax1.set_ylabel('Amplitude', fontsize= button_font_size)
ax2.set_ylabel('Amplitude', fontsize= button_font_size)
ax1.set_xlabel('Samples', fontsize=button_font_size)
ax2.set_xlabel('Samples', fontsize=button_font_size)
# Configurar límites de los ejes
ax1.set_ylim(-1000, 1000)
ax2.set_ylim(-4, 4)
# Configuración de las líneas
lines = [ax1.plot([], [], lw=2, linestyle='-')[0] for _ in range(3)]  # Primeras 3 líneas en la primera subgráfica
lines2 = [ax2.plot([], [], color='C{}'.format(i+4), lw=2, linestyle='-')[0] for i in range(3)]  # Últimas 3 líneas en la segunda subgráfica

#HEALTH VIEW GRAPH ELEMENTS
ax3.set_title('Heartrate', fontsize=graph_title_size)
ax4.set_title('Galvanic Skin Response', fontsize=graph_title_size)
ax3.set_ylabel('Amplitude', fontsize=button_font_size)
ax4.set_ylabel('Amplitude', fontsize=button_font_size)
ax3.set_xlabel('Samples', fontsize=button_font_size)
ax4.set_xlabel('Samples', fontsize=button_font_size)
ax3.set_ylim(50, 130)
ax4.set_ylim(15, 45)
lines3 = [ax3.plot([], [], lw=2, linestyle='-')[0] for _ in range(1)]  # Línea para datos de salud
lines4 = [ax4.plot([], [], color='C{}'.format(i + 4), lw=2, linestyle='-')[0] for i in range(1)]  # Línea para datos de salud

# Configurar títulos y etiquetas de los ejes para los subgráficos de movimiento
ax5.set_title('Gyroscope', fontsize=label_font_size)
ax5.set_xlabel('Samples')
ax5.set_ylabel('Amplitude')
ax6.set_title('Accelerometer', fontsize=label_font_size)
ax6.set_xlabel('Samples')
ax6.set_ylabel('Amplitude')

# Configurar títulos y etiquetas de los ejes para los subgráficos de salud
ax7.set_title('Heartrate', fontsize=label_font_size)
ax7.set_xlabel('Samples')
ax7.set_ylabel('Amplitude')
ax8.set_title('Galvanic Skin Response', fontsize=label_font_size)
ax8.set_xlabel('Samples')
ax8.set_ylabel('Amplitude')

# Configurar límites de los ejes
ax5.set_ylim(-1000, 1000)
ax6.set_ylim(-4, 4)
ax7.set_ylim(50, 130)
ax8.set_ylim(15, 45)

# Configuración de las líneas
lines5 = [ax5.plot([], [], lw=2, linestyle='-')[0] for _ in range(3)]  # Primeras 3 líneas en la primera subgráfica
lines6 = [ax6.plot([], [], color='C{}'.format(i+4), lw=2, linestyle='-')[0] for i in range(3)]  # Últimas 3 líneas en la segunda subgráfica
lines7 = [ax7.plot([], [], lw=2, linestyle='-')[0] for _ in range(1)]  # Línea para datos de salud
lines8 = [ax8.plot([], [], color='C{}'.format(i + 4), lw=2, linestyle='-')[0] for i in range(1)]  # Línea para datos de salud

#Ventana not resizable
# root.resizable(0, 0) 

root.mainloop()