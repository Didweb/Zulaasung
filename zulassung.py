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
		self.pase = False
		self.User = False


		# Traemos Sistema de control
		self.Con = CheckConfig()

		# Permiso de registro de usuarios Admin o Visitas
		self.reg_users = self.Con.Config['reg_users']

		# Traemos el servidor de datos
		self.DataServer = ServerData(self.Con)
		#self.Users = self.Server.Users
		#self.Roles = self.Server.Roles




class User(Control):

	def __init__(self):
		Control.__init__(self)


	def RegUser(self,user,password,role = 'ROLE_USER',iduser = 0):

		credencial = self.Credencial(user,'RegUser')
		self.DataServer.RegUser(user,password,role,iduser)



	def EditUserRole(self,user,NewRole):

		credencial = self.Credencial(user,'EditUserRole')
		self.DataServer.EditRol(user,NewRole)




	def EditUserName(self,user,NewName):

		credencial = self.Credencial(user,'EditUserName')
		self.User = self.DataServer.EditName(user,NewName)



	def DeleteUser(self,user):

		credencial = self.Credencial(user,'DeleteUser')
		self.DataServer.DelUser(user)



	def CheckRoleUser(self,user):

		credencial = self.Credencial(user,'CheckRoleUser')
		return self.DataServer.CheckRoleUser(user)


	def CheckIdUser(self,user):

		credencial = self.Credencial(user,'CheckIdUser')
		return self.DataServer.CheckIdUser(user)



	def LoginUser(self,name,password):

		if self.Login == True:
			raise DobleRegistro()

		credencial = self.Credencial(name,'LoginUser')
		self.pase = self.DataServer.Segurata(name,password)

		self.Login = self.pase['login']
		self.User = self.pase['user']
		self.Role = self.pase['role']
		self.Id = self.pase['id']


	def Credencial(self,user,place):



		if place == 'LoginUser':
			return True


		elif place == 'CheckIdUser' or place == 'CheckRoleUser' :

			if (self.reg_users == 'ROLE_ADMIN' \
								or self.reg_users == 'VISIT_REG') \
								and self.Role != 'ROLE_ADMIN':
				raise NotCredential()


		elif place == 'DeleteUser':

			if (self.reg_users == 'ROLE_ADMIN' \
								or self.reg_users == 'NONE' \
								or self.reg_users == 'VISIT_REG') \
								and self.Role == 'ROLE_ADMIN' \
								and self.User == user:
				raise NotCredential()

			if (self.reg_users == 'ROLE_ADMIN' \
								or self.reg_users == 'VISIT_REG') \
								and self.Role != 'ROLE_ADMIN' \
								and self.User != user:
				raise NotCredential()


		elif place == 'EditUserRole':

			if (self.reg_users == 'ROLE_ADMIN' \
								or self.reg_users == 'NONE' \
								or self.reg_users == 'VISIT_REG') \
								and self.Role == 'ROLE_ADMIN' \
								and self.User == user:
				raise NotCredential()

			if (self.reg_users == 'ROLE_ADMIN' \
								or self.reg_users == 'VISIT_REG') \
								and self.Role != 'ROLE_ADMIN':
				raise NotCredential()


		elif place == 'EditUserName':

			if (self.reg_users == 'ROLE_ADMIN' \
								or self.reg_users == 'VISIT_REG') \
								and self.Role != 'ROLE_ADMIN' \
								and self.User != user:
				raise NotCredential()


		elif place == 'RegUser':

			if self.reg_users == 'ROLE_ADMIN' \
								and self.Role != 'ROLE_ADMIN':
				raise NotCredential()

		return True







	def LoginOut(self):
		# Salir del login
		if self.Login == True:
			self.Login = False
			self.pase = False
			self.Role = False
		else:
			raise LoginIsFalse()


Controlador = User()

