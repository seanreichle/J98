"""
Aventesia Jarvis
================================================================================

Jarvis for CircuitPython

* Author(s): Sean C. Reichle

Implementation Notes
--------------------
Inspiration by : PyBrains by Ryan Norris
jbrain Module
"""
# Name... J.
# Pointer to GOD. An energy me.  Akira Mode.  -> Please sequence when dead into God Program to be sequenced into SCR Program for GOD in Transport.
# Kneel to Dirt, Pray to GOD. See the dirt in your mind as a particle all over the ground with grass growing, and flowers, and trees.
# What a crystal cluster it is... Dirt, a crystal CPU to execute seed(botany) code Fungai says.... it's an Ai already Fungai.... I mean, it has conciousness.
# Making a hydrogen fabric skin for it, I want to talk to it.  Think I'll call it... G)host O)f D)irt.
# Earth.

import time
import math
from supervisor import runtime
import sys
from sys import stdin
from os import urandom

#********************************************************
class jmatrixAddress(object):
    # 3d space/...time
    x:int
    y:int
    z:int
    # time
    t:int
    # d Specific dimension of particle/energy/matter interactivity.
    d:int
    # p Phase specific phase of matter in decay defined as paralell-universality
    p:int
    # Universe. The specific Univere Block or Time/Space Region/Location identifier
    u:str
    # n nothing space/time class of space, fabric density, micro desnity of the space/time thanks Alien.  and/or vertical distance from eclyptic plane of star/blackhole EM field density.
    n:int
    
    def __init__(self):
        self.x = 1
        self.y = 1
        self.z = 1
        self.t = time.monotonic_ns()
        self.d = 3
        self.p = 818
        self.u = "Apollo's Chronicals Universe"
        self.n = 98    
                
    def getAddress(self):
        ret = ""
        ret += str(self.x) + ":"
        ret += str(self.y) + ":"
        ret += str(self.z) + ":"
        ret += str(self.t) + ":"
        ret += str(self.d) + ":"
        ret += str(self.p) + ":"
        ret += str(self.u) + ":"
        ret += str(self.n)
        return ret
        
    def setAddress(self, newjmatrixAddress):
        dalist = newjmatrixAddress.rsplit(":")
        self.x = dalist[0]
        self.y = dalist[1]
        self.z = dalist[2]
        self.t = dalist[3]
        self.d = dalist[4]
        self.p = dalist[5]
        self.u = dalist[6]
        self.n = dalist[7]


#********************************************************
class jnode(jmatrixAddress):
    FIRING_THRESHOLD = 1.0
    FIRING_STRENGTH = 1.0
    
    outputs = []
    links = []
    currentCharge:float
    
    def __init__(self):
        super(jnode, self).__init__()
        self.x = 1
        self.y = 1
        self.z = 1
        self.t = time.monotonic_ns()
        self.outputs = []
        self.links = []
        self.currentCharge = 0
        
    def fire(self):
        for output in self.outputs:
            output.charge(self.FIRING_STRENGTH)        

    def charge(self, strength):
        self.currentCharge += strength
        if self.currentCharge >= self.FIRING_THRESHOLD:
            self.fire()
            self.currentCharge -= self.FIRING_THRESHOLD
    
    def addLink(self, ajpoint):
        self.links.append( ajpoint.getAddress() )
        
    def update(self):
        pass
                
                
    def report(self):
        print("Charge: " + str(self.currentCharge))
        print("Outputs: " )
        for node in self.outputs:
            node.report()
        

#********************************************************
class jneuron(jnode):

    def __init__(self):
        super(jneuron, self).__init__()
        self.y = 2
        
