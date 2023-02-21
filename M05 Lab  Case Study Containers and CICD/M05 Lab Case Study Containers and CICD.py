# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 15:30:29 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""

import emoji

def user():
    x = input('Smile or Frown?: ')

    if (x == 'Smile' or 'smile'):
        print (emoji.emojize(":grinning_face:"))

    elif (x == 'Frown' or 'frown'):
        print (emoji.emojize(':frowning_face:'))

    elif (x != 'Smile' or 'Frown' or 'smile' or 'frown'):
        print ('invalid input')

if __name__ == "__main__":
    user()