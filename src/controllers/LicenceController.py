#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

from Cheese.resourceManager import ResMan
from Cheese.cheeseController import CheeseController as cc
from Cheese.ErrorCodes import Error
from Cheese.appSettings import Settings

from src.repositories.licencesRepository import LicencesRepository

#@controller /licence
class LicenceController(cc):

    #@get /authLic
    @staticmethod
    def authLic(server, path, auth):
        args = cc.getArgs(path)

        if (not cc.validateJson(["code"], args)):
            Error.sendCustomError(server, "Wrong json structure", 400)
            return

        code = args["code"]
        licence = LicencesRepository.findBy("code", code)

        if (licence == None):
            Error.sendCustomError(server, "Unknown licence", 401)
            return
        elif (len(licence) <= 0):
            Error.sendCustomError(server, "Unknown licence", 401)
            return

        response = cc.createResponse({"LICENCE": licence[0].type}, 200)
        cc.sendResponse(server, response)

    #@get /generate
    @staticmethod
    def generate(server, path, auth):
        args = cc.getArgs(path)

        if (not cc.validateJson(["type"], args)):
            Error.sendCustomError(server, "Wrong json structure", 400)
            return

        type = args["type"]

        newId = LicencesRepository.findNewId()
        license = Licences()
        license.id = newId
        license.code = LicenceController.generateLicense()
        license.type = type

        LicencesRepository.save(license)
        response = cc.createResponse({"LICENSE": license.toJson()}, 200)
        cc.sendResponse(server, response)

    #@get /get
    @staticmethod
    def get(server, path, auth):
        args = cc.getArgs(path)

        if (not cc.validateJson(["name", "pass"], args)):
            return cc.createResponse({"ERROR": "Wrong json structure"}, 400)

        if (args["name"] != Settings.getName and
            args["pass"] != Settings.getPass):
            return cc.createResponse({"ERROR": "Unauthorized"}, 401)
        
        licenses = LicencesRepository.findAll()

        jsonArray = cc.modulesToJsonArray(licenses)

        response = cc.createResponse({"LICENSES": jsonArray}, 200)
        cc.sendResponse(server, response)


    # METHODS

    @staticmethod
    def generateLicense():
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

