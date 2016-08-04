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

from Crypto.Hash import MD5

from control.exp_control import (ErrorConfig,ErrorConfigNoActivo,ErrorPasword)

class CheckConfig:
	"""
	Se encarga de verificar que los datos de configuración son correctos
	Devuelve un diccionario con las opciones correctos o bien un error.
	"""
	def __init__(self):

		BrutConfig = self.readYaml('config','config.yaml')
		OpConfig = self.readYaml('control','options.yaml')



		Config = {}
		Config['data_users'] = self.CheckValue(BrutConfig['data_users'], OpConfig['data_users'])
		Config['data_roles'] = self.CheckValue(BrutConfig['data_roles'], OpConfig['data_roles'])
		Config['reg_users'] = self.CheckValue(BrutConfig['reg_users'], OpConfig['reg_users'])

		Config['iduser'] = self.CheckValue(BrutConfig['iduser'], OpConfig['iduser'])

		Config['pw_encrypt'] = self.CheckValue(BrutConfig['pw_encrypt'], OpConfig['pw_encrypt'])
		Config['pw_min'] = isinstance( BrutConfig['pw_min'], int )
		Config['pw_type'] = self.CheckValue(BrutConfig['pw_type'], OpConfig['pw_type'])

		for key,valores in Config.items():
			if valores == False:
				raise ErrorConfig()

		self.Config = Config


	def CheckPassword(self,password):

		PwType = self.Config['pw_type']

		PwMin = self.Config['pw_min']

		if len(password) < self.Config['pw_min']:
			raise ErrorPasword()

		if PwType == 'SIMPLE':
			return True

		elif PwType == 'ALFA_NUM':
			"""if re.match(r'[A-Za-z0-9]', password):
				print('OK')
			else:
				print('NO VALIDO')
			"""
			raise SinImplementar()
		elif PwType == 'ALFA_NUM_SYMBOL':
			raise SinImplementar()

		elif PwType == 'CAPS_ALFA_NUM_SYMBOL':
			raise SinImplementar()
		else:
			return False


	def EncryptPw(self,password):
		PwEncrypt = self.Config['pw_encrypt']
		if PwEncrypt == 'NONE':
			return password

		elif PwEncrypt == 'MD5':
			m = MD5.new()
			m.update(password)
			return m.digest()







	def CheckValue(self,valor,options):
		if valor in options:
			return valor
		else:
			return False


	def readYaml(self,NameFolder,NameFile):
		fileYAML = open('./'+NameFolder+'/'+NameFile)
		Res = yaml.safe_load(fileYAML)
		fileYAML.close()
		return Res
