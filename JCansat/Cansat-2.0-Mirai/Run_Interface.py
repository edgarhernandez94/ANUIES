import subprocess

# Ejecutar el script de Python
subprocess.call(["python", "finalmain.py"])

# Minimizar la ventana de la consola
subprocess.call(["powershell", "-command", "$window = (Get-Process -Name python).MainWindowHandle; ShowWindow $window 2"])
