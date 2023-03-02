# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:16:53 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""

import time
import random
import threading

def first():
    time.sleep(random.randint(0, 5))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("first " + current_time)
    
def second():
    time.sleep(random.randint(0, 5))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("second " + current_time)
    
def third():
    time.sleep(random.randint(0, 5))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("third " + current_time)

if __name__=="__main__":
    firstthread = threading.Thread(target=first)
    secondthread = threading.Thread(target=second)
    thirdthread = threading.Thread(target=third)
    
    firstthread.start()
    secondthread.start()
    thirdthread.start()
    
    firstthread.join()
    secondthread.join()
    thirdthread.join()

    print("-------------- IT IS FINISHED --------------")