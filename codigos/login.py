# coding: utf-8 
# ENGINE DA VERIFICAÇÃO DO LOGIN 

import getpass

def verifica_login(login, senha): 
	
	'''verifica se o login e senha passado por parâmetro
	está salvo no banco de dados de usuarios permitidos'''

	
	import anydbm 
	db_login = anydbm.open('login_cadastrado.db', 'c')
	if login in db_login: 
		if db_login[login] == senha:
			print 'Logado com sucesso.'
			return True
		else:
			print 'Senha incorreta.'
			return False

	else:
		print 'Usuário não cadastrado.'


#exemplo de teste
while True:

	login = raw_input('LOGIN: ')
	senha = getpass.getpass('SENHA: ')

	if verifica_login(login, senha): 
		print '\n\n\nSeja bem vindo'
		break
	else: 
		print 'Tente Novamente'
	
	raw_input('Aperte Enter')
	print '\n\n\n\n\n\n\n\n\n\n\n'
