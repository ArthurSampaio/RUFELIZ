# -*- coding: utf-8 -*-

import anydbm #importa o modulo de banco de dados (proprio do python)
import pickle #responsável por importar os metodos de pickling e unpickling(transforma
			  #tipos em strings, e vice versa, respectivamente)
import smtplib
import sys
import time
from email.mime.text import MIMEText




remetente = '"Seu nome" <seu@email.com>'
msg = '''Subject: Assunto do e-mail
From: %s
To: {email}
Aqui vai a sua mensagem...
Você pode substituir com os "campos" de cada entrada na lista de e-mails.
Por exemplo: {gentilico}
Atenciosamente,
    Diretoria da Associação Python Brasil''' % remetente

'''Escopo do código para enviar email, dessa vez eu utilizei como uma classe e não função '''

class SendEmail (object):
	def __init__ (self, login, senha):
		self._login = login	
		self._senha = senha

	def conexao(self):
		self.connect = smtplib.SMPT('smpt.gmail.com', 587)
		#apresentando ao servidor
		self.connect.ehlo()
		#indicando uma conexão segura com o servidor
		self.connect.starttls() 
		#apois o starttls sempre é necessário se re-apresentar ao servidor
		self.connect.ehlo()
		#Realizando login 
		self.connect.login(self._login, self._senha)  #realiza o login no email com os atributos da classe

	def send_email(self, _login, destinatario, msg):
		return self.connect.sendmail(self._login, destinario, msg)

	def fecha_conexao (self):
		self.connect.close()


if __name__ == __main__:
# TESTE DA CLASSE
	login = raw_input("LOGIN: ")
	senha = getpass.getpass('SENHA: ')
	envio_email = SendEmail(login, senha)
	envio_email.conexao()
	i = 0

	db_emails_cadastrados = anydbm.open('emails.db', 'c')	# DB PARA EMAIL CADASTRADOS	

	for matricula in db_emails_cadastrados:
		mensagem = msg
		i += 1

		sys.stdout.write('Enviando email %02d para <%s> ... '%(i, db_emails_cadastrados[matricula])
		
	
