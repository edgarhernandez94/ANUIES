# Pro Signal Viewer Interface Guide

## Introduction
The Pro Signal Viewer interface allows you to visualize and analyze data from a connected device via serial communication. The interface interacts with an M5 device coupled with varios sensors. The system detects variations in position, acceleration, as well as added features such as Heartrate, Galvanic Skin Response, Temperature and Oxygen Saturation of blood. The data acquired can be visualized using the Pro Signal Viewer. The interface has the following appearance.

<img src=https://github.com/elizalanda1/ProSignalViewer/blob/main/Interface_Instructions/1.jpg>

## Setting Up Mirai Signal Viewer
To set up the Mirai Signal Viewer interface and comply with the requirements of the interface, follow these steps:

1. **Locate the Interface Script Folder:**
   - Navigate to the folder containing the script for the Pro Signal Viewer interface.

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
     python SignalProViewer.py
     ```
   - This command will start the interface, allowing you to connect and interact with the different devices.

## Initial Settings
1. **Communication Port and Baud Rate Selection:**  
   - Use the dropdown menu labeled "Communication port" to select the port to which your devices are connected.
   - If not visible, click on the "Update ports" button to refresh the list of available ports.
   - Moreover, use the dropdown menu labeled "Baud rate" to select a baud rate of 9600.
   <img src=https://github.com/elizalanda1/ProSignalViewer/blob/main/Interface_Instructions/2.jpg width="60%">

2. **Connection Status:**  
   - Click the "Connect" button to initiate the serial connection and start receiving data.
   - The status of the selected port will be displayed in the "Port status" label.
   - Press the "Disconnect" button to pause the animation and disconnect from the device.
   <img src=https://github.com/elizalanda1/ProSignalViewer/blob/main/Interface_Instructions/3.jpg width="60%">

## Animation View Selection
<img src=https://github.com/elizalanda1/ProSignalViewer/blob/main/Interface_Instructions/4.jpg width="60%">

- **Movement view:**  
  - Once connected click on the "Movement view" button, the animation shall display on the right side of the screen.
  - The data regarding the position and acceleration will start being animated.

**To change from one view to another, first disconnect from the current view and select the new one**

- **Health view:**  
  - Click on the "Connect" button and once again select "Health view", the animation shall display on the right side of the screen.
  - The data regarding Heartrate, Galvanic Skin Response, Temprature and Oxygen Saturation will be animated.

**To change from one view to another, first disconnect from the current view and select the new one**

 - **Pro view:**
  - Click on the "Connect" button and once again select "Pro vie", the animation shall display on the right side of the screen.
  - In this view, all previosly mentioned data will be animated.

## Testing Hub
<img src=https://github.com/elizalanda1/ProSignalViewer/blob/main/Interface_Instructions/5.jpg width="60%">

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
<img src=https://github.com/elizalanda1/ProSignalViewer/blob/main/Interface_Instructions/6.jpg width="60%">
