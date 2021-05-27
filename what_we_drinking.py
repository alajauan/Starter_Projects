#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/




print ("Welcome to What We Drinking")

import sys

age= int(input ("Please Enter Your Age: "))
 
for i in range (0, 1): 
   
         if age >= 21 :
            print("Enter 1 for Rum\n")
            print("Enter 2 for Vodka\n")         
            print("Enter 3 for Tequila\n")

         if age < 21:
            print ("We are sorry you do not meet the age requirement")
            sys.exit()
 

import random

rum =["Rum Punch", "Mojito", "Mai Tai", "Dark ’n Stormy", "Piña Colada", "Hurricane" ] 
rum_type = rum[random.randint(0, len(rum) -1)]

vodka =["Screwdriver", "Vodka Martini", "Cosmopolitan", "Vodka Tonic", "Moscow Mule", "Bloody Mary" ]
vodka_type = vodka[random.randint(0, len(vodka) -1)]

tequlia= ["Margarita", "Tequila Sunrise", "Bloody Maria", "El Diablo", "Sangrita", " Paloma"]
tequlia_type = tequlia[random.randint(0, len(tequlia) -1)]

choice = int(input("Enter your choice:"))
    
for i in range (0,1):
  
   if choice == 1 :
       print (rum_type)
   elif choice == 2 :
       print (vodka_type)
   elif choice == 3 :
        print ("Margarita")
   else:
        
        print ("Invalid Selection")
   



print ("Drink Up & Enjoy")




