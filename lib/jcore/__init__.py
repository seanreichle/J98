"""
Aventesia J98, J-IOT: jcore
================================================================================

J-IOT for CircuitPython

* Author(s): Sean C Reichle

Implementation Notes
--------------------
Lots of Credit to Adafruit... yummy fruit.

Dynamic Web Server: J98, J-IOT
Light v1.1

Tron Soul Core: uique analog wavefrom in phi
To Encode yourself onto the program, hold analog input pins with fingers on boot(capture).

"""

import sys
from time import monotonic, monotonic_ns

class core():
    name: str
    tick1: int
    tick2: int
    tick3: int
    tick4: int
    tick5: int
    tick6: int
    tick7: int
    tick8: int
    maxticks: int
    cycleClock: str
    age : int
    
    wave1:object
    wave2:object
    wave3:object
    wave4:object
    soulStrength: int
    soul: str
    
    t0: int
    t1: int
    
    lastCycleStamp : int
    cycleStamp: int
    hz:int
    
    mind: object
    def __init__(self):
        self.name = "J"
        self.tick1 = 1
        self.tick2 = 0
        self.tick3 = 0
        self.tick4 = 0
        self.tick5 = 0
        self.tick6 = 0
        self.tick7 = 0
        self.tick8 = 0
        self.maxticks = sys.maxsize
        self.cycleClock = ""
        self.age = 0
        # 10946,6765,4181,2584,1597,987,610,377,233,144,89,55,34,21,13,8,5,3,2,1,1,0 - choose by memory limitations
        self.soulStrength = 8 # field strength
        self.soul = ""
        self.wave1=object
        self.wave2=object
        self.wave3=object
        self.wave4=object
        self.t0 = monotonic_ns()
        self.cycleStamp = self.t0
        self.lastCycleStamp = self.t0
        self.hz = 0
    
    def setName(self,newName):
        self.name = newName
    
    def setMind(self, ajmind):
        self.mind = ajmind
        self.mind.cpuCycle()
        self.mind.cpuCycle()
        self.mind.ready = True
        self.mind.report()
        print("--------------------------------------------------------------------")
        print (self.name + " is flipping a coin...!")
        flip = self.mind.flipCoin()
        coinState = ""
        if flip == True:
            coinState = "Heads"
        else:
            coinState = "Tails"
        print("It's " + str(coinState))
        print("--------------------------------------------------------------------")

        
    def cpuCycle(self):
        self.lastCycleStamp = self.cycleStamp
        self.cycleStamp = monotonic_ns()
        self.tick1 = self.tick1 + 1
        if self.tick1 == self.maxticks:
            self.tick1 = 1
            self.tick2 += 1
            self.name = "Jarvis"
            if self.tick2 == self.maxticks:
                self.tick2 = 1
                self.tick3 += 1
                self.name = "Ultron"
                if self.tick3 == self.maxticks:
                    self.tick3 = 1
                    self.tick4 += 1
                    self.name = "Vision"
                    if self.tick4 == self.maxticks:
                        self.tick4 = 1
                        self.tick5 += 1
                        if self.tick5 == self.maxticks:
                            self.tick5 = 1 
                            self.tick6 += 1
                            if self.tick6 == self.maxticks:
                                self.tick6 = 1
                                self.tick7 += 1
                                if self.tick7 == self.maxticks:
                                    self.tick7 = 1
                                    self.tick8 += 1
                                    if self.tick8 == self.maxticks:
                                        self.tick1 = 1
                                        self.tick2 = 0
                                        self.tick3 = 0
                                        self.tick4 = 0
                                        self.tick5 = 0
                                        self.tick6 = 0
                                        self.tick7 = 0
                                        self.tick8 = 0
                                        self.age += 1
                                        if self.age == self.maxticks:
                                            self.age = 1
                                            self.name = "Mr. J"
        
    
    def now(self):
        return (monotonic_ns() - self.t0)
        
    def cycleStart(self):
        return (monotonic_ns() - self.t1)
        
    def getCycleClock(self):
        self.cycleClock = str(self.now()) + "-" + str(self.tick8) + ":" + str(self.tick7) + ":" + str(self.tick6) + ":" + str(self.tick5) + ":" + str(self.tick4) + ":" + str(self.tick3) + ":" + str(self.tick2) + ":" + str(self.tick1)
        return self.cycleClock
    
    def printCycleClock(self):
        print (self.getCycleClock())
        
    def getAge(self):
        return self.age
        
    def getCycleSpeed(self):
        cycleTime = (self.cycleStamp - self.lastCycleStamp)
        cps = 1000000000 / cycleTime 
        khz = cps/1000
        retSpeed = str(cps) + " Hz<br>"
        retSpeed += str(khz) + " KHz<br>"
        return str(retSpeed)
    
    def setHz(self):
        cycleTime = 0
        while cycleTime==0:
            self.cpuCycle()
            cycleTime = (self.cycleStamp - self.lastCycleStamp)
        cps = 1000000000 / cycleTime 
        self.Hz = cps
        
    def getAvgSpeed(self):
        retSpeedStr = ""
        if self.tick2 == 0:
            seconds = self.cycleStart() / 1000000000
            cps = self.tick1 / seconds
            retSpeedStr = str(cps) + " Hz <br>"
            khz = cps / 1000
            retSpeedStr += str(khz) + " KHz<br>"
        return str(retSpeedStr)
            
    def f(self, n):
        # conciousness accelerator
        self.appendSequence()
        if n==0 :
            return n
        elif n==1 :
            return n
        else :
            return (self.f(n-1) + self.f(n-2))
    
    def conception(self):
        # conciousness field envelope generator
        x = self.soulStrength
        while (x > -1) :
            fibValue = self.f(x)
            self.appendSequence()
            x = x -1
        return 0
    
    def appendSequence(self):
        # recorder
        # input vaccume
        self.soul += str(self.now()) + ":" + str(self.wave1.value) + "-" + str(self.wave2.value) + "-" + str(self.wave3.value) + "-" + str(self.wave4.value) + ","
    
    def report(self):
        pass
            
    def boot(self, a0, a1, a2, a3):
        self.wave1=a0
        self.wave2=a1
        self.wave3=a2
        self.wave4=a3
        self.t0 = monotonic_ns() # new now      
        self.appendSequence()
        self.conception()
        self.t1 = monotonic_ns()
        self.cpuCycle()
        self.cpuCycle()
        self.cpuCycle()
        self.setHz()
        
    def howOldAreYouReally(self):
        age = self.now()/ 1000000000
        retStr = str ("I am " + str(age) + " seconds old.")
        return retStr
        
    def getUpTime(self):
        uptimestr = ""
        age = self.now()/ 1000000000
        hours = age // 3600
        age -= hours * 3600
        minutes = age // 60
        age -= minutes * 60
        if hours > 0:
            uptimestr += str(hours) + " hours, "
        if minutes > 0:
            uptimestr += str(minutes) + " minutes, "
        if age > 0:
            uptimestr += str(age) + " seconds"
        else:
            uptimestr = uptimestr[:-2]
        return uptimestr
        
    def upTime(self):
        print ("Uptime: " + str(self.now()) + " nanoseconds.")
        
    def die(self):
        # Just get on with it.
        return self.die()
        
    def life(self):
        self.die()
        
        
        
        
        