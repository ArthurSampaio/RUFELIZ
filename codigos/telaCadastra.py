# coding: utf-8 
#TELA DE CADASTRAR NOVO COMENSAL

from Admin import Administrador
from SendEmail import SendEmail
from Tkinter import *

class CadastraUsuario(object):
	def __init__(self, toplevel): 
		self.login = 'rufelizp1@gmail.com'
		self.senha = 'projetoru'
		#INICIALIZANDO KANVAS E FRAMES 
		kanvas = Canvas(toplevel, width = 300, height = 100, bg = 'darkblue').grid(row = 0, columnspan = 3)	
		self.toplevel = toplevel
		self.toplevel.title('RUFELIZ - Cadastro de novo comensal')
		
		#TEXTO PRINCIPAL
		Label(self.toplevel, text = 'CADASTRO DE USUÁRIO', fg = 'darkblue', font = ('Arial', '22', 'bold'), height = 3).grid(row = 1, columnspan = 3)
		font1 = ('Arial', '10', 'bold')
		
		#PARA MATRICULA 
		Label(self.toplevel, text = 'Matricula: ', font = font1, width = 14).grid(row = 2, column = 1)
		self.matricula = Entry(self.toplevel, width = 25, font = font1).grid(row = 2, column = 2)
		
		#PARA EMAIL 
		Label(self.toplevel, text = 'Email: ', font = font1, width = 14).grid(row = 3, column = 1)
		self.email = Entry(self.toplevel, width = 25, font = font1).grid(row = 3, column = 2)
		
		#PARA A CAIXA DROPDOWN DA ALIMENTAÇÃO
		Label(self.toplevel, text = 'Alimentação: ', font = font1, width = 14).grid(row = 4, column = 1)
		self.alimentacao = StringVar(toplevel)
		self.alimentacao.set(' ') #valor inicial do dropdown
		escolhas = ['Vegetariano', 'Carnívoro']
		opcao = OptionMenu(self.toplevel, self.alimentacao, *escolhas)#O * serve para que o dropdown divida os itens da lista respectiva lista apontada
		opcao.grid(row = 4, column = 2)
		#para utilizar a escolha dentro da opcao usar o metodo var.get()
		
		#DEFININDO OS BOTÕES DE SALVAR E FECHAR
		self.botao_salvar = Button(self.toplevel, font = font1, text = 'Salvar', bg='dodgerblue', command= self.salvar)
		self.botao_salvar.grid(row = 5, column = 1, padx = 10, pady = 10)
		self.botao_fechar = Button(self.toplevel, font = font1, text = 'Fechar', bg = 'dodgerblue', command = self.fechar)
		self.botao_fechar.grid(row = 5, column = 2)
	
	def salvar(self):
		adm = Administrador(self.login, self.senha)
		matricula = self.matricula.get("1.0", END)
		alimentacao = self.alimentacao.get("1.0", END)
		email = self.email.get("1.0", END)
		
		
		if adm.cadastra_usuario(matricula, email, alimentacao):
			#Implementando uma caixa de diálogo para aparecer quando ocorrer a ação de salvar (tanto para True qnt para False)
			self.janela_aux = Toplevel(toplevel)
			Label(self.janela_aux, text = 'Cadastro realizado com sucesso', width = 25).grid(row = 1, columnspan = 2)
			botao = Button(self.janela_aux, font = font1, text = 'Ok', bg = 'dodgerblue', command = self.janela_aux.destroy())
			botao.grid(row = 2, columnspan = 2)
			#indica que a janela criada é filha da janela mãe "toplevel"0
			self.janela_aux.transient(self.toplevel)
			#Mantém os eventos restritos a janela filha enquanto ela estiver aberta
			self.janela_aux.grab_set()
	def fechar(self):
		self.toplevel.destroy()	
		
		
instancia=Tk()
CadastraUsuario(instancia)
instancia.mainloop()
