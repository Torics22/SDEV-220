# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:29:38 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""

today = open("today.txt", "r")

today_string = today.read()

print(today_string)

x = today_string.split()

print(x)