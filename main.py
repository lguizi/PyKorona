#!/usr/bin/env python3 
import json
import requests
import colorama
import matplotlib.pyplot as plt

print(
"""
Select actions:
1. View summary of the world
2. View summary of specific country
3. Get historical data for a specific country
""")

command = input("> ")
if command == "1":
    r = requests.get("https://corona.lmao.ninja/all")
    data = json.loads(r.text)
    print("="*20)
    print("Cases: " + str(data["cases"]))
    print("Deaths: " + str(data["deaths"]))
    print("Recovered: " + str(data["recovered"]))
    print("="*20)
elif command == "2":
    pass
elif command == "3":
    pass
else:
    print("Unexpected command")
    exit()