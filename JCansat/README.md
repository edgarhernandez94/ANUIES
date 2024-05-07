<p align="center">
  <img src="https://pbs.twimg.com/profile_images/1356640339180707841/lFpJ-GjN_400x400.jpg"/>
</p>

# J-CANSAT

J-CANSAT is an educational project that combines the concept of CanSat (a miniature satellite) with innovative technology. This repository contains the code and resources related to the J-CANSAT project.

## Description

The goal of the J-CANSAT project is to provide students and enthusiasts with a hands-on experience in the development and operation of a CanSat. A CanSat is a soda can-sized device that integrates various components such as PCB boards, sensors, communication modules, and data storage. It enables simulated satellite missions, collecting and transmitting real-time data.

This repository includes the necessary source code for programming and controlling the CanSat, as well as design files for 3D printing the CanSat casing. In addition, it provides technical documentation, user manuals, and other useful resources to help users understand and effectively utilize the CanSat.

## Features

- Source code for CanSat programming
- Design files for 3D printing the CanSat casing
- Technical documentation and user manuals
- Additional resources such as libraries and configuration files

## Requirements

- Compatible hardware platform (specify required platform)
- Programming and configuration software (specify required software)

# J-CANSAT Manual

This README file serves as a reference manual for the J-CANSAT project. It provides detailed instructions on the setup, assembly, programming, and usage of the CanSat.

## Manual Contents

