import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mapa con Google Maps")
        self.setGeometry(100, 100, 800, 600)

        # Crear una vista de WebEngine
        self.map_view = QWebEngineView(self)
        self.setCentralWidget(self.map_view)

        # Cargar el mapa de Google Maps
        self.load_google_maps()

    def load_google_maps(self):
        # Reemplaza 'TU_CLAVE_DE_API' con tu propia clave de API de Google Maps
        api_key = 'AIzaSyDpzjZlUy9R6r4-l5ZMRajrRbvP8gEX_I8'
        latitude = 37.7749  # Reemplaza con la latitud deseada
        longitude = -122.4194  # Reemplaza con la longitud deseada

        html = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Google Maps</title>
                <style>
                    html, body, #map {{
                        height: 100%;
                        margin: 0;
                        padding: 0;
                    }}
                </style>
            </head>
            <body>
                <div id="map"></div>
                <script src="https://maps.googleapis.com/maps/api/js?key={api_key}"></script>
                <script>
                    function initMap() {{
                        var center = {{ lat: {latitude}, lng: {longitude} }};
                        var map = new google.maps.Map(document.getElementById('map'), {{
                            center: center,
                            zoom: 14
                        }});
                    }}
                    initMap();
                </script>
            </body>
            </html>
        '''

        self.map_view.setHtml(html)


# Crear la aplicación
app = QApplication(sys.argv)

# Crear y mostrar la ventana del mapa
window = MapWindow()
window.show()

# Ejecutar la aplicación
sys.exit(app.exec())
