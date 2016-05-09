# coding: utf-8
# TELA DE LOGIN 

from Admin import Administrador
from Tkinter import *


class Login:
	def __init__(self,toplevel): 
		#FRAMES
		self.toplevel = toplevel
		self.toplevel.title('RUFELIZ - Ligando o RU com a comunidade')
		self.frame1=Frame(toplevel,padx = 10, pady = 15)
		self.frame1.grid()
		self.frame2=Frame(toplevel, padx = 15, pady = 5)
		self.frame2.grid()
		self.frame3=Frame(toplevel)
		self.frame3.grid()
		self.frame4=Frame(toplevel,pady=10)
		self.frame4.grid()
		self.frame5 = Frame(toplevel, pady = 10).grid()
		
		#FOTOS 
		self.photo = PhotoImage(file = '/home/petcomputacao/Documentos/sampaio/RUFELIZ/images/ufcg.gif')	
		self.label = Label(image = self.photo)
		self.label.image = self.photo
		self.label.grid(row = 0, column = 0)	
		
		#MENSAGENS E CORPO DO NOME E SENHA		
		Label(self.frame1,text='RU FELIZ', fg='darkblue',
		font=('Arial','14','bold'), height=3).grid()
		fonte1=('Arial','10','bold')
		Label(self.frame2,text='Nome: ',font=fonte1,width=8).grid()
		self.nome=Entry(self.frame2,width=50, font=fonte1)
		self.nome.focus_force() # Para o foco começar neste campo
		self.nome.grid()
		Label(self.frame3,text='Senha: ',
		font=fonte1,width=8).grid()	
		self.senha=Entry(self.frame3,width=50,show='*', font=fonte1)
		self.senha.grid()
		#BOTÃO DE CONFERIR
		self.confere=Button(self.frame4, font=fonte1, text='Confirmar', bg='dodgerblue', command=self.conferir).grid()
		#BOTAO DE SAIR
		self.fecha = Button(self.frame4, font = fonte1, text = 'Sair', bg = 'dodgerblue', command = self.sair).grid()
		

		self.msg=Label(self.frame5,font=fonte1, height=3,text='AGUARDANDO...')
		self.msg.grid()

	def conferir(self):
		NOME=self.nome.get()
		SENHA=self.senha.get()
		self.login = Administrador (NOME, SENHA)
		
		if self.login.verifica_login():
			self.msg['text']='ACESSO PERMITIDO'
			self.msg['fg']='darkgreen'
			self.toplevel.destroy()
		else:
			self.msg['text']='ACESSO NEGADO'
			self.msg['fg']='red'
			self.nome.focus_force()
			
	def retorna (self):
		return self.login.verifica_login()

	def retorna_dados(self):
		return self.login.login_senha()

	def sair(self): self.toplevel.destroy()
		



