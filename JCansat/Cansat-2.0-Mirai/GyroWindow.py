import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QWidget

#plt.style.use('fivethirtyeight')  # Usar un estilo estético para las gráficas

class GyroWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Gyroscope")
        self.main_window = main_window
        self.setWindowState(QtCore.Qt.WindowFullScreen)
        # Configuración del fondo
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QtGui.QPixmap("fondo.png"))  # Cambia la ruta a la de tu imagen
        self.background_label.resize(self.width(), self.height())
        # Ajustes de la figura y estética
        self.fig, self.ax = plt.subplots(figsize=(10, 6), dpi=80)
        self.line_x, = self.ax.plot([], [], label='X', linewidth=2, linestyle='-', color='blue')
        self.line_y, = self.ax.plot([], [], label='Y', linewidth=2, linestyle='-', color='green')
        self.line_z, = self.ax.plot([], [], label='Z', linewidth=2, linestyle='-', color='red')

        # Configuraciones estéticas adicionales
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        self.ax.legend(loc='upper right', frameon=True, shadow=True)
        self.ax.margins(x=0.05, y=0.05)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Value')
        self.ax.set_title('Gyroscope')

        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.back_to_main_window)
        self.back_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.back_button.setFlat(True)
        # Widget de gráfico
        graph_widget = QWidget()
        graph_layout = QVBoxLayout(graph_widget)
        graph_layout.addWidget(self.back_button)
        graph_layout.addWidget(self.fig.canvas)

        # Paneles laterales
        side_layout = QVBoxLayout()
        self.create_label_text_pair("X", side_layout)
        self.create_label_text_pair("Y", side_layout)
        self.create_label_text_pair("Z", side_layout)
        side_layout.addStretch(1)

        main_layout = QHBoxLayout()
        main_layout.addWidget(graph_widget, 1)  # El gráfico tendrá más espacio que los textEdits.
        main_layout.addLayout(side_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Configurando transparencia
        graph_widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        graph_widget.setStyleSheet("background:transparent;")
        central_widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        central_widget.setStyleSheet("background:transparent;")

    def create_label_text_pair(self, label_text, parent_layout):
        label = QLabel(label_text)
        text_edit = QTextEdit()
        text_edit.setMaximumHeight(80)
        text_edit.setMaximumWidth(200)

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(text_edit)
        layout.addStretch(1)

        parent_layout.addLayout(layout)
        setattr(self, f"{label_text.lower()}_text_edit", text_edit)
    def display_graph(self, data):
        # Estos son ejemplos de cómo podrías inicializar las listas en caso de que no existan todavía.
        if not hasattr(self, 'data_x'):
            self.data_x = []
        if not hasattr(self, 'data_y'):
            self.data_y = []
        if not hasattr(self, 'data_z'):
            self.data_z = []

        # Agregamos las nuevas muestras a nuestras listas.
        self.data_x.extend([float(data[3])])
        self.data_y.extend([float(data[4])])
        self.data_z.extend([float(data[5])])
        #print(self.data_x)
        # Si hemos recibido más de 10 muestras, eliminamos las primeras.
        if len(self.data_x) > 20:
            del self.data_x[0]
            del self.data_y[0]
            del self.data_z[0]

        # Establece el límite de y a 100.
        #self.ax.set_ylim(0, 100)
         # Actualizamos el límite de y
        self.ax.set_ylim(min(self.data_x + self.data_y + self.data_z), max(self.data_x + self.data_y + self.data_z))

        # Ahora, simplemente dibuja las listas completas.
        self.line_x.set_data(range(len(self.data_x)), self.data_x)
        self.line_y.set_data(range(len(self.data_y)), self.data_y)
        self.line_z.set_data(range(len(self.data_z)), self.data_z)
        self.ax.set_xlim(0, len(self.data_x) - 1)
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw()
                # Suponiendo que quieres mostrar el último valor de cada lista en los QTextEdit:
        if self.data_x:
            self.x_text_edit.setText(str(self.data_x[-1]))
        if self.data_y:
            self.y_text_edit.setText(str(self.data_y[-1]))
        if self.data_z:
            self.z_text_edit.setText(str(self.data_z[-1]))

    def back_to_main_window(self):
        self.close()
        self.main_window.show()