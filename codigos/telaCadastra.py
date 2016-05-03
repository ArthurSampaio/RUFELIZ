# coding: utf-8 
#TELA DE CADASTRAR NOVO COMENSAL

from Admin import Administrador
from SendEmail import SendEmail
from Tkinter import *

class CadastraUsuario(object):
	def __init__(self, toplevel): 
		#INICIALIZANDO KANVAS E FRAMES 
		kanvas = Canvas(toplevel, width = 300, height = 100, bg = 'darkblue').pack()
		self.toplevel = toplevel
		self.toplevel.title('RUFELIZ - Cadastro de novo comensal')
		self.frame1 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame2 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame3 = Frame(toplevel, padx = 15, pady = 20).pack()
		self.frame4 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame5 = Frame(toplevel, padx = 5, pady = 5).pack()
		#TEXTO PRINCIPAL
		Label(self.frame1, text = 'CADASTRO DE USUÁRIO', fg = 'darkblue', font = ('Arial', '22', 'bold'), height = 3).pack()
		font1 = ('Arial', '10', 'bold')
		#PARA MATRICULA 
		Label(self.frame2, text = 'Matricula: ', font = font1, width = 14).pack(side = LEFT)
		self.matricula = Entry(self.frame2, width = 20, font = font1)
		self.matricula.focus_force()
		self.matricula.pack(side = LEFT)
		#PARA EMAIL 
		Label(self.frame2, text = 'Email: ', font = font1, width = 14).pack(side = LEFT)
		self.matricula = Entry(self.frame2, width = 20, font = font1)
		self.matricula.focus_force()
		self.matricula.pack(side = LEFT)
		#PARA A CAIXA DROPDOWN DA ALIMENTAÇÃO
		Label(self.frame3, text = 'Alimentação: ', font = font1, width = 14).pack(side = LEFT)
		var = StringVar(toplevel)
		var.set(' ') #valor inicial do dropdown
		escolhas = ['Vegetariano', 'Carnívoro']
		opcao = OptionMenu(self.frame3, var, *escolhas)
		opcao.pack(side = LEFT, padx = 10, pady = 10)
		#para utilizar a escolha dentro da opcao usar o metodo var.get()
		
		
instancia=Tk()
CadastraUsuario(instancia)
instancia.mainloop()
