# -*- coding: utf-8 -*-

#CLASSE DE ADMINSTRADOR	

import anydbm #importa o modulo de banco de dados (proprio do python)
import pickle 
import getpass
import string


class Administrador (object):

	def __init__(self,login_adm, senha_adm): #construtor
		self._login = login_adm
		self._senha = senha_adm 
		self.db_emails = anydbm.open('emails.db', 'c')	# DB PARA EMAIL CADASTRADOS
		self.db_login = anydbm.open('login_cadastrado.db', 'c')

	def verifica_login (self): #VERIFICA O LOGIN QND FOR PARA O ADMINISTRADOR ACESSAR - USADO NA TELA DE LOGIN - 
		if self._login in self.db_login and self.db_login[self._login] == self._senha: return True
		else: return False
			
	def verifica_matricula(self, matricula):
		if matricula in self.db_emails:
			return True
		return False		
		
	def login_senha(self): 
		return self._login, self._senha	

	def cadastra_usuario (self, matricula, email, alimentacao):
	#cadastra um novo comensal(aluno) na lista de emails e recebe se é carnívoro ou vegetariano, retorna 1 caso 	seja cadastrado ou 0 caso já esteja na lista '''

		if matricula not in self.db_emails:
			#transforma a lista [email, alimentacao] em string e armazena no db
			self.db_emails[matricula] = pickle.dumps([email, alimentacao])
			return True
		else:
			return False

	def altera_usuario(self, matricula, novo_email, nova_alimentacao):
	#altera email e alimentação do aluno 
		if matricula in self.db_emails:  #se alterar retorna 1, se a matricula n estiver cadastrada retorna 0
			#transforma a informação armazenada em forma de string no seu tipo original 
			#após substituição, o tipo de dado será transformado em string e armazenado
			self.db_emails[matricula] = pickle.dumps([novo_email, nova_alimentacao])
			return True 	
		else: return False
			

	def remove_usuario (self, matricula): 
		if matricula in self.db_emails: 
			del self.db_emails[matricula]
			return True
		return False

	def retorna_email(self):
		emails = []
		for key in self.db_emails:
			dados = pickle.loads(self.db_emails[key])
			emails.append(dados[0])
		return emails
		
	def retorna_valores_lista(self):
		matriculas, emails, alimentacao = [], [], [] 
		for matricula in self.db_emails: 
			email_alimentacao = (pickle.loads(self.db_emails[matricula]))
			matriculas.append(matricula)
			emails.append(email_alimentacao[0])
			alimentacao.append(email_alimentacao[1])
		return matriculas, emails, alimentacao			
				

	def estatisticas(self):
		#retorna a quantidade de cadastrados, de vegetarianos e carnívoros
		veg, carn = 0,0
		for usuarios in self.db_emails: 
			dado = pickle.loads(self.db_emails[usuarios])
			if 'veg' in dado[1].lower() : veg += 1
			if 'carn' in dado[1].lower(): carn += 1
		return veg, carn

	def __str__(self): 
		a = ''
		a += 'Matricula\tEmail\tAlimentação\n'	
		a += '______________________________________________________________'
		a += '\n\n'
		for matricula in self.db_emails: 
			email_alimentacao = (pickle.loads(self.db_emails[matricula]))
			a +=  '%s\t%s\t%s\n' %(matricula,email_alimentacao[0],email_alimentacao[1])
		return a
	
	
	
	
