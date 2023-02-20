# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 15:30:29 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""

import emoji

user = input('Smile or Frown?: ')

if (user == 'Smile' or 'smile'):
    print (emoji.emojize(':sweat_smile:'))

elif (user == 'Frown' or 'frown'):
    print (emoji.emojize(':frowning_face:'))

elif (user != 'Smile' or 'Frown' or 'smile' or 'frown'):
    print ('invalid input')

