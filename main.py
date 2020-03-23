#!/usr/bin/env python3
import os
import json
import requests
import colorama
import matplotlib.pyplot as plt

def menu():
    print("""██████╗ ██╗   ██╗██╗  ██╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗ █████╗ 
██╔══██╗╚██╗ ██╔╝██║ ██╔╝██╔═══██╗██╔══██╗██╔═══██╗████╗  ██║██╔══██╗
██████╔╝ ╚████╔╝ █████╔╝ ██║   ██║██████╔╝██║   ██║██╔██╗ ██║███████║
██╔═══╝   ╚██╔╝  ██╔═██╗ ██║   ██║██╔══██╗██║   ██║██║╚██╗██║██╔══██║
██║        ██║   ██║  ██╗╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║
╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
---------------------------------------------------------------------
Select actions:
1. View summary of the world
2. View summary of specific country
3. Get historical data for a specific country

""")
    
    command = input("> ")
    if command == "1":
        r = requests.get("https://corona.lmao.ninja/all")
        data = json.loads(r.text)
        print("{:=^20}".format("World"))
        print("Cases: " + str(data["cases"]))
        print("Deaths: " + str(data["deaths"]))
        print("Recovered: " + str(data["recovered"]))
        print("="*20)
    elif command == "2":
        country = str(input("Enter country name: "))
        r = requests.get("https://corona.lmao.ninja/countries/{0}".format(country))
        data = json.loads(r.text)
        print("{:=^20}".format(country))
        print("Cases: " + str(data["cases"]))
        print("Deaths: " + str(data["deaths"]))
        print("Recovered: " + str(data["recovered"]))
        print("="*20)
    elif command == "3":
        country = str(input("Enter country name: "))
        r = requests.get("https://corona.lmao.ninja/historical/{0}".format(country))
        data = json.loads(r.text)
        x = []
        y = []
        for day in data["timeline"]["cases"]:
            x.append(day)
            y.append(data["timeline"]["cases"][day])        
        plt.style.use('dark_background')
        plt.fill_between( x, y, color="skyblue", alpha=0.2)
        plt.plot(x, y, color="Slateblue", alpha=0.6)
        plt.xlabel("Time")
        plt.ylabel("Cases")
        plt.title("Corona historical data for {0}".format(country))
        plt.show()
    elif command == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Unexpected command")
        exit()
    print("\n"*5)
while True:
    menu()