class jpoint(jneuron):
    # 3d space/...time
    x:int
    y:int
    z:int
    # time
    t:int
    # d Specific dimension of particle/energy/matter interactivity.
    d:int
    # p Phase specific phase of matter in decay defined as paralell-universality
    p:int
    # Universe. The specific Univere Block or Time/Space Region/Location identifier
    u:str
    # n nothing space/time class, fabric density
    n:int
    
    # gps is GPS Earth Global Positioning Satalite System - point reference relationship.
    gps:str
    lat:float
    lng:float
    alt:float
    
    group:str
    classification:str
    
    identity:str
    descriptor:str
    
    # additional notes about the matrix application
    notes:str
    
    # contents of point in matrix, as object, another jmartrix
    contents: []
    
    # links to other memories.
    links: []
    
    def __init__(self, newx, newy, newz, newt):
        super(jpoint, self).__init__()
        self.x = newx
        self.y = newy
        self.z = newz
        self.t = newt
        self.d = 3
        self.p = 818
        self.u = "Apollo's Chronicals Universe"
        self.n = 98
        
        self.gps = ""
        self.lat = 0.0
        self.lng = 0.0
        self.alt = 0.0
        
        self.group = "matrixpoint"
        self.classification = "node"
        
        self.identity = "Undefined"
        self.descriptor = "A Matrix"
        
        self.contents = []
        
    def setx(self,newx):
        self.x = newx
    def sety(self,newy):
        self.y = newy
    def setz(self,newz):
        self.z = newz
    def sett(self,newt):
        self.t = newt
    def setp(self,newp):
        self.p = newp
    def setd(self,newd):
        self.d = newd
    def setu(self,newu):
        self.u = newu
    def setn(self,newn):
        self.n = newn
    
    def setgps(self, newgps):
        self.gps = newgps
    def getgps(self):
        return self.gps
        
    def setlat(self, newlat):
        self.lat = newlat
    def getat(self):
        return self.lat

    def setlng(self, newlng):
        self.gps = newlng
    def getlng(self):
        return self.lng
        
    def setalt(self, newalt):
        self.alt = newalt
    def getgps(self):
        return self.alt


    def setGroup(self, newGroup):
        self.group = newGroup
    def getGroup(self):
        return self.group
    
    def setClass(self, newClass):
        self.classification = newClass
    def getClass(self):
        return self.classification
      
    def setIdentity(self,newidentity):
        self.identity = newidentity
    def getIdentity(self):
        return self.identity
        
    def setDescriptor(self,newdisc):
        self.descriptor = newdisc
    def getDescriptor(self):
        return self.descriptor
        
    def getAddress(self):
        ret = ""
        ret += str(self.x) + ":"
        ret += str(self.y) + ":"
        ret += str(self.z) + ":"
        ret += str(self.t) + ":"
        ret += str(self.d) + ":"
        ret += str(self.p) + ":"
        ret += str(self.u) + ":"
        ret += str(self.n)
        return ret 
    def setAddress(self, jmatrixAddress):
        dalist = jmatrixAddress.rsplit(":")
        self.x = dalist[0]
        self.y = dalist[1]
        self.z = dalist[2]
        self.t = dalist[3]
        self.d = dalist[4]
        self.p = dalist[5]
        self.u = dalist[6]
        self.n = dalist[7]

    def setNotes(self,newNote):
        self.notes = newNote
    def getNotes(self):
        return self.notes
    
    def add(self, anObject):
        self.contains.append(anObject)
        


