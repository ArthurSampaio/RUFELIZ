# -*- coding: utf-8 -*-
#CODIGO DA MAIN DO PROJETO

import anydbm
import pickle 
import getpass
import sys
import smtplib
from email.mime.text import MIMEText
from Admin import Administrador
from SendEmail import SendEmail 


def clear():  #PARA LIMPAR TELA DO TERMINAL 
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)

def tela_principal ():
	print '1.\tCADASTRAR USUÁRIO' 
	print '2.\tATUALIZAR USUÁRIO'
	print '3.\tREMOVER USUÁRIO'
	print '4.\tIMPRIMIR EMAILS'
	print '5.\tENVIA EMAILS'
	print '6.\tESTATISTICAS'
	print '7.\tSAIR.'
	

def main ():

	while True: 
		#Realiza o login do adminstrador	
		print '\tBEM VINDO AO PROJETO DE P1'
		print '\tPARA COMEÇAR, POR FAVOR INSIRA SUAS CREDENCIAIS'
		login = raw_input('LOGIN: ')
		senha = getpass.getpass('SENHA: ')
		adm = Administrador(login, senha)
		if adm.verifica_login(): 
			#se o login for válido, irá instanciar um objeto de SendEmail
			envia = SendEmail(login,senha) 
			break
		else: 
			print 'Login e/ou senha inválida. Tente novamente.'
			clear()
	
	while True: 
		clear()
		tela_principal()
		opcao = int(raw_input('OPÇÃO: '))
				
		if opcao == 1: 
			print 'aaaa'
			while True: 
				print 'Para finalizar, digite "encerrar" no campo de matricula'
				matricula = raw_input('MATRICULA: ')
				if matricula == 'encerrar': break
				email = raw_input('EMAIL: ')
				alimentacao = raw_input('Vegetariana ou Carnivora: ')
				if adm.cadastra_usuario(matricula, email, alimentacao):
					print 'USUÁRIO CADASTRADO COM SUCESSO.'
				else: 
					print 'USUÁRIO JÁ CONSTA NOS NOSSOS REGISTROS.'

		elif opcao == 2: 
			print adm
			matricula = raw_input('MATRICULA: ')
			email = raw_input('Novo Email: ')
			alimentacao = raw_input('Nova Alimentação ')
			if adm.altera_usuario(matricula, email, alimentacao):
				print 'Alteração realizada com sucesso.'
			else: 
				print 'Matricula não cadastrada.'
			
		elif opcao == 3: 
			print adm
			print 'Insira a matricula do usuário que você quer remover do DB'
			matricula = raw_input('MATRICULA: ')
			if adm.remove_usuario(matricula): 
				print 'Usuário removido com sucesso'
			else: 
				print 'Falha.Matricula não cadastrada'
	
		elif opcao == 4:
			print adm
			raw_input('Tecle para continuar')
		

		elif opcao == 5:
			print 'Por favor aguarde enquanto a conexão é estabelecida'
			if envia.conexao(): print 'Conexão realizada com sucesso'
			emails = adm.retorna_email()
			mensagem = raw_input('Digite sua mensagem: ')
			subject = raw_input('Digite o assunto da msg: ')
			i = 0		# conta qnts emails foram enviados. 	
			for end in emails:
				i += 1
				envia.send_mail(end, subject, mensagem)
				print '%Email %i enviado' %i
				

			envia.close_connection()
		
		elif opcao == 6: 
			veg, carn = adm.estatisticas()
			print 'Há %i comensais cadastrados' %(veg+carn)
			print 'Vegetarianos: %i\t %.1f' %(veg, (float(veg/(veg+carn))*100))
			print 'Carnívoros: %i\t %1.f' %(carn, (float(carn/(veg+carn))*100))
			raw_input('Clique para continuar')

		elif opcao == 7: clear(); exit()


					 

