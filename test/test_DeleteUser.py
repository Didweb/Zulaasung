#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_DeleteUser.py
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

import unittest


import sys

import os

import yaml



sys.path.append(os.getcwd())
from zulassung import (Control,Controlador,User,PasswordNotCorrect,
						DobleRegistro,UserNotExist,LoginIsFalse,
						NotCredential,ValueNotReg)



class TestDeleteUser(unittest.TestCase):

	def setUp(self):
		fileYAML = open('./test/test_data_users.yaml')
		UsersTest = yaml.safe_load(fileYAML)
		fileYAML.close()
		self.UsersTest = UsersTest






	def test_DeleteUser_sinRegistro_reg_RA(self):
		"""
		Opciones:
		Usuario: Sin registrar,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = False
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.iduser = 'AUTO'
		self.UsersTest

		self.assertRaises(NotCredential, lambda:Controler.DeleteUser('pep'))


	def test_DeleteUser_propio_U_RA_reg_RA(self):
		"""
		Opciones:
		Usuario: ROLE_ADMIN,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = 'ROLE_ADMIN'
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.iduser = 'AUTO'
		self.UsersTest
		Controler.User = 'edu'

		self.assertRaises(NotCredential, lambda:Controler.DeleteUser('edu'))


	def test_DeleteUser_otro_U_RA_reg_RA(self):
		"""
		Opciones:
		Usuario: ROLE_ADMIN,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = 'ROLE_ADMIN'
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.iduser = 'AUTO'
		self.UsersTest
		Controler.User = 'edu'

		self.assertTrue( lambda:Controler.DeleteUser('juan'))


	def test_DeleteUser_otro_U_RU_reg_RA(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.iduser = 'AUTO'
		self.UsersTest
		Controler.User = 'juan'

		self.assertRaises(NotCredential, lambda:Controler.DeleteUser('pep'))



	def test_DeleteUser_otro_U_RU_reg_NONE(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest
		Controler.User = 'juan'

		self.assertTrue( lambda:Controler.DeleteUser('pep'))


	def test_DeleteUser_propio_U_RU_reg_NONE(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest
		Controler.User = 'juan'

		self.assertTrue( lambda:Controler.DeleteUser('juan'))

if __name__ == "__main__":
	unittest.main()
