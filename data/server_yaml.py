#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  server_yaml.py
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

class ServerYaml():

	def __init__(self,Con):

		self.Con = Con
		self.Users = self.Con.readYaml('data','data_users.yaml')
		self.Roles = self.Con.readYaml('data','data_roles.yaml')



	def Segurata(self,user,password):

		Usuarios = self.Users['Users'].keys()

		if user in Usuarios:
			passwordData = self.Users['Users'][user]['password']
			if passwordData == password:
				self.Login = True
				self.User = user
				self.Role = self.Users['Users'][user]['roles']
				self.Id = self.Users['Users'][user]['id']
				self.pase = {'login':self.Login,
							'user':self.User,
							'role':self.Role,
							'id':self.Id}
				return self.pase
			else:
				raise PasswordNotCorrect()

		else:
			raise UserNotExist()



	def DelUser(self,user):

		CheckValueUser = self.Con.CheckValue(user,self.Users['Users'])

		if user == self.User:
			raise AutoDelete()

		if CheckValueUser != False:
			del self.Users['Users'][user]
			self.SaveUsers(self.Users)

		else:
			raise ValueNotReg()




	def EditRol(self,user,NewRole):


		CheckValueRole = self.Con.CheckValue(NewRole,self.Roles['Roles'])
		CheckValueUser = self.Con.CheckValue(user,self.Users['Users'])


		if CheckValueRole != False and CheckValueUser != False:
			self.Users['Users'][user]['roles'] = NewRole
			self.SaveUsers(self.Users)
		else:
			raise ValueNotReg()



	def EditName(self,user,NewName):

		CheckValueUser = self.Con.CheckValue(user,self.Users['Users'])


		if CheckValueUser != False:
			ElUser = self.Users['Users'][user]
			Renmobrado = {'password':ElUser['password'],
							'roles':ElUser['roles'],
							'id':ElUser['id']}

			self.Users['Users'][NewName] = Renmobrado
			del self.Users['Users'][user]

			self.SaveUsers(self.Users)

		else:
			raise ValueNotReg()



	def RoleUser(self,user):
		return self.Users['Users'][user]['roles']


	def SaveUsers(self,data):

		with open('./data/data_users.yaml', 'w') as outfile:
			outfile.write( yaml.dump(data, default_flow_style=False) )
		outfile.close()
