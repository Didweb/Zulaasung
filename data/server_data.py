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

class ServerData():

	def __init__(self,Config):

		self.Con = Config
		self.data_users = self.Con.Config['data_users']

		if self.data_users == 'YAML':
			self.Users = self.Con.readYaml('data','data_users.yaml') #self.YamlUser()
			self.Roles = self.Con.readYaml('data','data_roles.yaml')

		elif self.data_users == 'MYSQL':
			self.MysqlUser()
		elif self.data_users == 'PSQL':
			self.PsqlUser()


	def DelUser(self,user):

		if self.data_users == 'YAML':
			del self.Users['Users'][user]
			self.SaveUsers(self.Users)

		elif self.data_users == 'MYSQL':
			raise SinImplementar()

		elif self.data_users == 'PSQL':
			raise SinImplementar()


	def EditRol(self,user,NewRole):

		if self.data_users == 'YAML':
			self.Users['Users'][user]['roles'] = NewRole
			self.SaveUsers(self.Users)

		elif self.data_users == 'MYSQL':
			raise SinImplementar()

		elif self.data_users == 'PSQL':
			raise SinImplementar()


	def EditName(self,user,NewName):

		if self.data_users == 'YAML':
			ElUser = self.Users['Users'][user]
			Renmobrado = {'password':ElUser['password'],
							'roles':ElUser['roles'],
							'id':ElUser['id']}


			self.Users['Users'][NewName] = Renmobrado
			del self.Users['Users'][user]

			self.SaveUsers(self.Users)

		elif self.data_users == 'MYSQL':
			raise SinImplementar()

		elif self.data_users == 'PSQL':
			raise SinImplementar()


	def SaveUsers(self,data):

		#stream = open('./data/data_users.yaml', 'w')
		#Res = yaml.dump(data, stream)
		#stream.close()
		with open('./data/data_users.yaml', 'w') as outfile:
			outfile.write( yaml.dump(data, default_flow_style=False) )
		outfile.close()

	def MysqlUser(self):
		raise SinImplementar()


	def PsqlUser(self):
		raise SinImplementar()
