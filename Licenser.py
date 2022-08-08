#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time

from Cheese.cheese import CheeseBurger
from Cheese.appSettings import Settings

"""
File generated by Cheese Framework

main file of Cheese Application
"""

if __name__ == "__main__":
    CheeseBurger.init()

    i = 0
    while True:
        try:
            req = {
                "name": Settings.name,
                "port": Settings.port,
                "icon": "/icon.png",
                "color": "FF0000"
            }
            print("Sending request to FrogieHub")
            requests.post(f"http://localhost/services/doYouKnowMe", json=req)
            break
        except:
            i += 1
            if (i >= 10): break
            print("Unable to reach FrogieHub")
            time.sleep(1)

    CheeseBurger.serveForever()