"""
Author: Ramon Rodriguez
Date: 3/24/2024
Description: This python script demonstrates how to interact with serial ports
             on your system. It lists available ports, prompts the user to select
             one, configures serial communication settings, and opens the serial
             connection.
"""
 
#Importing the list_ports module from the serial.tools package
import serial.tools.list_ports

#Obtaining a list of available serial ports using the list_ports module,
#and assigning it to the variable 'ports'
#Creating a new serial instance for communication with devices
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

#Initializing an empty list to store the available serial ports
portslist = []

#Iterating through each port in the 'ports' list obtained earlier,
#converting it to a string, appending it to 'portslist' and printing it
for onePort in ports:
    portslist.append(str(onePort))
    print(str(onePort))

#Asking the user to select a port by inputting the COM port number
val = input("Select Port: COM")

#Searching for the selecting port in the list of available ports and storing it in 'portVar'
for x in range(0,len(portslist)):
    if portslist[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

#Configuring serial communication settings
serialInst.baudrate = 115200
serialInst.port = portVar

#Opening the serial connection
serialInst.open()

while True:
    command = input("Send Command: ")
    serialInst.write(command.encode('utf-8'))

    if command == 'exit':
        exit()