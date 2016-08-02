#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config_control.py
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

import sys

import os


from control.exp_control import (ErrorConfig,ErrorConfigNoActivo)

class CheckConfig:
	"""
	Se encarga de verificar que los datos de configuración son correctos
	Devuelve un diccionario con las opciones correctos o bien un error.
	"""
	def __init__(self):

		BrutusConfig = self.readYaml('config','config.yaml')
		OptionsConfig = self.readYaml('control','options.yaml')

		Config = {}
		Config['data_users'] = self.CheckValue(BrutusConfig['data_users'],OptionsConfig['data_users'])
		Config['data_roles'] = self.CheckValue(BrutusConfig['data_roles'],OptionsConfig['data_roles'])
		Config['reg_users'] = self.CheckValue(BrutusConfig['reg_users'],OptionsConfig['reg_users'])

		for key,valores in Config.items():
			if valores == False:
				raise ErrorConfig()

		self.Config = Config



	def CheckValue(self,valor,options):
		if valor in options:
			return valor
		else:
			return False


	def readYaml(self,NameFolder,NameFile):
		fileYAML = open('./'+NameFolder+'/'+NameFile)
		Res= yaml.safe_load(fileYAML)
		fileYAML.close()
		return Res