1.  [Introduction](#Introduction)
   - Overview of CanSat and its applications
   - Purpose and objectives of the manual

2. [System Requirements](#system-requirements)
   - Compatible hardware platform
   - Software required for CanSat programming and configuration

3. [Initial Setup](#initial-setup)
   - Installation of the development environment
   - Configuration of necessary tools and libraries

4. [CanSat Assembly](#cansat-assembly)
   - Step-by-step instructions for physical assembly of the CanSat
   - Connections and wiring between components

5. [CanSat Programming](#cansat-programming)
   - Description of compatible programming languages
   - Code examples and step-by-step programming guide

6. [Sensor and Module Configuration](#sensor-and-module-configuration)
   - Instructions for configuring and calibrating the sensors included in the kit
   - Integration of communication and data storage modules

7. [Usage and Operation](#usage-and-operation)
   - Instructions for CanSat usage before, during, and after the mission
   - Data collection and analysis

9. [Troubleshooting](#troubleshooting)
   - List of common issues and possible solutions

10. Additional Resources
   - Links to technical documentation, tutorials, and useful external resources

## Introduction

Welcome to the J-CANSAT manual! This section provides an overview of CanSat and its applications, as well as the purpose and objectives of this manual.

### Overview of CanSat

CanSat is a miniature satellite that fits inside a standard-sized soda can. It is designed to perform various scientific missions and experiments, mimicking the functionality of a real satellite. CanSats are used in educational settings to provide hands-on experience in aerospace engineering, data collection, and analysis.

### Applications of CanSat

CanSats have a wide range of applications across various fields, including:

- Weather forecasting and atmospheric studies
- Environmental monitoring and pollution analysis
- Remote sensing and imaging
- Communications and signal analysis
- Educational projects and competitions

By building and operating a CanSat, you can gain practical knowledge and skills in satellite development, data analysis, and mission planning.

### Purpose and Objectives of the Manual

The purpose of this manual is to guide you through the process of setting up, assembling, programming, and operating your J-CANSAT. It serves as a comprehensive reference, providing step-by-step instructions, code examples, and troubleshooting tips.

The objectives of this manual are:

1. To provide a clear understanding of the CanSat concept and its applications.
2. To assist you in successfully assembling and programming your J-CANSAT.
3. To enable you to conduct meaningful scientific missions and collect data.
4. To offer guidance in analyzing and interpreting the collected data.
5. To inspire further exploration and experimentation in the field of aerospace engineering.

We hope this manual helps you make the most of your J-CANSAT experience and fosters your interest in satellite development and scientific research.

Let's get started!

## System Requirements

Before getting started with your J-CANSAT project, please ensure that you have the following system requirements:

### Software Requirements

In addition to the hardware platform, you will need the following software for CanSat programming and configuration:

- Windows 10 or higher.
- Arduino IDE
- J-Cansat GUI
- CH340 driver

## Initial Setup

To begin working with the J-CANSAT project, you will need to perform the initial setup, including the installation of the development environment and the configuration of necessary tools and libraries. Follow the steps below to get started:

### Installation of the Development Environment

1. **Windows 10 or higher:** Ensure that you have a compatible Windows operating system. The J-CANSAT project has been tested on both Windows 10 and Windows 11.

2. **Arduino IDE:** Install the Arduino IDE, which is the integrated development environment used for programming the CanSat. You can download the latest version of the Arduino IDE from the official website: [Arduino IDE](https://www.arduino.cc/)

### Configuration of Necessary Tools and Libraries

1. **J-Cansat GUI:** The J-CANSAT project includes a graphical user interface (GUI) that provides a user-friendly interface for configuring and controlling the CanSat. The GUI files are included in the repository. To set up the GUI, follow the instructions provided in the documentation or README file.

2. **CH340 driver:** If you are using a CH340 USB-to-serial adapter for connecting the CanSat to your computer, you will need to install the CH340 driver. The driver files are included in the repository. Refer to the documentation or README file for instructions on installing the CH340 driver.

Make sure to install the latest versions of the required software and drivers to ensure compatibility and access to the latest features and bug fixes.

Once you have completed the initial setup, you are ready to move on to the next steps, such as assembly, programming, and configuration of the CanSat.

## CanSat Assembly

This section provides step-by-step instructions for the physical assembly of the CanSat. Follow these instructions carefully to ensure a successful assembly process.

### Step 1: Gather the Components

Before starting the assembly, gather all the components required for the CanSat. These may include:

- CanSat main body (soda can design or rocket design). Depends of the version.
- Mirai Innovation boards (sensor and communication modules). X1 J-CANSAT NEW MISSION KIT and X1 J-CANSAT THE FUTURE IS NOW KIT
- Sensors (IMU, GPS, altitude sensor, atmospheric pressure). Depends of the version
- Other modules (vision module, camera, SD card, air quality sensor) X1 J-CANSAT THE FUTURE IS NOW KIT
- Wires and connectors
![components](https://github.com/mirai-innovation/JCansat/assets/38308445/c5cc2388-358e-4936-949e-23fef8c19712)

### Step 2: Mount the Mirai Innovation Boards

Carefully mount the Mirai Innovation boards inside the CanSat casing. Ensure proper alignment and secure them in place using the provided mounting brackets or adhesive.
![image](https://github.com/mirai-innovation/JCansat/assets/38308445/d9c0e8a7-9b9e-44af-a6cd-f99d72bde2ae)

| Module 1                                | Module 2                                      | Module 3                 |               
|------------------------------------|------------------------------------------|-------------------------------------|
| Two double 32-pin header strips     | 10k Resistors                             | Five 8-pin headers                   |
| 5mm LED                            | Four long 8-pin header pins               | 2-pin push button                    |
| 220-330 ohm resistor               | 2-pin JST connector                       | 6-pin header                         |
| 7-pin header                        | Female JST connector with cable           | 220 ohm resistor                     |
| 4-pin header                        | Switch                                   | SD module                            |
| Two long 8-pin header pins          | 4-pin header                              | Camera module                        |
| 2-pin JST connector                 | Two 2-pin male headers                    | Temperature module                   |
| Female JST connector with wires     | Two 1-pin male headers                    | CO2 module                           |
| GPS module                          | Charging module                           |                                     |
| Radiofrequency module               | Boost module                              |                                     |
| Arduino Mega Micro                  | IMU module                                |                                     |


### Step 3: Connect the Sensors and Modules

Connect the sensors and modules to their respective ports on the Mirai Innovation boards. Follow the pinout diagrams or instructions provided with the kit to make the correct connections.
#### Module 1.

View 1.
![image](https://github.com/mirai-innovation/JCansat/assets/38308445/e790255b-5c78-44f2-83d2-a5bfdc8de2ad)
View 2.
![image](https://github.com/mirai-innovation/JCansat/assets/38308445/e96d3f5a-8b1b-4850-b695-46d501dac048)

#### Module 2.
View 1. 
![image](https://github.com/mirai-innovation/JCansat/assets/38308445/77cf4c36-224e-4d5e-b7ae-cee081ea7b26)
View 2.
![image](https://github.com/mirai-innovation/JCansat/assets/38308445/2de3cef8-dcd9-4071-88c5-48cd77f86c66)

<!--- (### Step 4: Secure the Wiring

Once all the components are connected, carefully secure the wiring inside the CanSat casing to prevent any loose connections or interference. Use zip ties or tape to organize and secure the wires.

### Step 5: Double-Check the Connections

Before closing the CanSat casing, double-check all the connections to ensure they are properly secured and aligned. This will help prevent any potential issues during operation.

### Step 6: Close the CanSat Casing

If you are using a custom casing, follow the specific instructions provided with the casing to close and seal it properly. For a soda can, ensure that the can is tightly sealed and the components are protected.

Congratulations! You have successfully assembled your CanSat. The next step is to proceed with the programming and configuration process to make it ready for operation.-->


## 5. CanSat Programming

This section provides information on programming the CanSat and includes code examples and a step-by-step programming guide.

### Description of Compatible Programming Languages

The CanSat can be programmed using various programming languages depending on the microcontroller or development board being used. Some of the commonly used languages for CanSat programming include:

- Arduino programming language (based on C/C++)


### Code Examples and Step-by-Step Programming Guide

To help you get started with programming the CanSat, we provide code examples and a step-by-step programming guide. The code examples demonstrate various functionalities and features of the CanSat, such as data collection, sensor integration, communication protocols, and more. The step-by-step programming guide walks you through the process of setting up the development environment, writing code, and uploading it to the CanSat.

Refer to the [CanSat Programming](#cansat-programming) directory in this repository for the code examples and programming guide. Follow the instructions carefully to understand and customize the code according to your project requirements.

Remember to review the comments and documentation within the code examples, as they provide explanations and guidance on how to modify and expand the functionality to suit your specific needs.\

## Uploading Arduino Code to Arduino Mega

Follow these steps to upload the "cansat.ino" code to your Arduino Mega using the Arduino IDE:

1. **Install Arduino IDE**: Download and install the Arduino IDE from the official Arduino website (https://www.arduino.cc/en/software).

2. **Connect the Arduino Mega**: Use a USB cable to connect your Arduino Mega to your computer.

3. **Open Arduino IDE**: Launch the Arduino IDE.

4. **Select the Board**: In the Arduino IDE, go to **Tools** > **Board** and select "Arduino Mega" or "Arduino Mega 2560".

5. **Select the Port**: While still in the **Tools** menu, go to **Port** and choose the appropriate COM port for your Arduino Mega.

6. **Open the Sketch**: Click on **File** > **Open** and locate the "cansat.ino" file on your computer. Open it in the Arduino IDE.

7. **Verify and Compile**: Click the checkmark icon or go to **Sketch** > **Verify/Compile** to compile the sketch and check for any errors.

8. **Upload the Sketch**: Click the right arrow icon or go to **Sketch** > **Upload** to upload the code to your Arduino Mega.

9. **Upload Complete**: Once the upload process is complete, you should see a "Done uploading" message in the status bar.

10. **Verify the Operation**: Observe the behavior of your Arduino Mega to ensure the code is running correctly.

That's it! Your Arduino code (cansat.ino) is now uploaded and running on your Arduino Mega.

Remember to double-check the connections and power supply to ensure proper functionality of your Arduino Mega.

## 6. Sensor and Module Configuration

This section provides instructions for configuring and calibrating the sensors included in the kit, as well as integrating the communication and data storage modules.

### Instructions for Configuring and Calibrating Sensors

To ensure accurate and reliable data collection, it is important to properly configure and calibrate the sensors included in the kit. Follow these instructions to configure and calibrate the sensors:

1. **IMU (Inertial Measurement Unit)**: Connect the IMU sensor to the appropriate pins on the Mirai PCB board. Refer to the provided documentation or pinout diagram for the correct connections. Install any necessary libraries or drivers for the IMU sensor. Configure the sensor settings, such as sampling rate, measurement range, and filtering options, according to your project requirements. Perform sensor calibration if needed, following the instructions provided by the sensor manufacturer.

2. **GPS (Global Positioning System)**: Connect the GPS module to the Mirai PCB board as instructed. Ensure that the GPS antenna has a clear view of the sky for optimal signal reception. Install any required libraries or drivers for the GPS module. Configure the GPS module settings, such as baud rate and update frequency, as per your project needs. Allow sufficient time for the GPS module to acquire satellite signals and obtain accurate positioning information.

3. **Altitude Sensor**: Connect the altitude sensor to the designated pins on the Mirai PCB board. Check the sensor datasheet or documentation for the correct pin configuration. Calibrate the altitude sensor according to the provided instructions. This calibration process usually involves setting the reference altitude or adjusting an offset value to account for local atmospheric conditions.

4. **Atmospheric Pressure Sensor**: Connect the atmospheric pressure sensor to the appropriate pins on the Mirai PCB board. Ensure that the sensor is correctly wired as specified in the documentation. Install any necessary libraries or drivers for the atmospheric pressure sensor. Calibrate the sensor using a known reference pressure value or follow the calibration procedure provided by the sensor manufacturer.

### Integration of Communication and Data Storage Modules

The kit includes communication and data storage modules that enable you to transmit and store data collected by the CanSat. Follow these steps to integrate the communication and data storage modules:

1. **RF (Radio Frequency) Module**: Connect the RF module to the Mirai PCB board according to the pinout instructions. Install any required libraries or drivers for the RF module. Configure the module settings, such as operating frequency and modulation type, based on your project requirements. Implement the necessary protocols and functions to establish communication between the CanSat and ground station.

2. **SD Card Module**: Connect the SD card module to the designated pins on the Mirai PCB board. Ensure that the module is properly connected and oriented. Install any necessary libraries or drivers for the SD card module. Implement the appropriate functions in your code to read and write data to the SD card. Consider file naming conventions and data organization for efficient data storage and retrieval.

Ensure that all connections are secure and properly insulated to avoid any interference or data corruption during operation. Test the sensor and module functionality before the actual deployment of the CanSat.

Refer to the documentation provided with the kit for more detailed instructions on configuring, calibrating, and integrating the sensors and modules. Make sure to follow the recommended best practices and guidelines to ensure accurate data collection and reliable performance of your CanSat.

## 7. Usage and Operation

This section provides instructions for using the CanSat before, during, and after the mission, as well as guidelines for data collection and analysis.

### Instructions for CanSat Usage

Follow these instructions for using the CanSat before, during, and after the mission:

1. **Pre-Mission Preparation**: Before the mission, ensure that the CanSat is fully assembled according to the provided instructions. Double-check all connections and make sure the battery is charged. Review the mission objectives and requirements to ensure proper configuration and settings.

2. **Mission Deployment**: During the mission, carefully position and secure the CanSat inside the launch vehicle or carrier. Ensure that the CanSat is oriented correctly for optimal data collection. Follow all safety protocols and guidelines during the launch or deployment process.

3. **Data Collection**: The CanSat is equipped with various sensors to collect data during the mission. Monitor the data collection process and ensure that all sensors are functioning properly. Take note of any anomalies or unexpected readings.

4. **Data Storage**: The collected data can be stored either onboard the CanSat using the data storage module or transmitted in real-time to a ground station using the communication module. Ensure that the storage or transmission process is uninterrupted and reliable.

5. **Post-Mission Analysis**: After the mission, retrieve the CanSat and carefully examine it for any damage. Download the collected data from the CanSat's storage module or ground station. Analyze the data to gain insights and draw conclusions based on the mission objectives. Compare the collected data with the expected outcomes or predicted values.

### Data Collection and Analysis

To effectively collect and analyze the data from the CanSat, consider the following guidelines:

1. **Data Logging**: Ensure that the data logging process is initiated and functioning correctly. Monitor the data storage capacity and make sure it does not exceed the limits of the storage module or SD card.

2. **Data Retrieval**: Use the appropriate methods to retrieve the collected data from the CanSat's storage module or ground station. Transfer the data to a computer or storage device for further analysis.

3. **Data Analysis**: Apply suitable data analysis techniques and tools to process and interpret the collected data. Utilize statistical methods, visualization tools, or custom algorithms to extract meaningful insights from the data. Consider the mission objectives and the specific parameters being measured.

4. **Result Evaluation**: Compare the collected data with the expected outcomes or predicted values. Evaluate the accuracy and reliability of the measurements. Identify any discrepancies or anomalies that may require further investigation.

5. **Mission Report**: Prepare a mission report summarizing the data collection process, analysis results, and conclusions. Include any recommendations or improvements for future missions based on the findings.

Remember to follow all safety guidelines and legal requirements during the usage and operation of the CanSat. Document all procedures and observations for future reference and knowledge sharing.

## 8. Troubleshooting

This section provides a list of common issues that you may encounter while using the CanSat and possible solutions to resolve them.

### Common Issues and Solutions

1. **Power-related Issues**:
   - **Issue**: The CanSat does not power on or shuts down unexpectedly.
   - **Solution**: Check the battery connection and ensure it is securely attached. Verify that the battery is charged or replace it with a fully charged one if needed. Double-check the power switch position and make sure it is in the "ON" position.

2. **Sensor Readings Inconsistent or Unreliable**:
   - **Issue**: The sensor readings are inconsistent, fluctuating, or inaccurate.
   - **Solution**: Check the sensor connections and ensure they are properly attached. Verify that the sensor wiring is correct and matches the pin configuration. Calibrate the sensors as per the provided instructions or consult the sensor manufacturer's documentation. Ensure that the sensors are not affected by external interference or environmental factors.

3. **Communication Issues**:
   - **Issue**: The CanSat is unable to establish a connection or transmit data to the ground station.
   - **Solution**: Confirm that the communication module is properly connected and configured. Check the wiring and connections between the CanSat and the ground station. Ensure that the communication frequencies and protocols are set correctly. Test the communication module with known working devices or components to isolate the issue.

4. **Data Storage Problems**:
   - **Issue**: The CanSat fails to store data or encounters errors during the data storage process.
   - **Solution**: Verify the proper connection and configuration of the data storage module. Ensure that the storage medium, such as an SD card, is properly inserted and formatted. Check for any limitations or restrictions on the storage capacity. Test the data storage functionality with a small amount of data to confirm its proper operation.

5. **Software Errors or Code Issues**:
   - **Issue**: The CanSat behaves unexpectedly or does not execute the desired functions.
   - **Solution**: Review the code for any syntax errors, logic flaws, or compatibility issues. Check the libraries and dependencies for compatibility with the specific hardware and software versions. Debug the code by adding debug statements or utilizing the Serial Monitor for troubleshooting. Consult online forums, documentation, or community resources for code-related issues.

If you encounter an issue that is not listed above or if the provided solutions do not resolve the problem, consider seeking assistance from the kit's manufacturer or consulting the available support channels. Document any troubleshooting steps and findings for future reference.

## 9. Additional Resources

This section provides a list of additional resources that can be helpful for further understanding and working with the CanSat kit.

### Technical Documentation

- [CanSat Kit User Manual](link-to-user-manual): Refer to the official user manual provided with the CanSat kit for detailed instructions on assembly, configuration, and usage.

- [Sensor Datasheets](link-to-sensor-datasheets): Access the datasheets for the sensors included in the kit to understand their specifications, pin configurations, and recommended usage guidelines.

### Tutorials and Guides

- [CanSat Assembly Tutorial](link-to-assembly-tutorial): Follow a step-by-step tutorial that demonstrates the assembly process of the CanSat, including the placement of components and wiring connections.

- [Programming Guide for CanSat](link-to-programming-guide): Explore a comprehensive guide that covers various programming aspects of the CanSat, including code examples, libraries, and troubleshooting tips.

### Online Communities and Forums

- [CanSat Forum](link-to-cansat-forum): Engage with a community of CanSat enthusiasts, where you can share your experiences, ask questions, and exchange knowledge with other users.

- [Arduino Forum](link-to-arduino-forum): Join the Arduino community forum to seek advice, discuss programming challenges, and connect with Arduino enthusiasts.

### Video Tutorials

- [CanSat Kit Assembly Video](link-to-assembly-video): https://www.youtube.com/watch?v=6z1HlNjEK00&ab_channel=MiraiInnovation Watch a detailed video tutorial that guides you through the assembly process of the CanSat, providing visual instructions and tips along the way.

- [CanSat Programming Tutorial](link-to-programming-tutorial): Access a video tutorial series that walks you through the programming aspects of the CanSat, covering code examples and demonstrations.

These resources should provide valuable guidance and support as you explore and work with the CanSat kit. Make sure to refer to the official documentation and seek assistance from the kit's manufacturer or online communities if you have specific questions or challenges.


