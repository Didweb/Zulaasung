#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zulassung.py
#
#  Copyright 2016 Eduard Pinuaga Linares <info@did-web.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#



import yaml

from exp_control import *

class Control:

	def __init__(self):

		self.config = self.readConfig()
		print (self.config)
		print (self.data_users)
		print (self.data_roles)
		print (self.reg_users)
		self.Users = self.readUsers()
		self.Roles = self.readRoles()
		self.Login = False



	def readConfig(self):
		fileYAML = open('config/config.yaml')
		Config = yaml.safe_load(fileYAML)
		fileYAML.close()
		self.data_users = Config['data_users']
		self.data_roles = Config['data_roles']
		self.reg_users = Config['reg_users']
		return Config


	def readUsers(self):
		fileYAML = open('data/data_users.yaml')
		Users = yaml.safe_load(fileYAML)
		fileYAML.close()
		return Users


	def readRoles(self):
		fileYAML = open('data/data_roles.yaml')
		Roles = yaml.safe_load(fileYAML)
		fileYAML.close()
		return Roles




class User(Control):

	def __init__(self):
		Control.__init__(self)


	def CheckRegister(self):
		pass


	def LoginUser(self,name,password):
		# Sistema de Login de usuario
		Usuarios = self.Users['Users'].keys()

		if self.Login == True:
			raise DobleRegistro()

		if name in Usuarios:
			passwordData = self.Users['Users'][name]['password']
			if passwordData == password:
				self.Login = True
			else:
				raise PasswordNotCorrect()

		else:
			raise UserNotExist()


	def LoginOut(self):
		# Salir del login
		if self.Login == True:
			self.Login = False
		else:
			raise LoginIsFalse()









Controlador = User()

