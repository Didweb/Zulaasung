#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_RegUser.py
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
import random



sys.path.append(os.getcwd())
from zulassung import (Control,Controlador,User,PasswordNotCorrect,
						DobleRegistro,UserNotExist,LoginIsFalse,
						NotCredential,ValueNotReg,ErrorPasword)



class TestRegUser(unittest.TestCase):

	def setUp(self):
		fileYAML = open('./test/test_data_users.yaml')
		UsersTest = yaml.safe_load(fileYAML)
		fileYAML.close()
		self.UsersTest = UsersTest

		ran = random.randint(1, 100000)
		self.ran = str(ran)






	def test_RegUser_sinRegistrar_RA(self):
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

		self.assertRaises(NotCredential, lambda:Controler.RegUser('pedro'+self.ran,'x'))


	def test_RegUser_sinRegistrar_NONE(self):
		"""
		Opciones:
		Usuario: Sin registrar,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = False
		Controler.pase = False
		Controler.Role = False
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		self.assertTrue( lambda:Controler.RegUser('pedro'+self.ran,'x'))


	def test_RegUser_u_RA_re_RA(self):
		"""
		Opciones:
		Usuario: ROLE_ADMIN,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = False
		Controler.Role = 'ROLE_ADMIN'
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.iduser = 'AUTO'
		self.UsersTest

		self.assertTrue(lambda:Controler.RegUser('pedro'+self.ran,'x'))


	def test_RegUser_u_RA_re_NONE(self):
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
		self.UsersTest

		self.assertTrue(lambda:Controler.RegUser('pedro'+self.ran,'x'))


	def test_RegUser_u_RU_re_RA(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = ROLE_ADMIN
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'ROLE_ADMIN'
		Controler.iduser = 'AUTO'
		Controler.User = 'pep'
		self.UsersTest

		self.assertRaises(NotCredential, lambda:Controler.RegUser('pedro'+self.ran,'x'))



	def test_RegUser_u_RU_re_NONE(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		self.assertTrue(lambda:Controler.RegUser('pedro'+self.ran,'x'))



	def test_RegUser_Error_pw_min(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		Controler.pw_min_value = 2
		print (Controler.RegUser('pedro'+self.ran,'x'))
		self.assertRaises( ErrorPasword , lambda:Controler.RegUser('pedro'+self.ran,'x'))


	def test_RegUser_Correct_pw_min(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		Controler.pw_min_value = 2

		self.assertTrue( lambda:Controler.RegUser('pedro'+self.ran,'xx'))


	def test_RegUser_Correct_Simple(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		Controler.pw_min_value = 4
		Controler.pw_type = 'SIMPLE'

		self.assertTrue( lambda:Controler.RegUser('pedro'+self.ran,'xxxx'))


	def test_RegUser_Error_Alfa_num(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		Controler.pw_min_value = 4
		Controler.pw_type = 'ALFA_NUM'


		self.assertRaises(  ErrorPasword , lambda:Controler.RegUser('pedro'+self.ran,'xxxx'))


	def test_RegUser_Correct_Alfa_num(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		Controler.pw_min_value = 4
		Controler.pw_type = 'ALFA_NUM'

		self.assertTrue(lambda:Controler.Controler.RegUser('pedro'+self.ran,'xxx1'))


	def test_RegUser_Error_Alfa_num_Symbol(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		Controler.pw_min_value = 4
		Controler.pw_type = 'ALFA_NUM_SYMBOL'
		Controler.User = 'pedro'+self.ran
		self.assertFalse(lambda:Controler.CheckPassword('xxx1'))




	def test_RegUser_Correct_Alfa_num_Symbol(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		Controler.pw_min_value = 4
		Controler.pw_type = 'ALFA_NUM_SYMBOL'

		self.assertTrue( lambda:Controler.CheckPassword('x1#1'))




	def test_RegUser_Error_Alfa_num_Symbol_Caps(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		Controler.pw_min_value = 4
		Controler.pw_type = 'CAPS_ALFA_NUM_SYMBOL'

		self.assertRaises(ErrorPasword , lambda:Controler.Controler.RegUser('x1#1'))




	def test_RegUser_Correct_Alfa_num_Symbol_Caps(self):
		"""
		Opciones:
		Usuario: ROLE_USER,
		reg_users = NONE
		"""
		Controler = User()
		Controler.Login = True
		Controler.pase = True
		Controler.Role = 'ROLE_USER'
		Controler.reg_users = 'NONE'
		Controler.iduser = 'AUTO'
		self.UsersTest

		Controler.pw_min_value = 4
		Controler.pw_type = 'CAPS_ALFA_NUM_SYMBOL'

		self.assertTrue(lambda:Controler.RegUser('pedro'+self.ran,'x1D!'))

if __name__ == "__main__":
	unittest.main()
