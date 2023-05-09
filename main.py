from pystyle import Colorate, Colors
import os
import time as t
import socket

os.system("cls")
os.system("title SHL Panel - By zMiless")

options = """
| SHL PANEL | ZMILESS
|###########################################|
| [ 1 ] DDoS Tool (WIFI, IP VIS)            |
| [ 2 ] IPhone Code Braak (USB , WIFI)      |
| [ 3 ] Android 13 Install (USB)            |
| [ 4 ] Find Website IP Adress (WIFI)       |
| [ 5 ] Down Website (DANG, WIFI, IP VIS)   |
| [ E ] Exit                                |
|###########################################|
"""

print(Colorate.Horizontal(Colors.blue_to_purple, options, 1))

while True:
    
    c = input(Colorate.Horizontal(Colors.cyan_to_blue, f"> ", 1))
    
    if c == "1":
        print("1")
    
    elif c == "2":
        print("2")
    
    elif c == "3":
        print("3")
    
    elif c == "4":
        print("4")
    
    elif c == "5":
        print("5")
    
    elif c == "6":
        print("6")
    
    elif c == "e":
        exit()
    
    else:
        print(Colorate.Color(Colors.red, "That Command Do Not Exist!", 1))



