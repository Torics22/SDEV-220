# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:44:17 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""
import csv

with open("Final Project.csv", "r") as fromFile:
    reader = csv.reader(fromFile)
    for row in reader:
        if len(row) > 0:
            print(row)