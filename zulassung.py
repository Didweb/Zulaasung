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


from control.exp_control import *

from control.config_control import (CheckConfig)

from data.server_data import (ServerData)

class Control:

	def __init__(self):

		# Inicializamos Login y Role
		self.Login = False
		self.Role = False

		# Traemos Sistema de control
		self.Con = CheckConfig()

		# Permiso de registro de usuarios Admin o Visitas
		self.reg_users = self.Con.Config['reg_users']

		# Traemos el servidor de datos
		self.Server = ServerData(self.Con)
		self.Users = self.Server.Users
		self.Roles = self.Server.Roles




class User(Control):

	def __init__(self):
		Control.__init__(self)


	def CheckRegister(self):
		pass


	def EditUserRole(self,user,NewRole):
		credencial = self.Credencial()


		CheckValueRole = self.Con.CheckValue(NewRole,self.Roles['Roles'])
		CheckValueUser = self.Con.CheckValue(user,self.Users['Users'])


		if CheckValueRole != False and CheckValueUser != False:
			self.Server.EditRol(user,NewRole)
		else:
			raise ValueNotReg()



	def EditUserName(self,user,NewName):
		credencial = self.Credencial()

		CheckValueUser = self.Con.CheckValue(user,self.Users['Users'])


		if CheckValueUser != False:
			self.Server.EditName(user,NewName)
		else:
			raise ValueNotReg()


	def DeleteUser(self,user):
		credencial = self.Credencial()

		CheckValueUser = self.Con.CheckValue(user,self.Users['Users'])

		if user == self.User:
			raise AutoDelete()

		if CheckValueUser != False:
			self.Server.DelUser(user)
		else:
			raise ValueNotReg()


	def CheckRoleUser(self,user):
		credencial = self.Credencial()
		return self.Users['Users'][user]['roles']


	def CheckIdUser(self,user):
		credencial = self.Credencial()
		return self.Users['Users'][user]['id']



	def LoginUser(self,name,password):
		# Sistema de Login de usuario
		Usuarios = self.Users['Users'].keys()

		if self.Login == True:
			raise DobleRegistro()

		if name in Usuarios:
			passwordData = self.Users['Users'][name]['password']
			if passwordData == password:
				self.Login = True
				self.User = name
				self.Role = self.Users['Users'][name]['roles']
				self.Id = self.Users['Users'][name]['id']
			else:
				raise PasswordNotCorrect()

		else:
			raise UserNotExist()


	def Credencial(self):
		""" Nos aseguramos de que tiene credenciales como Role_Admin
		y esta  logeado """
		if self.reg_users == 'ROLE_ADMIN':
			if self.Login == False:
				raise NotCredential()
			elif self.Role == 'ROLE_ADMIN':
				return True
		elif self.reg_users == 'NONE' and self.Role == 'ROLE_ADMIN':
			return True
		elif self.reg_users == 'NONE' and self.Role == False:
			raise NotCredential()


	def LoginOut(self):
		# Salir del login
		if self.Login == True:
			self.Login = False
		else:
			raise LoginIsFalse()


Controlador = User()

