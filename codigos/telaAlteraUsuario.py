# coding: utf-8 
#TELA DE ALTERAR USUARIO DO RU

from Admin import Administrador
from Tkinter import *

class AlteraUsuario(object):
	def __init__(self, toplevel, login, senha): 
		self.login = login
		self.senha = senha
		#instanciando um objeto Adminstrador
		self.adm = Administrador (self.login, self.senha)
		
		self.toplevel = toplevel
		self.toplevel.title('RUFELIZ - Alterando Cadastro')
		
		#fonte utilizada
		self.font1 = ('Arial', '10', 'bold')
		
		#IMAGEM PRINCIPAL
		self.photo = PhotoImage(file = '/home/petcomputacao/Documentos/sampaio/RUFELIZ/images/ru_altera.gif')	
		self.label = Label(self.toplevel, image = self.photo)
		self.label.image = self.photo
		self.label.grid(row = 0, column = 0, columnspan = 3)
		
		#PARA MATRICULA 
		frameM = Frame(self.toplevel, padx = 5, pady = 5).grid(row = 2)
		Label(self.toplevel, text = 'Matricula: ', font = self.font1, width = 14).grid(row = 2, column = 0)
		self.matricula = Entry(self.toplevel, width = 25,font = self.font1)
		self.matricula.focus_force()
		self.matricula.grid(row = 2, column = 1)
		#botão para verificar que a matricula ja consta no bd
		self.botao_verificar = Button(self.toplevel, font = self.font1, text = 'Verificar', command = self.verifica_matricula)
		self.botao_verificar.grid(row = 2, column = 2)
		
		
		#DEFININDO OS BOTÕES DE SALVAR E FECHAR
		self.botao_salvar = Button(self.toplevel, font = self.font1, text = 'Salvar', bg='dodgerblue', command = self.salvar)
		self.botao_salvar.grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 10)
		self.botao_fechar = Button(self.toplevel, font = self.font1, text = 'Fechar', bg = 'dodgerblue', command = self.fechar)
		self.botao_fechar.grid(row = 9, column = 1, columnspan = 2)

	def verifica_matricula(self): 
		if self.adm.verifica_matricula(self.matricula.get()) and len(self.matricula.get()) >= 1:
			Label(self.toplevel, text = 'Usuário cadastrado', font = ('Arial', '8'), bg = 'green', fg = 'white').grid(row = 3, column = 2)
			#PARA EMAIL 
			Label(self.toplevel, text = 'Email: ', font = self.font1, width = 14).grid(row = 5, column = 0)
			self.email = Entry(self.toplevel, width = 25, font = self.font1)
			self.email.grid(row = 5, column = 1)
			
			#PARA A CAIXA DROPDOWN DA ALIMENTAÇÃO
			Label(self.toplevel, text = 'Alimentação: ', font = self.font1, width = 14).grid(row = 7, column = 0)
			self.alimentacao = StringVar(self.toplevel)
			self.alimentacao.set(' ') #valor inicial do dropdown
			escolhas = ['Vegetariano', 'Carnivoro']
			opcao = OptionMenu(self.toplevel, self.alimentacao, *escolhas)#O * serve para que o dropdown divida os itens da lista respectiva lista apontada
			opcao.grid(row = 7, column = 1)
			#para utilizar a escolha dentro da opcao usar o metodo var.get()
			
		else: 
			Label(self.toplevel, text = 'Usuário não possui cadastro', font = ('Arial', '8'), bg = 'red', fg = 'white').grid(row = 3, column = 2)
		
	def salvar (self): 
		adm = Administrador(self.login, self.senha)
	#A confirmação que foi alterado ou não será mostrado numa janela auxiliar. (Segue sua implementação)	
		self.janela_aux = Toplevel(self.toplevel)
		if adm.altera_usuario(self.matricula.get(), self.email.get(), self.alimentacao.get()):
			Label(self.janela_aux, text = 'Alteração Concluída', width = 50, font = self.font1).grid()
		else: 	
			Label(self.janela_aux, text = 'Ocorreu um erro. Por favor, tente novamente', fg = 'red', width = 50, font = self.font1).grid()
		# botao da tela auxiliar
		botao = Button(self.janela_aux,text = 'Ok', command = self.fechar_dialogo).grid()
		#indica que a janela criada é filha da janela mãe "toplevel"0
		self.janela_aux.transient(self.toplevel)
		#Mantém os eventos restritos a janela filha enquanto ela estiver aberta
		self.janela_aux.grab_set()
		
	def fechar_dialogo(self):
		self.janela_aux.destroy()
		
	def fechar(self):
		self.toplevel.destroy()
		
instancia=Tk()

AlteraUsuario(instancia, 'uhu', 'ijki')
instancia.mainloop()
		
