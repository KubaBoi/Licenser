#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

from cheese.appSettings import Settings
from cheese.modules.cheeseController import CheeseController
from cheese.admin.adminManager import AdminManager
from cheese.Logger import Logger
from cheese.ErrorCodes import Error
from python.authorization import Authorization

#REST CONTROLLERS
from python.controllers.HelloWorldController import HelloWorldController
from python.controllers.LicenceController import LicenceController


"""
File generated by Cheese Framework

server handler of Cheese Application
"""

class CheeseServerMulti(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

class CheeseServer(HTTPServer):
    """Handle requests in one thread."""

class CheeseHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path.startswith("/admin")):
            AdminManager.controller(self)
            return
        self.__log()
        if (self.path == "/alive"):
            CheeseController.sendResponse(self, CheeseController.createResponse({"RESPONSE": "Yes"}, 200))
            return
        try:
            path = CheeseController.getPath(self.path)
            auth = None

            if (path == "/"):
                CheeseController.serveFile(self, "index.html")
            elif (path.startswith("/hello")):
                if (path.startswith("/hello/world")):
                    HelloWorldController.helloWorld(self, self.path, auth)
                else:
                    if (self.path.endswith(".css")):
                        CheeseController.serveFile(self, self.path, "text/css")
                    else:
                        CheeseController.serveFile(self, self.path)
            elif (path.startswith("/licence")):
                if (path.startswith("/licence/authLic")):
                    LicenceController.authLic(self, self.path, auth)
                elif (path.startswith("/licence/generate")):
                    LicenceController.generate(self, self.path, auth)
                else:
                    if (self.path.endswith(".css")):
                        CheeseController.serveFile(self, self.path, "text/css")
                    else:
                        CheeseController.serveFile(self, self.path)
            else:
                if (self.path.endswith(".css")):
                    CheeseController.serveFile(self, self.path, "text/css")
                else:
                    CheeseController.serveFile(self, self.path)
        
        except Exception as e:
            Logger.fail("An error unknown occurred", e)
            Error.sendCustomError(self, "Internal server error :(", 500)

    def do_POST(self):
        self.__log()
        try:
            auth = None

            if (self.path.startswith("/hello")):
                pass
            elif (self.path.startswith("/licence")):
                pass
            else:
                Error.sendCustomError(self, "Endpoint not found :(", 404)

        except Exception as e:
            Logger.fail("An error unknown occurred", e)
            Error.sendCustomError(self, "Internal server error :(", 500)

    def end_headers(self):
        if (Settings.allowCORS):
            self.send_header("Access-Control-Allow-Origin", "*")
            BaseHTTPRequestHandler.end_headers(self)
        else:
            self.send_header("Content-type", "application/json")

    def log_message(self, format, *args):
        return

    def __log(self):
        Logger.okGreen(f"{self.client_address[0]} - {self.command} \"{self.path}\"")

