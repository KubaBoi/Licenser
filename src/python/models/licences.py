#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.modules.cheeseModel import CheeseModel

#@model
class Licences(CheeseModel):
	def __init__(self, id=None, code=None, type=None):
		self.id=id
		self.code=code
		self.type=type

	def toJson(self):
		return {
			"ID": self.id,
			"CODE": self.code,
			"TYPE": self.type
		}

	def toModel(self, json):
		self.id = json["ID"]
		self.code = json["CODE"]
		self.type = json["TYPE"]
