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



class ServerYaml():

	def __init__(self):
		ServerData.__init__(self)




	def EditRol(self,user,NewRole):

		self.Users['Users'][user]['roles'] = NewRole
		self.SaveUsers(self.Users)


	"""
	def EditRol(self,user,NewRole):

		if self.data_users == 'YAML':
			self.Users['Users'][user]['roles'] = NewRole
			self.SaveUsers(self.Users)

		elif self.data_users == 'MYSQL':
			raise SinImplementar()

		elif self.data_users == 'PSQL':
			raise SinImplementar()
	"""