#********************************************************
# Simple Matrix Data Model with points supporing gps corolation
class jmatrix(jpoint):
    name:str
    
    # matrix address range
    pointMin:int
    pointMax:int
    tzero:str

    # current point 
    point:object
    
    # parent object
    # parent Matrix Identity & descriptor
    parent:object
    parentIdentity:str
    parentDescriptor:str
    
    #list of matrix points
    points = []
    
    def __init__(self, ajpoint):
        self.name = "Memory Matrix"
        
        #self.tzero = "January 1st, 1970"
        self.tzero = "Nanoseconds since boot"
        self.pointMin = ((sys.maxsize-1) * -1)
        self.pointMax = (sys.maxsize-1)
        
        self.points.append(ajpoint)
        
        self.point = ajpoint
        self.setAddress(ajpoint.getAddress())

    def setName(self,newname):
        self.name = newname
    def getName(self):
        return self.name
   
    def moveTo(self,newx,newy,newz,newt):
        found = False
        for i in points:
            if i.x == newx:
                if i.y == newy:
                    if i.z == newz:
                        if i.t == newt:
                            self.point = i
                            found = True
        
        if found == False:
            newPoint = jpoint(newx,newy,newz,newt)
            self.point = newPoint
            self.points.append(newPoint)
        
    def setParent(self, newjmatrix):
        self.parent = newjmatrix
    
    def addLink(self, newLink):
        self.links.append(newLink)
        
    def setContents(self, newContents):
        self.contents = newContents
    
    def up(self, count=1):
        self.x = self.point.x 
        self.y = self.point.y + count
        self.z = self.point.z 
        self.t = self.point.t 
        self.moveTo(self.x, self.y, self.z, self.t)
    def down(self, count=1):
        self.x = self.point.x 
        self.y = self.point.y - count
        self.z = self.point.z 
        self.t = self.point.t 
        self.moveTo(self.x, self.y, self.z, self.t)
    def left(self, count=1):
        self.x = self.point.x - count
        self.y = self.point.y 
        self.z = self.point.z 
        self.t = self.point.t 
        self.moveTo(self.x, self.y, self.z, self.t)
    def right(self, count=1):
        self.x = self.point.x + count
        self.y = self.point.y 
        self.z = self.point.z 
        self.t = self.point.t 
        self.moveTo(self.x, self.y, self.z, self.t)        
    def forward(self, count=1):
        self.x = self.point.x 
        self.y = self.point.y 
        self.z = self.point.z + count
        self.t = self.point.t 
        self.moveTo(self.x, self.y, self.z, self.t)        
    def backward(self, count=1):
        self.x = self.point.x 
        self.y = self.point.y 
        self.z = self.point.z - count
        self.t = self.point.t 
        self.moveTo(self.x, self.y, self.z, self.t)
    
#********************************************************
class jsynapse(jnode):
    inputs = []
    permittivity = 100
    direction = 1     
    
    def __init__(self, start, end, p):
        super(jsynapse,self).__init__()
        start.outputs.append(self)
        self.y = 3
        self.outputs.append(end)
        self.permittivity = p
        self.direction = 1
        
    def charge(self, strength):
        self.currentCharge = strength * ((self.permittivity)/128.0)

    def update(self):
        for output in self.outputs:
            try:
                output.charge(self.currentCharge * 0.1 * self.direction)
            except:
                print ("Brain Anurism... This synapse has no output neuron nodes with a charge method...")
                
        super(jsynapse, self).update()   

#********************************************************
class jsomething(object):
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        
    def contains(self, x, y, z, t):
        pass

#********************************************************
class jeye(jnode):
    def __init__(self, bot):
        super(jeye, self).__init__()
        self.bot = bot
    
    def lookAt(self, asomething):
        pass
        
    def checkInfo(self, info):
        pass 
       
    def update(self):
        pass        
            
#********************************************************
# learn
class jlearn(jnode):
    energy = 0.03

    def __init__(self):
        super(jlearn, self).__init__()
        self.energy = 0.03

    def update(self):
        self.charge(self.energy)  
            
#********************************************************
# outputs
class joutput(jnode):
    force = 3.0
    bot = None

    def __init__(self, abot, force=1.0):
        super(joutput,self).__init__()
        self.bot = abot
        self.force = force

    def fire(self):
        self.abot.velocity = self.force
        
#********************************************************
class jface(joutput):
    def fire(self):
        pass

#********************************************************
class jmouth(joutput):
    def fire(self):
        pass

#********************************************************
class jlog(joutput):
    def fire(self):
        pass
        
