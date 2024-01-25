import board
import busio
from supervisor import runtime
from sys import stdin, stdout
try:
    from typing import Dict, Tuple
except ImportError:
    pass
    
class serialTerminal:
    connected:bool
    uart:object
    uartTxBuffer:str
    uartRxBuffer:str
    serialLog:str
    uartPort:int
    uartSpeed:int    
    
    def __init__(self):
        self.connected = 0
        self.uartPort = 1 
        self.uartPortPins = {'tx':'TX', 'rx':'RX'}
        self.uartSpeed = 115200 
        self.uartTxBuffer=""
        self.uartRxBuffer=""
        self.serialLog = ""
        #txPin = self.uartPortPins['tx']
    
    #-----------------------------------------------------------------
    # Serial Terminal Program
    def connect(self):
        ret = 0
        if not self.connected:
            try:
                self.uart = busio.UART(board.TX, board.RX, baudrate=self.uartSpeed, timeout=0)
                ret = 1
                self.log("Connected")
            except:
                self.log("UART Open Failure.")
        return ret
        
    #-----------------------------------------------------------------
    def serialTerminalProgram(self):
        self.connected = self.connect()
        quitTerminal = False
        if self.connected:
            while quitTerminal == False:
                databuffer = self.uart.read(32)
                if databuffer is not None :
                    data_string = ''.join([chr(b) for b in databuffer])
                    print(str(data_string))
                
                key = runtime.serial_bytes_available
                if key:
                    print("uart >")
                    cmd = input()
                    if cmd == "exit":
                        return 0
                    self.uart.write(bytearray(cmd+chr(13)+chr(10)))
                    key=""  
        else:
            wait = self.getKeyboard()
    
    #-----------------------------------------------------------------
    def log(self, newlogdata):
        self.serialLog = self.serialLog + newlogdata + "<br>"
    #-----------------------------------------------------------------
    def getLog(self):
        ret = self.serialLog
        self.serialLog = ""
        return ret
    #-----------------------------------------------------------------
    def setTX(self, sendData):
        self.uartTxBuffer = uartTxBuffer + sendData
        self.tx()
        self.rx()
    #-----------------------------------------------------------------
    def clearBuffers(self):
        self.uartTxBuffer=""
        self.uartRxBuffer=""
    #-----------------------------------------------------------------
    def clearLog(self):
        self.serialLog = ""
    #-----------------------------------------------------------------
    def tx(self):
        if self.connected:
            self.uart.write(bytearray(self.uartTxBuffer))
            self.uartRxBuffer = ""
        pass
    #-----------------------------------------------------------------
    def rx(self):
        if self.connected:
            databuffer = self.uart.read(32)
            if databuffer is not None :
                data_string = ''.join([chr(b) for b in databuffer])
                self.uartRxBuffer = self.uartRxBuffer + data_string
    #-----------------------------------------------------------------
    def getRX(self):
        if len(self.uartRxBuffer) == 0:
            if not self.connected:
                self.connect()
            self.rx()
        
        if len(self.uartRxBuffer) > 0:
            ret = self.uartRxBuffer
            self.uartRxBuffer = ""
            
        return ret
    #-----------------------------------------------------------------
    def getKeyboard(self):
        while not runtime.serial_bytes_available:
            pass
        keyIn = stdin.read(1)
        return(keyIn)        
