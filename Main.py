from pctower import *
from pcscreen import *
from personalcomputer import *
from workstation import *

class Main:
  answer = 'a'
  while answer != 'EXIT': 
      #Δημιουργω μενου για τον χρήστη
   print('Please make a selection using the shortcuts PT, PSC, PC, WS')
   menu = {'Pc Towers' : 'PT',
          'Pc Screens': 'PSC',
          'Personal Computers': 'PC',
          'Work Stations': 'WS'}
  
   print(menu)
   selection = input() 

   if selection == 'PT':
    memorysize = input('Please insert memory size in GB ') 
    frequency = input('Please insert frequency in GHz ')
    obj = PCTower(memorysize, frequency) #Δημιουργω αντικειμενο και αρχικοποιω τα πεδια του
    obj.message() #Καλω τη μεθοδο απο το αντικειμενο για να τυπωσει σχετικο μηνυμα

   elif selection == 'PSC':
    screensize = input('Please select screen size in inches ')
    obj = PCScreen(screensize)
    obj.message()


   elif selection == 'PC':
    print('Personal computer is composed by 1 Tower, 1 Screen & 1 Hard Disk Driver')
    memorysize = input('Please insert Towers memory size in GB ')
    frequency = input('Please insert frequency in GHz ')
    screensize = input('Please select screen size in inches ')
    drivercapacity = input('Please insert the capacity of Hard Disk Drive in GB ')
    obj = PersonalComputer(memorysize, frequency , screensize, drivercapacity)
    obj.message()
  
   elif selection == 'WS':
    print('The Work station is composed by a Personal Computer as well as an Operating System (Windows or Linux)')
    memorysize = input('Please insert Towers memory size in GB ')
    frequency = input('Please insert frequency in GHz ')
    screensize = input('Please select screen size in inches ')
    drivercapacity = input('Please insert the capacity of Hard Disk Drive in GB ')
    operatingsystem = str(input('Please select an operating system Windows or Linux '))
    obj = WorkStation(memorysize, frequency ,screensize, drivercapacity, operatingsystem)
    obj.message()
   
   else:
    print('You entered invalid shortcut, run again the program')#Ελεγχος συντομογραφιας
   print('To continue shoppping tap YES. Otherwise tap EXIT') #Ρωταω το χρηστη αν θελει να συνεχίσει την αγορα
   answer = str(input())