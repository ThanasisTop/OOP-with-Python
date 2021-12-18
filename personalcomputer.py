from pctower import *
from pcscreen import *
class PersonalComputer(PCTower, PCScreen):
  def __init__(self, memorysize, frequency , screensize, drivercapacity):
      PCTower.__init__(self, memorysize, frequency) #Διατηρω τη κληρονομικοτητα απο την PCTower
      PCScreen.__init__(self, screensize) #Διατηρω τη κληρονομικοτητα απο την PCScreen
      self.DriverCapacity = drivercapacity #Δημιουργω αλλο ενα επιπλέον πεδιο 
  
  def message(self):
    PCTower.message(self)
    PCScreen.message(self)
    print('and a hard drive disk with',self.DriverCapacity, 'GB capacity')