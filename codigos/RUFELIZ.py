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
	def __init__(self, toplevel): 
		self.toplevel = toplevel 
		self.toplevel.title('RUFELIZ - Com você para melhorar o atendimento')
		kanvas = Canvas(toplevel, width = 450, height = 100, bg = 'darkblue').grid()

		#TEXTO PRINCIPAL
		Label(self.toplevel, text = 'RUFELIZ', fg = 'darkblue', font = ('Arial', '22', 'bold'), height = 3).grid()
		#fonte padrão 
		self.font1 = ('Arial', '10', 'bold')	

	
		#DEFININDO BOTÕES 
		botao_cadastra = Button(self.toplevel, font = self.font1, text = 'Cadastrar Usuário', width = 30, bg='dodgerblue').grid()
		botao_altera = Button(self.toplevel, font = self.font1, text = 'Altera Usuário', width = 30, bg='dodgerblue').grid()
		botao_remove = Button(self.toplevel, font = self.font1, text = 'Remove Usuário', width = 30, bg='dodgerblue').grid()	
		botao_email = Button(self.toplevel, font = self.font1, text = 'Envia Email', width = 30, bg='dodgerblue').grid()
		botao_visualiza = Button(self.toplevel, font = self.font1, text = 'Visualizar dados', width = 30, bg='dodgerblue').grid()
	
	
#Inicia a tela de login, caso o login seja Verdadeiro ele fecha a tela (de login) e retorna verdadeiro. 		
top = Tk()
login = Login(top)
top.mainloop()
#caso o usuário não coloque o login-senha corretos, o programa quebra. Pois o objeto admin dentro da classe Login não é instanciado
#e a função retorna um erro. Por isso é usado o try/except 
try: 
	if login.retorna():
		instancia=Tk()
		print login.retorna_dados()
		RUFELIZ(instancia)
		instancia.mainloop()
		login, senha = login.retorna_dados()
except: 
	exit()	
	
