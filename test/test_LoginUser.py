#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_LoginUser.py
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



class TestLoginUser(unittest.TestCase):

	def setUp(self):
		fileYAML = open('./test/test_data_users.yaml')
		UsersTest = yaml.safe_load(fileYAML)
		fileYAML.close()
		self.UsersTest = UsersTest






	def test_LoginUser_yaEstaReg(self):
		"""
		Opciones:
		Usuario: Registrado,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = False
		Controler.Role = False
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.iduser = 'AUTO'


		self.assertRaises(DobleRegistro, lambda:Controler.LoginUser('pep','p'))




	def test_LoginUser_sin_reg_RA(self):
		"""
		Opciones:
		Usuario: sin registrar,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = False
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.iduser = 'AUTO'

		self.assertRaises(NotCredential, lambda:Controler.LoginUser('pep','p'))



	def test_LoginUser_sin_reg_NONE(self):
		"""
		Opciones:
		Usuario: sin registrar,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = False
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'

		self.assertTrue(lambda:Controler.LoginUser('pep','p'))




	def test_LoginUser_RU_reg_RA(self):
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

		self.assertRaises(NotCredential, lambda:Controler.LoginUser('pep','p'))




	def test_LoginUser_RA_reg_RA(self):
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

		self.assertTrue( lambda:Controler.LoginUser('edu','e'))



	def test_LoginUser_RA_reg_NONE(self):
		"""
		Opciones:
		Usuario: ROLE_ADMIN,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = 'ROLE_ADMIN'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'

		self.assertTrue( lambda:Controler.LoginUser('edu','e'))




	def test_LoginUser_RU_reg_NONE(self):
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

		self.assertTrue( lambda:Controler.LoginUser('pep','p'))




	def test_LoginUser_Error_password(self):
		"""
		Opciones:
		Usuario: sin registro,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = False
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		Controler.Users = self.UsersTest

		self.assertRaises(PasswordNotCorrect, lambda:Controler.LoginUser('pep','xxx'))




	def test_LoginUser_Error_DobleRegistro(self):
		"""
		Opciones:
		Usuario: ROLE_ADMIN,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = False
		Controler.Role = 'ROLE_ADMIN'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		Controler.Users = self.UsersTest
		Controler.User= 'edu'

		self.assertRaises(DobleRegistro, lambda:Controler.LoginUser('edu','e'))




	def test_LoginUser_Error_NoExisteUser(self):
		"""
		Opciones:
		Usuario: sin registrar,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = False
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		Controler.Users = self.UsersTest


		self.assertRaises(UserNotExist, lambda:Controler.LoginUser('mandela','m'))



	def test_LoginUser_ok_con_md5(self):
		"""
		Opciones:
		El password encriptado de prueba es : x
		Usuario: sin registrar,
		reg_users = NONE
		"""
		fileYAML = open('./test/test_data_users_md5.yaml')
		UsersTest = yaml.safe_load(fileYAML)
		fileYAML.close()

		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = False
		Controler.reg_users = 'NONE'
		Controler.pw_encrypt = 'MD5'
		Controler.iduser = 'AUTO'
		Controler.Users = UsersTest


		self.assertTrue(lambda:Controler.LoginUser('anton','x'))



	def test_LoginUser_Error_con_md5(self):
		"""
		Opciones:
		El password encriptado de prueba es : x
		Usuario: sin registrar,
		reg_users = NONE
		"""
		fileYAML = open('./test/test_data_users_md5.yaml')
		UsersTest = yaml.safe_load(fileYAML)
		fileYAML.close()

		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = False
		Controler.reg_users = 'NONE'
		Controler.pw_encrypt = 'MD5'
		Controler.iduser = 'AUTO'
		Controler.Users = UsersTest


		self.assertRaises(PasswordNotCorrect,lambda:Controler.LoginUser('anton','xxxx'))

if __name__ == "__main__":
	unittest.main()
