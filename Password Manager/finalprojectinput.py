# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:41:29 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""
import datetime as dt
import csv
import sys
from cryptography.fernet import Fernet

class user_info():
    def __init__(self, website, username, password, date):
        self.website = website
        self.username = username
        self.password = password
        self.date = date

#Function used to get input from user#
def ori_input():
    answer = input('Would you like to input information? (Yes or NO)')
    while answer.lower() == "yes":
        website = input('Enter the name of the website: ')
        username = input('Enter the username: ')
        password = input('Enter the password: ')
        
        # with open("key_file.ppk", "r") as fromFile:
        #     key = fromFile.read()

        # fernet = Fernet(key)
        # encPassword = fernet.encrypt(bytes(password, "utf-8"))
        # password = encPassword
        date = dt.date.today()
        with open("Final Project.csv", "a") as toFile:
            writer = csv.writer(toFile)
            writer.writerow([website, username, password, date])
        answer = input('Is there more you wish to enter? (Yes or NO)')
        if answer.lower() == 'no':
            print('goodbye')
            sys.exit()

#def ori_output():

if __name__=="__main__":
    ori_input()
    #if example == 'Y':
        #key()