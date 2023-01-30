# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 07:45:27 2023

@author: Kyle Stitt

sdev 245 Spring 2023

File Name:M02 Lab - Case Study: if...else and while

Description: Using if loops program will take input from user about student and output if the student is on the deans list, honor role, or not
"""
import sys
first_name='unknown'

last_name='unknown'

gpa=float(0.0)

while last_name != 'ZZZ':
    last_name=str(input('Input Students Last Name:'))
    if last_name == 'ZZZ' : break
    first_name=str(input('Input Students First Name: '))
    gpa=float(input('Input Students GPA: '))
    if gpa >= 3.5:
        print(first_name + ' has made the deans list.')
    if gpa >= 3.2 and gpa < 3.5:
        print(first_name + ' has made the honor role.')

if last_name =='ZZZ':
    print('Goodbye')
    sys.exit()