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

from control.exp_control import (SinImplementar,PasswordNotCorrect,UserNotExist,DuplicateUser)
import yaml

class ServerYaml():

	def __init__(self,Con):

		self.Con = Con
		self.Users = self.Con.readYaml('data','data_users.yaml')
		self.Roles = self.Con.readYaml('data','data_roles.yaml')



	def RegisterUser(self,OptionIduser,user,password,role,iduser):

		Usuarios = self.Users['Users'].keys()
		ResPw = False

		if user in Usuarios:
			raise DuplicateUser()
		else:
			ResPw = self.Con.CheckPassword(password)

			if ResPw == True:
				PassFinaly = self.Con.EncryptPw(password)
			else:
				raise ErrorPasword()

			CheckValueRole = self.Con.CheckValue(role,self.Roles['Roles'])

			if CheckValueRole == False:
				raise ValueNotReg()
			else:
				RoleFinaly = role


			IduserFinaly = self.CheckIduser(iduser,OptionIduser)

			self.Users['Users'][user] = {'password':PassFinaly,
											'roles':RoleFinaly,
											'id':IduserFinaly}

			self.SaveUsers(self.Users)
			return True




	def CheckIduser(self,iduser,OptionIduser):

		OpIdUser =  OptionIduser

		if OpIdUser == 'IN_BBDD':
			raise ErrorConfig()

		elif OpIdUser == 'NONE':
			iduser = iduser
			return iduser

		elif OpIdUser == 'AUTO':
			l = []
			for nombre in self.Users['Users']:
				ids = self.Users['Users'][nombre]['id']
				l.append(ids)

			MayorMenor = sorted(l, reverse = True)
			iduser = MayorMenor[0]+1
			return iduser




	def Segurata(self,user,password):

		Usuarios = self.Users['Users'].keys()

		if user in Usuarios:

			if self.Con.Config['pw_encrypt'] == 'MD5':
				password = self.Con.EncryptPw(password)

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
			return True
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
			return NewName
		else:
			raise ValueNotReg()



	def RoleUser(self,user):


		if user in self.Users['Users']:
			return self.Users['Users'][user]['roles']
		else:
			raise UserNotExist()



	def IdUser(self,user):

		if user in self.Users['Users']:
			return self.Users['Users'][user]['id']
		else:
			raise UserNotExist()



	def SaveUsers(self,data):

		with open('./data/data_users.yaml', 'w') as outfile:
			outfile.write( yaml.dump(data, default_flow_style=False) )
		outfile.close()
