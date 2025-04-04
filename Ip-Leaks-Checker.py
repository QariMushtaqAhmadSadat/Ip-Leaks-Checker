#!/usr/bin/env python3
import time
import requests

while True:
    try:
        ip = requests.get("https://api.ipify.org").text
        print(f"Public IP: {ip}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)  # Wait 5 seconds before the next check
