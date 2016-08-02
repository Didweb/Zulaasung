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


		self.Login = False

		Con = CheckConfig()
		Server = ServerData(Con.Config)
		self.Users = Server.Users




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

