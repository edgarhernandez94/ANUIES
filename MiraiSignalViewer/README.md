# Signal Viewer Interface Guide

## Introduction
The Signal Viewer interface allows you to visualize and analyze data from a connected device via serial communication. The interface interacts with a device called the Signal Stick, which is a M5 Stack C Plus. The Signal Stick detects variations in position and acceleration, and the data acquired can be visualized and recorded using the Mirai Signal Viewer. The interface has the following appearance.

<img src=https://github.com/elizalanda1/MiraiSignalViewer/blob/main/InterfaceTutorial/1.jpg>

## Setting Up Mirai Signal Viewer
To set up the Mirai Signal Viewer interface and comply with the requirements of the interface, follow these steps:

1. **Locate the Interface Script Folder:**
   - Navigate to the folder containing the script for the Mirai Signal Viewer interface.

2. **Accessing the Terminal:**
   - While in the folder location, open the terminal by typing "cmd" in the address bar of the file explorer and pressing Enter.

3. **Installing Requirements:**
   - Ensure that you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).
   - Locate the `requirements.txt` file in the interface script folder.
   - Open the terminal and navigate to the interface script folder using the `cd` command.
   - Run the following command to install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

4. **Running the Interface:**
   - After installing the requirements, you can run the Mirai Signal Viewer interface using the following command in the terminal:
     ```
     python MiraiSignalViewer.py
     ```
   - This command will start the interface, allowing you to connect and interact with the Signal Stick device.

## Initial Settings
1. **Communication Port Selection:**  
   - Use the dropdown menu labeled "Communication port" to select the port to which your Signal Viewer is connected.
   - Click on the "Update ports" button to refresh the list of available ports.
   <img src=https://github.com/elizalanda1/MiraiSignalViewer/blob/main/InterfaceTutorial/2.jpg width="60%">

2. **Baud Rate Selection:**  
   - Use the dropdown menu labeled "Baud rate" to select a baud rate of 115200.
   <img src=https://github.com/elizalanda1/MiraiSignalViewer/blob/main/InterfaceTutorial/3.jpg width="60%">

3. **Connection Status:**  
   - The status of the selected port will be displayed in the "Port status" label.
   - Once a valid signal is received from the connected device, the animation will start automatically.

## Animation Control
- **Connect/Disconnect:**  
  - Click the "Connect" button to initiate the serial connection and start receiving data.
  - Press the "Disconnect" button to pause the animation and disconnect from the device.
  - To resume the animation, click on the "Connect" button again.
  <img src=https://github.com/elizalanda1/MiraiSignalViewer/blob/main/InterfaceTutorial/4.jpg width="60%">

## Testing Hub
<img src=https://github.com/elizalanda1/MiraiSignalViewer/blob/main/InterfaceTutorial/5.jpg width="60%">

1. **Selecting a Folder:**  
   - Click on the "Select folder" button to choose the directory where the data will be saved.

2. **Starting the Test:**  
   - After selecting the folder, click on the "Start test" button to begin capturing and saving the data.
   - Ensure that the folder is selected before starting the test. You can verify a folder has been selected through the "Folder path" label that is located in the bottom of the Testing Hub

3. **Ending the Test:**  
   - To stop capturing data, click on the "End test" button.
   - This will finalize the data recording process and close the CSV file.
  
## Exit interface
At any given moment, the "Exit" button is enabled to quit running the interface.

