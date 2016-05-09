# coding: utf-8
## Junção de todas as interfaces gráficas ~nova main~

from Tkinter import *
from Admin import Administrador
from SendEmail import SendEmail
from tabelaDados import TabelaDados
from telaLogin import Login
from telaAlteraUsuario import AlteraUsuario
from telaRemoverUsuario import RemoveUsuario
from telaCadastra import CadastraUsuario
from telaSendMail import Email

class RUFELIZ(object):
	def __init__(self, toplevel, login, senha): 
		#Login e senha que será utilizada durante todo o código
		self.login = login
		self.senha = senha
		
		self.toplevel = toplevel 
		self.toplevel.title('RUFELIZ - Com você para melhorar o atendimento')
		kanvas = Canvas(toplevel, width = 450, height = 100, bg = 'darkblue').grid()

		#TEXTO PRINCIPAL
		Label(self.toplevel, text = 'RUFELIZ', fg = 'darkblue', font = ('Arial', '22', 'bold'), height = 3).grid()
		#fonte padrão 
		self.font1 = ('Arial', '10', 'bold')	

	
		#DEFININDO BOTÕES 
		botao_cadastra = Button(self.toplevel, font = self.font1, text = 'Cadastrar Usuário', width = 30, bg='dodgerblue', command = self.cadastra).grid()
		botao_altera = Button(self.toplevel, font = self.font1, text = 'Altera Usuário', width = 30, bg='dodgerblue', command = self.altera).grid()
		botao_remove = Button(self.toplevel, font = self.font1, text = 'Remove Usuário', width = 30, bg='dodgerblue', command = self.remove).grid()	
		botao_email = Button(self.toplevel, font = self.font1, text = 'Envia Email', width = 30, bg='dodgerblue', command = self.email).grid()
		botao_visualiza = Button(self.toplevel, font = self.font1, text = 'Visualizar dados', width = 30, bg='dodgerblue', command = self.visualiza).grid()
	
	#Linkagens com as outras classes 
	
	def cadastra(self): 
		self.tela_cadastra = Toplevel(self.toplevel)
		CadastraUsuario(self.tela_cadastra, self.login, self.senha)
		self.tela_cadastra.grab_set()
		self.tela_cadastra.mainloop()
		self.tela_cadastra.grab_set()
		
	def altera(self): 
		self.tela_altera = Toplevel(self.toplevel)
		AlteraUsuario(self.tela_altera, self.login, self.senha)
		self.tela_cadastra.mainloop()
		self.tela_cadastra.grab_set()	
		
	def remove(self): 
		self.tela_remove = Toplevel(self.toplevel)
		RemoveUsuario(self.tela_remove, self.login, self.senha)
		self.tela_remove.mainloop()
		self.tela_cadastra.grab_set()
	
	def email(self): 
		self.tela_email = Tk()
		Email(self.tela_email, self.login, self.senha)
		self.tela_email.mainloop()
		self.tela_cadastra.grab_set()		
	
	def visualiza(self): 
		self.tela_visualiza = Tk()
		TabelaDados(self.tela_visualiza)
		self.tela_visualiza.mainloop()
		self.tela_visualiza.grab_set()	
	
	
#Inicia a tela de login, caso o login seja Verdadeiro ele fecha a tela (de login) e retorna verdadeiro. 		
top = Tk()
login = Login(top)
top.mainloop()
#caso o usuário não coloque o login-senha corretos, o programa quebra. Pois o objeto admin dentro da classe Login não é instanciado
#e a função retorna um erro. Por isso é usado o try/except 
try: 
	if login.retorna():
		instancia=Tk()
		login, senha = login.retorna_dados()
		RUFELIZ(instancia, login, senha)
		instancia.mainloop()

except: 
	exit()	
	
