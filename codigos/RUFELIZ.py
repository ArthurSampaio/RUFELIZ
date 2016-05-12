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



#_____________________________MAIN______________________________________

class RUFELIZ(object):
	def __init__(self, toplevel, login, senha): 
		#Login e senha que será utilizada durante todo o código
		self.login = login
		self.senha = senha
		
		self.toplevel = toplevel 
		self.toplevel.title('RUFELIZ - Com você para melhorar o atendimento')
		self.toplevel
						
		
		#IMAGEM PRINCIPAL
		self.photo = PhotoImage(file = '/home/petcomputacao/Documentos/sampaio/RUFELIZ/images/ru_marca.gif')	
		self.label = Label(image = self.photo)
		self.label.image = self.photo
		self.label.grid()
		
		 # add a menu: ..................................................
		menubar = Menu(toplevel)
		filemenu = Menu(menubar,tearoff=0)
		filemenu.add_command(label="Sobre", command = self.sobre)
		filemenu.add_command(label="Sair", command = self.sair)
		menubar.add_cascade(label="Mais",menu=filemenu)
		toplevel.config(menu=menubar)
		
		
		#TEXTO PRINCIPAL
		Label(self.toplevel, text = '', fg = 'darkblue', font = ('Arial', '22', 'bold'), height = 3)
		#fonte padrão 
		self.font1 = ('Arial', '10', 'bold')	
	
		#DEFININDO BOTÕES 
		botao_cadastra = Button(self.toplevel, font = self.font1, text = 'Cadastrar Usuário', width = 50, bg='dodgerblue', fg = 'white', command = self.cadastra).grid(columnspan = 3)
		botao_altera = Button(self.toplevel, font = self.font1, text = 'Altera Usuário', width = 50, bg='dodgerblue',fg = 'white',  command = self.altera).grid(columnspan = 3)
		botao_remove = Button(self.toplevel, font = self.font1, text = 'Remove Usuário', width = 50, bg='dodgerblue', fg = 'white', command = self.remove).grid(columnspan = 3)	
		botao_email = Button(self.toplevel, font = self.font1, text = 'Envia Email', width = 50, bg='dodgerblue', fg = 'white', command = self.email).grid(columnspan = 3)
		botao_visualiza = Button(self.toplevel, font = self.font1, text = 'Visualizar dados', width = 50, bg='dodgerblue', fg = 'white', command = self.visualiza).grid(columnspan = 3)
	
		
	
	
	#Linkagens com as outras classes 
	def cadastra(self): 
		self.tela_cadastra = Toplevel(self.toplevel)
		CadastraUsuario(self.tela_cadastra, self.login, self.senha)
		self.tela_cadastra.grab_set()
		self.tela_cadastra.mainloop()
		
		
	def altera(self): 
		self.tela_altera = Toplevel(self.toplevel)
		AlteraUsuario(self.tela_altera, self.login, self.senha)
		self.tela_altera.grab_set()
		self.tela_altera.mainloop()	
	
	def remove(self): 
		self.tela_remove = Toplevel(self.toplevel)
		RemoveUsuario(self.tela_remove, self.login, self.senha)
		self.tela_remove.grab_set()
		self.tela_remove.mainloop()
	
	def email(self): 
		self.tela_email = Toplevel(self.toplevel)
		Email(self.tela_email, self.login, self.senha)
		self.tela_email.grab_set()
		self.tela_email.mainloop()
			
	
	def visualiza(self): 
		self.tela_visualiza = Toplevel(self.toplevel)
		TabelaDados(self.tela_visualiza, self.login, self.senha)
		self.tela_visualiza.grab_set()
		self.tela_visualiza.mainloop()	
		
	def sair(self):
		self.toplevel.destroy()
		
	def sobre(self): 
		#janela sobre o projeto
		self.janela_aux = Toplevel()
		Label(self.janela_aux, text = 'Sobre o RUFELIZ', width = 50, font = self.font1).grid()
		sobre = StringVar()
		sobre = '''RUFELIZ, é um sistema que tem por objetivo estreitar os laços entre o Restaurante Universitário da UFCG e o corpo discente que é usuário de seus serviços. 
		
Tal estreitamento de laços se dará pelo RUFELIZ, que ficará responsável em criar um banco de dados com os dados de todos os comensais (matricula, email e alimentação), em que os gerentes do RU irão avisar via email (e posteriormente sms) informações relevantes, como cardápio do dia e funcionamento do RU. 

O Código está sendo escrito em linguagem de programação python com orientação a objetos. 

RUFELIZ, é um projeto de Arthur Sampaio para a disciplina de P1 do curso de Ciência da Computação da UFCG, Brazil. '''
		self.text = Text(self.janela_aux)
		self.text.insert(END, sobre)
		self.text.grid()	

		
		botao = Button(self.janela_aux,text = 'Ok', command = self.fechar_dialogo).grid()
		#indica que a janela criada é filha da janela mãe "toplevel"0
		self.janela_aux.transient(self.toplevel)
		#Mantém os eventos restritos a janela filha enquanto ela estiver aberta
		self.janela_aux.grab_set()		
	
	def fechar_dialogo(self):
		self.janela_aux.destroy()
	
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
	
