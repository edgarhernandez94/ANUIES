# FES Control Interface Guide

## Introduction
The FES Control Interface allows you to control Functional Electrical Stimulation (FES) channels via a graphical user interface. You can activate or deactivate specific channels using the provided buttons.

<img src=https://github.com/elizalanda1/FES_Interface/blob/main/FESInterfaceTutorial/1.jpg>

## Setting Up the Interface
Follow these steps to set up the FES Control Interface:

1. **Locate the Interface Script Folder:**
   - Navigate to the folder containing the script for the FES Control Interface.

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
     python Interface_elements.py
     ```
   - This command will start the interface, allowing you to connect and interact with the Signal Stick device.

## Initial Settings

1. **Select Communication Port:**
   - Choose a communication port from the dropdown menu labeled "Communication Port".
   - If the desired port is not listed, click the "Update Ports" button to refresh the port list.
   <img src=https://github.com/elizalanda1/FES_Interface/blob/main/FESInterfaceTutorial/2.jpg width="60%">

2. **Connect to the Device:**
   - Click the "Connect" button to establish a connection with the selected port.
   - Once connected, the button text will change to "Disconnect".
   <img src=https://github.com/elizalanda1/FES_Interface/blob/main/FESInterfaceTutorial/3.jpg width="60%">

3. **Activate FES Channels:**
   - Use the buttons labeled "Channel 1", "Channel 2", "Channel 3", and "Channel 4" to activate individual FES channels.
   - To activate all channels simultaneously, click the "Activate All" button.
   <img src=https://github.com/elizalanda1/FES_Interface/blob/main/FESInterfaceTutorial/4.jpg width="60%">
  
4. **Deactivate FES Channels:**
   - To deactivate individual channels, click the "Disconnect" button corresponding to the channel.
   - To deactivate all channels simultaneously, click the "Disconnect All" button.
   <img src=https://github.com/elizalanda1/FES_Interface/blob/main/FESInterfaceTutorial/5.jpg width="60%">

5. **Exit the Interface:**
   - Click the "Exit" button or press the "Esc" key to close the interface.
   <img src=https://github.com/elizalanda1/FES_Interface/blob/main/FESInterfaceTutorial/6.jpg width="60%">

