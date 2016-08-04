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



	# Comprobamos que  Users sea un diccionario
	def test_tipoUsers(self):
		EsDict = isinstance(Controlador.Users, dict)
		self.assertTrue(EsDict)


	# Comprobamos que  Roles sea un diccionario
	def test_tipoRoles(self):
		EsDict = isinstance(Controlador.Roles, dict)
		self.assertTrue(EsDict)


	# Vemos el estado inical del Login
	def test_estadoLoginInicial(self):
		a = Control()
		self.assertFalse(a.Login)


	# Comprobar Login con un usuario inexistente
	def test_LoginUser_userFalse(self):
		Controlador.Login = False
		Controlador.Users = self.UsersTest
		self.assertRaises(UserNotExist,
							lambda:Controlador.LoginUser('pedro','x'))
		EsFalso = Controlador.Login
		self.assertFalse(EsFalso)


	# Comprobar Login con un usuario existente
	def test_LoginUser_userTrue(self):
		Controlador.Users = self.UsersTest
		Controlador.LoginUser('eduTest','e')
		EsTrue = Controlador.Login
		self.assertTrue(EsTrue)


	# Comprobar Login con Error en Password
	def test_LoginUser_ErrorPassword(self):
		Controlador.Login = False
		self.assertRaises(PasswordNotCorrect,
						lambda:Controlador.LoginUser('eduTest','xxx'))
		EsFalse = Controlador.Login
		self.assertFalse(EsFalse)


	# No se puede registrar si hay un login activo
	def test_LoginUser_DobleRegistro(self):
		Controlador.Login = False
		Controlador.Users = self.UsersTest
		self.assertRaises(DobleRegistro,
							Controlador.LoginUser('eduTest','e'))
		EsTrue = Controlador.Login
		self.assertTrue(EsTrue)


	# Impedir que se salgan del log con log False
	def test_LoginOut(self):
		self.assertRaises(LoginIsFalse, lambda:Controlador.LoginOut())
		Esfalse = Controlador.Login
		self.assertFalse(Esfalse)


	# Controlamos el sistema de credenciales, nadie registrado y ROLE_ADMIN.
	def test_CredencialRole_Admin_and_False(self):
		self.reg_users = 'ROLE_ADMIN'
		self.Login = False
		self.assertRaises(NotCredential, lambda:Controlador.Credencial())

	# Controlamos el sistema de credenciales, nadie registrado y ROLE_ADMIN.
	def test_Credencial_Role_and_True(self):
		self.reg_users = 'ROLE_ADMIN'
		self.Login = True
		self.Role = 'ROLE_ADMIN'
		self.assertTrue(lambda:Controlador.Credencial())


	# Controlamos el sistema de credenciales, Sin control.
	def test_Credencial_Not_Control(self):
		self.reg_users = 'NONE'
		self.assertTrue(lambda:Controlador.Credencial())

	# Control de CheckRoleUser con permisos y sin registrar.
	def test_CheckRoleUser_Role_Admin_Modo(self):
		self.reg_users = 'ROLE_ADMIN'
		self.Login = False
		self.assertRaises(NotCredential, lambda:Controlador.CheckRoleUser('pep'))

	# Control de CheckRoleUser con todo ok.
	def test_CheckRoleUser_Role_Admin_Modo_ok(self):
		self.reg_users = 'ROLE_ADMIN'
		self.Role = 'ROLE_ADMIN'
		Controlador.Users = self.UsersTest
		self.Login = True
		Res = Controlador.CheckRoleUser('pep')
		self.assertEqual(Res,'ROLE_USER')


	# Control de Editar nombre con nombre inexistente.
	def test_EditUserName_No_Exist(self):
		User = 'Juan'
		NewName = 'Antonio'
		self.reg_users = 'ROLE_ADMIN'
		self.Role = 'ROLE_ADMIN'
		self.Login = True
		Controlador.Users = self.UsersTest

		self.assertRaises(ValueNotReg, lambda:Controlador.EditUserName(User,NewName))

if __name__ == "__main__":
	unittest.main()
