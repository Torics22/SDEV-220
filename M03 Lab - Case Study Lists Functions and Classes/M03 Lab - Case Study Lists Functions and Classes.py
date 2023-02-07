# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:02:11 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""
#class Vehicle():
    #def _init__(self, Vtype):
       # self.Vtype = Vtype
#Starting the class and setting up App output       
class Automobile():
    def __init__(self, year, make, model, doors, roof, Vtype):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        self.Vtype = Vtype
    def __repr__(self):
        return f"Type = {self.Vtype} Year = {self.year} model = {self.model} doors = {self.doors} roof = {self.roof}"

#Getting Input From the user
Vtype = input('Please type input your type of Vehicle: ')

while Vtype != 'Car' and Vtype != 'car':
    print('Invalid Response')
    Vtype = input('Please type input your type of Vehicle: ')

year = input('Input the year of your Car: ')
make = input('Input the make of your Car: ')
model = input('Input the model of your Car: ')
doors = input('Input if you have a 2 door or 4 door: ')

while doors != '2 door' and doors != '4 door':
    print('Invalid Response')
    doors = input('Input if you have a 2 door or 4 door: ')
    
roof = input('Input if you have a Sun roof or not: (Y or N)')

while roof != 'Y' and roof != 'y' and roof != 'N' and roof != 'n':
    print('Invalid Response')
    roof = input('Input if you have a Sun roof or not: (Y or N)')

if roof == 'Y':
    roof = 'Sun roof'
if roof == 'N':
    roof = 'No Sun roof'

car = Automobile(year, make, model, doors, roof, Vtype = Vtype)
print(car)