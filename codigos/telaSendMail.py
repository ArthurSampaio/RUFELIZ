#coding: utf-8

#TELA DE ENVIAR EMAIL 
import anydbm
from SendEmail import SendEmail
from Admin import Administrador
from Tkinter import *

class Email(object): 
	def __init__(self, toplevel): 
		self.login = 'rufelizp1@gmail.com'
		self.senha = 'projetoru'
		#INICIALIZANDO O CANVAS E OS FRAMES
		self.kanvas = Canvas(toplevel, width = 50, height = 100).pack()
		self.toplevel = toplevel 
		self.toplevel.title('RUFELIZ - ENVIO DE EMAILS')
		self.frame1 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame2 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame3 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame4 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame5 = Frame(toplevel, padx = 5, pady = 5).pack()
		
		#MENSAGEM DE TELA 
		Label(self.frame1, text = 'RU FELIZ - ENVIO DE EMAILS', fg = 'darkblue', font = ('Arial', '22', 'bold'), height = 3).pack()
		#Campo do assunto
		font1 = ('Arial', '10', 'bold')
		Label(self.frame2, text = 'Assunto: ', font = font1, width = 14).pack(side = LEFT)
		self.assunto = Entry(self.frame2, width = 50).pack(side = LEFT)
		#Campo da mensagem 
		Label(self.frame3, text = 'Mensagem: ', font = font1, width = 14).pack(side = LEFT)
		self.mensagem = Text(self.frame2, height = 20, padx = 5, pady = 5)
		self.mensagem.pack(side = LEFT)
		#Botoẽs de enviar e fechar tela
		self.enviar = Button(self.frame4, font = font1, text = 'Enviar',  bg='dodgerblue', command= self.enviar).pack(side = BOTTOM)
		self.fechar = Button(self.frame4, font = font1, text = 'Fechar',  bg='dodgerblue', command= self.fechar).pack(side = BOTTOM)
		#MENSAGEM
		self.msg=Label(self.frame5,font=font1, height=3,text='AGUARDANDO...')
		self.msg.pack(side = BOTTOM)
		
	def enviar (self): 
		mensagem = self.mensagem.get("1.0", END).encode("utf-8")
		email = SendEmail(self.login,self.senha)
		if email.conexao():
			self.msg ['text'] = 'CONEXÃO REALIZADA COM SUCESSO'
			self.msg ['fg'] = 'green'
		else: 
			self.msg ['text'] = 'ALGUM ERRO OCORREU.'
			self.msg['fg'] = 'red'
		
		adm = Administrador(self.login, self.senha)
		a_enviar = adm.retorna_email()
		for end in a_enviar: 
			email.send_mail(end, self.assunto, mensagem)
	
		
	def fechar (self): 
		self.toplevel.destroy()
		

instancia=Tk()
Email(instancia)
instancia.mainloop()
		
