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
		#print ('Es Config',Config)

		data_users = Config['data_users']
		if data_users == 'YAML':
			self.Users = self.YamlUser()
		elif data_users == 'MYSQL':
			self.MysqlUser()
		elif data_users == 'PSQL':
			self.PsqlUser()


	def YamlUser(self):
		fileYAML = open('./data/data_users.yaml')
		Res= yaml.safe_load(fileYAML)
		fileYAML.close()
		return Res


	def MysqlUser(self):
		raise SinImplementar()


	def PsqlUser(self):
		raise SinImplementar()
