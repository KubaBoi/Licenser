#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.resourceManager import ResMan
from cheese.modules.cheeseController import CheeseController as cc
from cheese.ErrorCodes import Error

from python.repositories.licencesRepository import LicencesRepository

#@controller /licence
class Licence(cc):

    #@get /authLic
    @staticmethod
    def authLic(server, path, auth):
        args = cc.getArgs(path)

        if (not cc.validateJson(["code"], args)):
            Error.sendCustomError(server, "Wrong json structure", 400)
            return

        code = args["code"]
        licence = LicencesRepository.findBy("columnName-code", code)

        if (licence == None):
            Error.sendCustomError(server, "Unknown licence", 401)
            return
        elif (len(licence) <= 0):
            Error.sendCustomError(server, "Unknown licence", 401)
            return

        response = cc.createResponse({"LICENCE": licence.type}, 200)
        cc.sendResponse(server, response)
