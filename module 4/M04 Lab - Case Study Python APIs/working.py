# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:24:03 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""

import fastapi
from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None




@app.get("/")

def home():
    return {"Data": "Testing"}

@app.get("/about")

def about():
    return {"Data": "About"}

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to view.")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
        return {"Data":"Not Found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error":"Item ID already exists."}
    inventory[item_id] = item
    return inventory[item_id]
    