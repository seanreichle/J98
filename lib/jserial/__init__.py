"""
Aventesia Jarvis
================================================================================

Jarvis for CircuitPython

* Author(s): Sean C Reichle

Implementation Notes
--------------------


jserial 
"""

import board
import busio
from supervisor import runtime
from sys import stdin, stdout
import digitalio
from digitalio import DigitalInOut, Direction, Pull


connected = False
myuart:object
uartTxPort:object
uartTxBuffer:str
uartRxPort:object
uartRxBuffer:str

serialLog:str
uartSpeed:int    

def connect():
    try:
        myuart = busio.UART(uartTxPort, uartRxPort, baudrate=uartSpeed, timeout=0)
        connected = True
    except:
        pass

def clearLog():
    serialLog = ""
    uartRxBuffer = ""
    uartTxBuffer = ""
    
def monitor(txPin, rxPin, speed=115200):
    uartTxPort = txPin
    uartRxPort = rxPin
    uartSpeed = speed
    serialLog = ""
    uartRxBuffer = ""
    uartTxBuffer = ""
    while not connected:
        connect()
    
    if connected:
        databuffer = myuart.read(32)
        if databuffer is not None :
            data_string = ''.join([chr(b) for b in databuffer])
            uartRxBuffer += data_string
            return str(uartRxBuffer)
    
    
    