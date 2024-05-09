This documents explains the steps to obtain raw data from AURA software by
Lab Stream Layer (LSL) protocol using Python programming language. 
For information about LSL, please refer to: 
https://labstreaminglayer.readthedocs.io/

Steps:
1) Open AURA software and start reading EEG signals. 

2) Click the "LSL checkbox" located above the graphs to start streaming the raw EEG data. AURA software automatically generates an LSL stream layer called "AURA". 

3) In order to visualize the raw EEG data, run the following file: 1_LSL_read_raw_data.py

4) In order to filter the raw data coming from 'AURA' LSL stream, run the follwing file: 2_LSL_filter_raw_data.py   
This script will read the raw data, filtering and generate a new stream called: "AURAFilteredEEG"

5) In order to compute the Bandpower of the filtered data run the following file: 
This file receives an LSL stream of eight EEG channels with filtered EEG data called "AURAFilteredEEG"
The output is a 40 channel stream called 'EEG_BANDPOWER_X' contaning normalized bandpower values from input channels in the following form:

Delta CH1
Delta CH2
.
.
Delta CH8

Theta CH1~CH8
Alpha CH1~CH8
Beta CH1~CH8
Gamma CH1~CH8  

 
