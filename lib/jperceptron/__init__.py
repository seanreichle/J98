'''
Aventesia Jarvis, JIOT 
================================================================================
Jarvis for CircuitPython on Ljinux
J-IOT
* Author(s): Sean C Reichle,..

Implementation Notes
PercepTron Neural Network.

n = network(1.2,0.1,0.9,0.7) #weights
n.apply([1.6,1.5,2,1]) #data

#print(n)
print (n.calc(3)) #threshold 0|1
--------------------
'''
class ineuron:
    weight:float
    activation: float
    oneuron: object
    def __init__(self, j1):
        self.weight = j1
        self.activation = 0
    
    def act(self, x1):
        self.activation = x1 * self.weight
        return self.activation
    
    def __repr__(self):
        print ("weight: "  +str(self.weight)+ " activation: "+ str(self.activation))
        
        
class oneuron:
    output:int
    activation:float
    network:object
    def __init__(self):
        pass
        
    def inputs(self, inputv, nrn): #inputv[4] float,  nrn ineuron
        self.activation = 0
        for i in range(4):
            nrn[i].activation = nrn[i].act( inputv[i] )
            self.activation += nrn[i].activation
        
    def outvalue(self, j1):
        if self.activation >= j1:
            self.output = 1
        else:
            self.output = 0
        
        return self.output    
              

class network: 
    nrn:[] #ineurons
    onrn:object
    def __init__(self, a, b, c, d): #init with weight @ node 0-3 > 1 oneuron 
        self.nrn = [ineuron(a),ineuron(b),ineuron(c),ineuron(d)]
        self.onrn = oneuron()
        self.onrn.activation = 0
        self.onrn.output = 0
    
    def apply(self, vinputs):
        if len(vinputs) == 4:
            self.onrn.inputs( vinputs, self.nrn)
    
    def calc(self, threshold):
        return self.onrn.outvalue( threshold )
        
    def __repr__(self):
        for neuron in self.nrn:
            print(neuron)
        