# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 15:30:29 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""

import emoji

user = input('Smile or Frown?: ')

if user == 'Smile' and 'smile':
    print(emoji.emojize(':smile:'))

if user == 'Frown' and 'frown':
    print(emoji.emojize(':frowning_face:'))

if user != 'Smile' or 'smile' or 'Frown' or 'frown':
    print('invalid input')