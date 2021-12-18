from personalcomputer import *
class WorkStation(PersonalComputer):
  def __init__(self, memorysize, frequency ,screensize, drivercapacity, operatingsystem):
    PersonalComputer.__init__(self, memorysize, frequency ,screensize, drivercapacity)#Διατηρω την κληρονομικοτητα απο PersonalComputer
    self.OperatingSystem = operatingsystem
  
  def message(self):
    PersonalComputer.message(self)
    print('and an operating system: ', self.OperatingSystem,'.')
    