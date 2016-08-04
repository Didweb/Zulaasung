#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zulassung_test.py
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



class TestZulassung(unittest.TestCase):

	def setUp(self):
		fileYAML = open('./test/test_data_users.yaml')
		UsersTest = yaml.safe_load(fileYAML)
		fileYAML.close()
		self.UsersTest = UsersTest



	# Comprobamos la inicialización de las variables
	def test_Inicialitzation(self):
		Controler = User()

		self.assertFalse(Controler.Login)
		self.assertFalse(Controler.Role)
		self.assertFalse(Controler.pase)

	# test LoginOut
	def test_LoginOut(self):
		Controler = User()
		Controler.Login = True
		Controler.pase = True

		Controler.LoginOut()

		self.assertFalse(Controler.Login)
		self.assertFalse(Controler.pase)


	def test_CheckRoleUser_User_RA_reg_RA(self):
		"""
		Opciones:
		Usuario: ROLE_ADMIN ,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_ADMIN'
		Controler.reg_users = 'ROLE_ADMIN'
		self.UsersTest
		Res = Controler.CheckRoleUser('pep')
		self.assertEqual(Res,'ROLE_USER')


	def test_CheckRoleUser_User_RU_reg_RA(self):
		"""
		Opciones:
		Usuario: ROLE_USER ,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.User = 'pep'
		self.UsersTest

		self.assertRaises(NotCredential, lambda:Controler.CheckRoleUser('juan'))

	def test_CheckRoleUser_User_RU_reg_RA_elmismo(self):
		"""
		Opciones:
		Usuario: ROLE_USER ,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.User = 'pep'
		self.UsersTest

		Res = Controler.CheckRoleUser('pep')
		self.assertEqual(Res,'ROLE_USER')


	def test_CheckRoleUser_User_RA_reg_NONE(self):
		"""
		Opciones:
		Usuario: ROLE_ADMIN ,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_ADMIN'
		Controler.reg_users = 'NONE'
		Controler.User = 'edu'
		self.UsersTest

		Res = Controler.CheckRoleUser('pep')
		self.assertEqual(Res,'ROLE_USER')


	def test_CheckRoleUser_User_RU_reg_NONE(self):
		"""
		Opciones:
		Usuario: ROLE_USER ,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.User = 'edu'
		self.UsersTest

		Res = Controler.CheckRoleUser('pep')
		self.assertEqual(Res,'ROLE_USER')


	def test_CheckIdUser_User_RA_reg_RA(self):
		"""
		Opciones:
		Usuario: ROLE_ADMIN ,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_ADMIN'
		Controler.reg_users = 'ROLE_ADMIN'
		self.UsersTest
		Res = Controler.CheckIdUser('pep')
		self.assertEqual(Res,2)


	def test_CheckIdUser_User_RU_reg_RA(self):
		"""
		Opciones:
		Usuario: ROLE_USER ,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.User = 'pep'
		self.UsersTest

		self.assertRaises(NotCredential, lambda:Controler.CheckIdUser('juan'))


	def test_CheckIdUser_User_RU_reg_RA_elmismo(self):
		"""
		Opciones:
		Usuario: ROLE_USER ,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.User = 'pep'
		self.UsersTest

		Res = Controler.CheckIdUser('pep')
		self.assertEqual(Res,2)


	def test_CheckIdUser_User_RA_reg_NONE(self):
		"""
		Opciones:
		Usuario: ROLE_ADMIN ,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_ADMIN'
		Controler.reg_users = 'NONE'
		Controler.User = 'edu'
		self.UsersTest

		Res = Controler.CheckIdUser('pep')
		self.assertEqual(Res,2)



	def test_CheckIdUser_User_RU_reg_NONE(self):
		"""
		Opciones:
		Usuario: ROLE_USER ,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.User = 'edu'
		self.UsersTest

		Res = Controler.CheckIdUser('pep')
		self.assertEqual(Res,2)

if __name__ == "__main__":
	unittest.main()
