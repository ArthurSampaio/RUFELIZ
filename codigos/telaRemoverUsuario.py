# coding: utf-8 
#TELA DE CADASTRAR NOVO COMENSAL

from Admin import Administrador
from Tkinter import *

class RemoveUsuario(object): 
	def __init__(self, toplevel, login, senha): 
		self.login = login
		self.senha = senha
		#INICIALIZANDO KANVAS 
		kanvas = Canvas(toplevel, width = 450, height = 100, bg = 'darkblue').grid(row = 0, columnspan = 4)	
		self.toplevel = toplevel
		self.toplevel.title('RUFELIZ - Remover usário')
		
		#TEXTO PRINCIPAL
		
		Label(self.toplevel, text = 'REMOÇÃO DE USUÁRIO', fg = 'darkblue', font = ('Arial', '22', 'bold'), height = 3).grid(row = 1, columnspan = 4)
		self.font1 = ('Arial', '10', 'bold')
		
		#PARA MATRICULA 
		frameM = Frame(self.toplevel, padx = 5, pady = 5).grid(row = 2)
		Label(self.toplevel, text = 'Matricula: ', font = self.font1, width = 14).grid(row = 2, column = 1)
		self.matricula = Entry(self.toplevel, width = 25,font = self.font1)
		self.matricula.grid(row = 2, column = 2)
	
		#DEFININDO OS BOTÕES DE REMOVER E FECHAR
		self.botao_remover = Button(self.toplevel, font = self.font1, text = 'Remover', bg='dodgerblue', command= self.remover)
		self.botao_remover.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10)
		self.botao_fechar = Button(self.toplevel, font = self.font1, text = 'Fechar', bg = 'dodgerblue', command = self.fechar)
		self.botao_fechar.grid(row = 5, column = 2, columnspan = 2)
		
	def remover(self): 
		adm = Administrador (self.login, self.senha)
		self.janela_aux = Toplevel()
		if adm.remove_usuario(self.matricula.get()): 
			Label(self.janela_aux, text = 'Remoção realizada com sucesso', width = 50, font = self.font1).grid()
		else: 
			Label(self.janela_aux, text = 'O usuário não consta no Banco de Dados\nImpossível de remover', width = 50, font = self.font1).grid()
		botao = Button(self.janela_aux,text = 'Ok', command = self.fechar_dialogo).grid()
		#indica que a janela criada é filha da janela mãe "toplevel"0
		self.janela_aux.transient(self.toplevel)
		#Mantém os eventos restritos a janela filha enquanto ela estiver aberta
		self.janela_aux.grab_set()
	
	def fechar_dialogo(self):
		self.janela_aux.destroy()
			
	def fechar(self):
		self.toplevel.destroy()	
