import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from cansatgui2 import Ui_MainWindow
from SplashScreen import SplashScreen
import keyboard
import threading
import time
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    time.sleep(4)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    def close_app(e):
        if e.name == 'esc':
            app.quit()
    esc_thread = threading.Thread(target=keyboard.on_press_key, args=('esc', close_app))
    esc_thread.start()
    sys.exit(app.exec_())