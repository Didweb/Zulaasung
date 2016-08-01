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

import sys

import yaml

class AuthException(Exception):

	def __init__(self):
		super(AuthException, self).__init__()

class UserNotExist(AuthException):
	def __str__(self):
		return "Usuario No existe"

class PasswordNotCorrect(AuthException):
	def __str__(self):
		return "Password incorrecto"


class DobleRegistro(AuthException):
	def __str__(self):
		return "Se ha intentado registrar 2 veces. [Debe hacer LogOut]"


class LoginIsFalse(AuthException):
	def __str__(self):
		return "No puede hacer LogOut sin Logearse antes."





class Control:

	def __init__(self):
		self.Users = self.readUsers()
		self.Roles = self.readRoles()
		self.Login = False


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

