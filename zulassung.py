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

		credencial = self.Credencial(user)
		self.DataServer.RegUser(user,password,role,iduser)



	def EditUserRole(self,user,NewRole):

		if self.Role == 'ROLE_ADMIN' and self.User != user :
			self.DataServer.EditRol(user,NewRole)
		else:
			raise NotCredential()



	def EditUserName(self,user,NewName):

		credencial = self.Credencial(user)
		self.DataServer.EditName(user,NewName)



	def DeleteUser(self,user):

		credencial = self.Credencial(user)
		self.DataServer.DelUser(user)



	def CheckRoleUser(self,user):

		credencial = self.Credencial(user)
		return self.DataServer.CheckRoleUser(user)


	def CheckIdUser(self,user):

		credencial = self.Credencial(user)
		return self.DataServer.CheckIdUser(user)



	def LoginUser(self,name,password):

		if self.Login == True:
			raise DobleRegistro()

		self.pase = self.DataServer.Segurata(name,password)

		self.Login = self.pase['login']
		self.User = self.pase['user']
		self.Role = self.pase['role']
		self.Id = self.pase['id']


	def Credencial(self,user):

		if self.reg_users == 'ROLE_ADMIN':
			if self.Login == False:
				raise NotCredential()

			elif self.Role == 'ROLE_ADMIN':
				return True

			elif self.Role != 'ROLE_ADMIN' and self.User == user:
				return True

			else:
				raise NotCredential()

		elif self.reg_users == 'NONE' and self.User == user:
			return True

		elif self.reg_users == 'NONE' and self.Role == False:
			raise NotCredential()


	def LoginOut(self):
		# Salir del login
		if self.Login == True:
			self.Login = False
			self.pase = False
		else:
			raise LoginIsFalse()


Controlador = User()

