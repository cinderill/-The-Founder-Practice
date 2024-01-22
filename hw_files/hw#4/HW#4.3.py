#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random

class Car:

  Name_Class = "Your horsewheels"

  def __init__ (self,
                model,
                mph,
                responseTime
                ):
    self.model = model
    self.mph = mph
    self.responseTime = responseTime
     
    
  def ready(self):
      print("Waiting for response from the car...")
      print("Ready to go!")
      return True
      
  def start(self, distance):
      print("Confirming signal...")
      print("GO!")
      Time = distance / self.mph + self.responseTime
      return Time
      
  
    
class Trakk:
    
    Name_Class = "Racing trakks"
    
    def __init__ (self,
                  name,
                  distance,
                  diff
                  ):
      self.name = name
      self.distance = distance
      self.diff = diff
    
  
def main():
    
    #Racers set
    racers = { 1 : Car("Flamethrower", 250, 3.1),
              2 : Car("StinkyFly", 180, 1.7),
              3 : Car("Born To Win", 120, 0.9)
              }
    
    trakks = { 1 : Trakk("DEAD END", 1000, [0,1,0,0,0]),
              2 : Trakk("Way Of PAIN", 2000, [0,1,0,0,0,0,0]),
              3 : Trakk("Stairway to Heaven", 3000, [0,1,0,0,0,0,0,0,0,0])
              }
    
    #Choose your racer
    while True:
        try:
            choice1 = int(input("Choose your wheelhorse (from 1 to 3): "))
            break
        except ValueError:
            print("Wanna Play?? Try Again!")
            
    #Choose your trakk
    while True:
        try:
            choice2 = int(input("Choose trakk (from 1 to 3): "))
            break
        except ValueError:
            print("Just make your choice...")
    
    player = racers[choice1]
    print("\n%s is on the Game!" % player.model)
    trakk = trakks[choice2]
    print("Trakk '%s' is ready to be dusted! About %d miles of suffer!\n" % (trakk.name, trakk.distance))
    status = False
    
    #Getting ready
    while not status:
        yn = input("Are you ready? (Y/N) - ")
        if yn in "yY":
            time.sleep(player.responseTime)
            status = player.ready()
    
    Time = player.start(trakk.distance)
    
    for phrase in ["*** READY ***", "**** SET ****", "**** GO! ****"]:
        print(phrase)
        time.sleep(1)
        
    for n in range(10):
        if random.choice(trakk.diff) == 1:
            print("It was a smashing hit! Is he okay?")
            Time += 0.5
            
    print("Your time is %.1f sec!" % float(Time))
    
    
    
    
main()
    