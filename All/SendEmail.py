# -*- coding: utf-8 -*-
# CLASSE PARA ENVIAR EMAILS A DIVERSOS DESTINATÁRIOS

import smtplib
import anydbm
import sys
import getpass
from email.mime.text import MIMEText

class SendEmail (object):
	def __init__(self, login, senha):
		self.login = login
		self.senha = senha

	def conexao(self):
		#cria um cliente smtp que conectara com smpt.gmail.com na porta 587
		self.gm = smtplib.SMTP('smtp.gmail.com', 587)
		#nos apresentando ao servidor 
		self.gm.ehlo()
		self.gm.starttls() #indicamos que será usado uma conexão segura
		self.gm.ehlo()   #re-apresentação
		self.gm.login(self.login, self.senha)  #realiza o login com a conta que enviará os emaill
		return True

	def send_mail (self, destinatario, subject, mensagem): 
		mail = MIMEText(mensagem)
		mail['To'] = destinatario
		mail['Subject'] =  subject
		if self.gm.sendmail(self.login, destinatario, mail.as_string()):
			return True

	def frescura (self): return True
	def close_connection(self):
		self.gm.close()
	

if __name__ == '__main__':
	login = raw_input('EMAIL: ')
	senha = getpass.getpass('SENHA: ')
	envio = SendEmail(login, senha)
	if envio.conexao(): 
		print "Conexão Realizada com Sucesso."
	destinatario = raw_input('destinatario: ')
	subject = raw_input('Subject: ')
	mensagem = raw_input('Mensagem: ')
	if envio.send_mail(destinatario, subject, mensagem):
		print 'mensagem enviada com sucesso. '
	envio.close_connection()


















