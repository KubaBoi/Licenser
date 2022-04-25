#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from cheese.resourceManager import ResMan

"""
File generated by Cheese Framework

class that stores Cheese Application settings
"""

class Settings:

    settings = {}
    adminSettings = {}

    # load settings
    @staticmethod 
    def loadSettings():
        Settings.settings = Settings.loadJson()
        Settings.name = Settings.settings["name"]
        Settings.version = Settings.settings["version"]
        Settings.licenseCode = Settings.settings["licenseCode"]
        Settings.host = Settings.settings["host"]
        Settings.port = Settings.settings["port"]
        Settings.dbDriver = Settings.settings["dbDriver"]
        Settings.dbHost = Settings.settings["dbHost"]
        Settings.dbName = Settings.settings["dbName"]
        Settings.dbUser = Settings.settings["dbUser"]
        Settings.dbPassword = Settings.settings["dbPassword"]
        Settings.dbPort = Settings.settings["dbPort"]
        Settings.allowDebug = Settings.settings["allowDebug"]
        Settings.allowCommit = Settings.settings["allowCommit"]
        Settings.allowMultiThreading = Settings.settings["allowMultiThreading"]
        Settings.allowCORS = Settings.settings["allowCORS"]
        Settings.allowDB = Settings.settings["allowDB"]

        Settings.activeLicense = None

        with open(f"{ResMan.root()}/adminSettings.json", "r") as f:
            Settings.adminSettings = json.loads(f.read())

    @staticmethod
    def loadJson():
        with open(f"{ResMan.root()}/appSettings.json", "r") as f:
            ret = json.loads(f.read())
        return ret