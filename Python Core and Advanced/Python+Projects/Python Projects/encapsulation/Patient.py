class Patient:

    def __init__(self,id,name,ssn):
        self.name = name
        self.id = id
        self.ssn = ssn
    
    def getID(self):
        return self.id 
    
    def setID(self,ID):
        self.id = ID

    def getName(self):
        return self.name 
    
    def setName(self,name):
        self.name = name

    def getSSN(self):
        return self.ssn 
    
    def setSSN(self,ssn):
        self.ssn = ssn    
    
P1 = Patient(123,"Ali",1234)
P1.setID(12)
P1.setName("Ali")
P1.setSSN(1234)
print(P1.getID())
print(P1.getName())
print(P1.getSSN())