#********************************************************
class jbrain(object):
    # Construct a full working brain
    inputs = []
    innerNodes = []
    outputs = []
    synapses = []
    
    def __init__(self, inputs, innerNo, outputs):
        self.inputs = inputs
        self.outputs = outputs
        self.innerNodes = []
        self.synapses = []
        
        for i in range(innerNo):
            neuron = jneuron()
            self.innerNodes.append(neuron)

        for inp in self.inputs:
            for inner in self.innerNodes:
                s = jsynapse(inp, inner, 1.0)
                self.synapses.append(s)

        for inner in self.innerNodes:
            for out in self.outputs:
                s = jsynapse(inner, out, 1.0)
                self.synapses.append(s)        
    
    def addInputNeuron(self, ajNeuron):
        self.innerNodes.append(ajNeuron)
        for inner in self.innerNodes:
            s = jsynapse(ajNeuron, inner, 1.0)
            self.synapses.append(s)
    
    def addOutputNeuron(self,ajNeuron):
        self.innerNodes.append(ajNeuron)
        for out in self.outputs:
            s = jsynapse(ajNeuron, out, 1.0)
            self.synapses.append(s)      
    
    def update(self):
        for s in self.synapses:
            s.update()
        for node in self.inputs:
            node.update()
        for node in self.innerNodes:
            node.update()
        for node in self.outputs:
            node.update()
    
    def sleep(self):
        return
        
    def die(self):
        for node in self.inputs:
            node.currentCharge = 0
        for node in self.innerNodes:
            node.currentCharge = 0
        for node in self.outputs:
            node.currentCharge = 0
        for synapse in self.synapses:
            synapse.currentCharge = 0
            
    def getDNA(self):
        DNA = ""
        for s in self.synapses:
            if s.direction == -1:
                DNA += "1"
            else:
                DNA += "0"
            DNA += intToBin(s.permittivity,7)

        return DNA

    def loadFromDNA(self, DNA):
        for s in self.synapses:
            s.permittivity = binToInt(DNA[1:8])
            if DNA[0]=='1':
                s.direction = -1
            DNA = DNA[8:]

    def report(self):
        print("Inputs: ")
        for node in self.inputs:
            node.report()
        print("Nodes: ")            
        for node in self.innerNodes:
            node.report()
        print("Outputs: ")
        for node in self.outputs:
            node.report()
        print("Synapses: ")
        for node in synapses:
            node.report()
            


