"""
Aventesia J98, J-IOT : jcore
================================================================================
J-IOT for CircuitPython

* Author(s): Sean C. Reichle

Implementation Notes
--------------------
Lots of Credit to Adafruit... yummy fruit.
Lots of Credit to JQuery
Lots of Credit to ThreeJS
Lots of Credit to 98.css

Dynamic Web Server: J988, J-IOT

Tron Soul Core: uique analog wavefrom in phi accelerator envelope
To Encode yourself onto the program, hold analog input pins with fingers on boot(capture).
"""

import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn, AnalogOut
import supervisor
import time
from time import monotonic
import re
import storage
import sys

# RP2040 Set clock frequency
"""
try:
    import microcontroller
    microcontroller.cpus[0].frequency = 125000000
    microcontroller.cpus[1].frequency = 125000000
except:
    pass
"""
 
# WiFi credentials
SSID="WIFI SSID"
SSIDPASSWD="WIFI PASSWORD"

# Start
print("__________________________________")
print("Loading J-HTTP")

# disable auto reload to stop unexpected reloads
supervisor.set_next_code_file(filename = 'code.py', reload_on_error = False, reload_on_success = False)
supervisor.runtime.autoreload = False

jpyOutput = "Server Side jpy script output"
jpyRequest = "Client Request"
jpyRawRequest = ""
jpyClient = ""
jpyHeader = ""
jpyCode = ""
jpyFile = ""

a0 = object
a1 = object
a2 = object
a3 = object
class fakeAnalog:
    value: int
    def __init__(self):
        self.value = 0
        
try:
    a0 = AnalogIn(board.A0)
    a1 = AnalogIn(board.A1)
    a2 = AnalogIn(board.A2)
    a3 = AnalogIn(board.A3)
except:
    a0 = fakeAnalog()
    a1 = fakeAnalog()
    a2 = fakeAnalog()
    a3 = fakeAnalog()
    
    
from jcore import core
# Start the j-iot core
jiot = core()
jiot.setName("J98")
jiot.boot(a0,a1,a2,a3)
jiot.cpuCycle()
jiot.printCycleClock()

# What am I thinking?
import jbrain
from jbrain import jmind
mind = jmind()
jiot.setMind(mind)
jiot.cpuCycle()

import wifi
import socketpool
# jhttp owns board.LED, jpy file execution handler.
from adafruit_jhttpserver import Server, Request, Response, Headers, Redirect, ChunkedResponse, FileResponse, JSONResponse, MIMETypes, GET, POST, PUT, DELETE, REQUEST_HANDLED_RESPONSE_SENT
import mdns

jiot.cpuCycle()
jiot.printCycleClock()

def do_connect(ssid, password):
    wifi.radio.enabled = True
    print('Trying to connect to "%s"...' % ssid)
    try:
        wifi.radio.connect(ssid, password)
    except Exception as e:
        print("Exception", str(e))
    
do_connect(SSID, SSIDPASSWD)
jiot.cpuCycle()
jiot.printCycleClock()

mdns_server = mdns.Server(wifi.radio)
mdns_server.hostname = "jpicoweb"
mdns_server.advertise_service(service_type="_http", protocol="_tcp", port=80)

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool,"/www", debug=True)

@server.route("/")
def base(request: Request):
    return FileResponse(request, "index.jpy", "/www")

@server.route("/cpu", append_slash=True)
def cpu_information_handler(request: Request):
    import microcontroller

    data = {
        "temperature": microcontroller.cpu.temperature,
        "frequency": microcontroller.cpu.frequency,
        "voltage": microcontroller.cpu.voltage,
    }
    return JSONResponse(request, data)

@server.route("/cycle", append_slash=True)
def getCycleClock(request: Request):
    data = {
        "age" : jiot.getAge(),
        "cycle": jiot.getCycleClock(),
    }
    return JSONResponse(request, data)

@server.route("/soul", append_slash=True)
def getCycleClock(request: Request):
    data = {
        "key" : "time-ns:wave1-wave2-wave3-wave4",
        "soul" : jiot.soul,
        
    }
    return JSONResponse(request, data)

# Start the server.
server.start(str(wifi.radio.ipv4_address))
jiot.cpuCycle()
jiot.printCycleClock()

while True:
    try:
        jiot.cpuCycle()
        pool_result = server.poll()
        if pool_result == REQUEST_HANDLED_RESPONSE_SENT:
            # Do something only after handling a request
            jiot.printCycleClock()
            pass

    # If you want you can stop the server by calling server.stop() anywhere in your code
    except OSError as error:
        print (jiot.cpuCycle())
        print(error)
