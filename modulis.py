A = 60

def printA():
  print('As esu printA() xdd funkcijaxdd')
  
  
class Vehicle():
  def __init__(self, P , R):
    self.P = P
    self.R = R
class Car(Vehicle):
    def __init__(self, P, R,S ):
        super().__init__(P,R)
        self.S = S
      
    def GetSeats(self):  
        Txt = self.P + 'turi ' + str(self.S) + ' sedimu vietu'
        return Txt
 
class Bus(Vehicle):
    def __init__(self, P, R,S ):
          super().__init__(P,R)
          self.S = S
      
    def GetSeats(self):  
          Txt = self.P + 'turi ' + str(self.S) + ' sedimu vietu'
          return Txt
class Train(Vehicle):
    def __init__(self, P, R,S ):
        super().__init__(P,R)
        self.S = S
      
    def GetSeats(self):  
        Txt = self.P + 'turi ' + str(self.S) + ' sedimu vietu'
        return Txt
  