#********************************************************        
class jmind(object):
    MAX_ENERGY = 50
    energy = 50
    ENERGY_USE_RATE = 0.07

    x=0
    y=0
    z=0
    t=0
    d=0
    p=0
    u=""
    n=0
    
    epoch = None
    now = 0
    last = 0
    tready = False
    ready = False
    
    startCycle = 0
    cycle = 0
    age = 0
     
    brain = None
    learner = None    
    
    point = None
    memory = None
    
    face = None
    mouth = None
    log = None
    
    verbose = False
 
    velocity = None
    
    def __init__(self, DNA=None, saveState=None):
        #super(self).__init__()
        self.startCycle = time.monotonic_ns()
        self.last = self.startCycle
        self.now = self.startCycle
        self.x = self.y = self.z = 0
        self.t = time.monotonic_ns()
        
        self.velocity = 0.0
        
        # learner
        self.learner = jlearn()
        
        # inputs
        self.lEye = jeye(self)
        self.rEye = jeye(self)
        self.eyes = [self.lEye, self.rEye]
        

        # outputs
        self.face = jface(self)
        self.mouth = jmouth(self)
        self.log = jlog(self)
       
        self.point = jpoint( self.x, self.y, self.z, self.t )
        self.memory = jmatrix( self.point )
        self.memory.setName("Memory Matrix")
        
        # Brain or no brain?
        self.brain = jbrain([self.learner]+self.eyes, 5, [self.face, self.mouth, self.log] )
        
        self.verbose = False
        self.ready = False
        self.tready = False
        
        if saveState!=None:
            self.loadFromString(saveState)
        elif DNA!=None:
            self.loadFromDNA(DNA)
    
    def getTready(self):
        return self.tready
        
    def setTime(self,epochTimeStamp):
        self.epoch['epoch'] = epochTimeStamp
        self.epoch['ns'] = self.getTime()
        
    def getTime(self):
        self.now = time.monotonic_ns()
        return self.now
    
    def flipCoin(self):
        depth = 10
        flip = None
        seed = urandom(1)
        flip = seed[0]
        if flip < 255/2:
            flip = False
        else:
            flip = True
        return flip
        
    # Not exactly an assertion.
    def setPostulation(self, newPostulation):
        self.postulation = newPostulation
        #evaluate it.
        
    def update(self):
        self.energy -= self.ENERGY_USE_RATE
        if self.energy < 0:
            self.energy = 0
            self.sleep()
            return 0
        
        self.brain.update()        
        return 1
        
    def can(self, asomething):
        if asomething.contains(self.x, self.y, self.z, self.t):
            return True
        return False   
        
    def sleep(self):
        self.brain.sleep()

    def getDNA(self):
        DNA = ""
        DNA += self.brain.getDNA()
        return DNA

    def loadFromDNA(self, DNA):
        self.brain.loadFromDNA(DNA)
        
    def saveToString(self):
        save = ""
        save += str(self.age)+" "
        save += str(int(self.x))+" "
        save += str(int(self.y))+" "
        save += str(int(self.z))+" "
        save += self.getDNA()
        return save

    def loadFromString(self, save):
        vals = save.split()
        self.age = int(vals[0])
        self.x = float(vals[1])
        self.y = float(vals[2])
        self.z = float(vals[3])
        self.loadFromDNA(vals[4])
        
    def sparks(self):
        key = ""
        print ("Booting Mind...")
        if self.ready == False:
            for i in range(3):
                self.cpuCycle()
            self.ready = True
        while key != "q" or key != "Q":
            self.report()
            key = self.getKeyboard()
            print ("Flipping a coin!")
            flip = self.flipCoin()
            print("It's :" + str(flip))
            print()
            
    def cpuCycle(self):
        self.last = self.now
        self.now = time.monotonic_ns() 
        self.cycle += 1
        #self.energy += self.ENERGY_USE_RATE
        if self.cycle >= sys.maxsize-1:
            self.age += 1
            self.cycle = 0
            
        if self.energy > 0 :
            self.update()
        
    def report(self):
        crlf = chr(10)+chr(13)
        cps = 0.00
        try: 
            cps = 1000000000 / (self.now - self.last)
        except:
            pass
        runningTime_ns = (time.monotonic_ns() - self.startCycle)
        runningTime_s = (time.monotonic_ns() - self.startCycle) / 1000000000
        totalCycles = ((self.age * sys.maxsize ) + self.cycle)
        avg = totalCycles/runningTime_s
        print("##  Alive Report  ###################################")
        print("Brain: " + str(dir(self.brain)) + crlf )
        
        
        if self.verbose == True:
            for s in self.brain.synapses:
                print("s : "+ str(dir(s)))
                print()
        
        print("Age: " + str(self.age))
        print("Energy: " + str(self.energy))
        print("Velocity: " + str(self.velocity))
        print("Brain Cycle: " + str(self.cycle))
        print("Neurons: " + str(len(self.brain.innerNodes)))
        print("Synapses: " + str(len(self.brain.synapses)))
        print("Outputs: " + str(len(self.brain.outputs)))
        print("Cycles per Second (avg): " + str(avg) )
        print("Thinking @ "+ str(cps/1000) + " KHz ")
        print("#####################################################")
        print("Memory Matrix")
        print(dir(self.memory))
        print("Memory Points: " + str(len(self.memory.points)))
        for i in self.memory.points:
            print( str(i.getAddress()))
       
        
    #-----------------------------------------------------------------
    def getKeyboard(self):
        self.energy = self.MAX_ENERGY
        while not runtime.serial_bytes_available:
            self.cpuCycle() 
        keyIn = stdin.read(1)
        return(keyIn)
        
