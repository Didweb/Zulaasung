#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ServerData.py
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

from control.exp_control import (SinImplementar)

from data.server_yaml import(ServerYaml)

class ServerData():

	def __init__(self,Config):

		self.Con = Config
		self.data_users = self.Con.Config['data_users']

		if self.data_users == 'YAML':
			self.Datas = ServerYaml(self.Con)


		elif self.data_users == 'MYSQL':
			self.MysqlUser()

		elif self.data_users == 'PSQL':
			self.PsqlUser()



	def RegUser(self,user,password,role,iduser):
		OptIduser = self.Con.Config['iduser']
		return self.Datas.RegisterUser(OptIduser,user,password,role,iduser)



	def Segurata(self,user,password):
		return self.Datas.Segurata(user,password)


	def DelUser(self,user):
		return self.Datas.DelUser(user)


	def EditRol(self,user,NewRole):
		return self.Datas.EditRol(user,NewRole)


	def EditName(self,user,NewName):
		return self.Datas.EditName(user,NewName)


	def SaveUsers(self,data):
		return self.Datas.SaveUsers(data)

	def CheckRoleUser(self,user):
		return self.Datas.RoleUser(user)

	def CheckIdUser(self,user):
		return self.Datas.IdUser(user)
