
import os
import random
from datetime import datetime


def Clear():
    os.system("cls")

def randomIsbn():
    return random.randint(100000, 99999)

def currentTime():
    return datetime.now()

def menuOrExit():
    print("\n\n    1. Main Menu")
    print("    2. Exit")
    return int(input("\n    Choose an option : "))


