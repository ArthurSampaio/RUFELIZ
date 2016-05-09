#coding: utf-8

#TELA DE ENVIAR EMAIL 
import anydbm
from SendEmail import SendEmail
from Admin import Administrador
from Tkinter import *

class Email(object): 
	def __init__(self, toplevel, login, email): 
		self.login = login
		self.senha = email
		#INICIALIZANDO O CANVAS E OS FRAMES
		self.toplevel = toplevel 
		self.toplevel.title('RUFELIZ - Envio de emails')
		
		#IMAGEM PRINCIPAL
		self.photo = PhotoImage(file = '/home/petcomputacao/Documentos/sampaio/RUFELIZ/images/ru_send.gif')	
		self.label = Label(self.toplevel, image = self.photo)
		self.label.image = self.photo
		self.label.grid(row = 0, column = 0)	
		
		#Campo do assunto
		font1 = ('Arial', '10', 'bold')
		Label(self.toplevel, text = 'Assunto: ', font = font1, width = 14).grid()
		self.subject = Entry(self.toplevel, width = 50, font = font1)
		self.subject.focus_force()
		self.subject.grid()
		#Campo da mensagem 
		Label(self.toplevel, text = 'Mensagem: ', font = font1, width = 10).grid()
		self.mensagem = Text(self.toplevel, height = 15, padx = 5, pady = 5)
		self.mensagem.grid()
		#Botoẽs de enviar e fechar tela
		self.enviar = Button(self.toplevel, font = font1, text = 'Enviar',  bg='dodgerblue', command= self.enviar).grid()
		self.fechar = Button(self.toplevel, font = font1, text = 'Fechar',  bg='dodgerblue', command= self.fechar).grid(row = 89, column = 0  )
		#MENSAGEM
		self.msg=Label(self.toplevel,font=font1, height=3,text='AGUARDANDO...')
		self.msg.grid()
		
	def enviar (self): 
		mensagem = self.mensagem.get("1.0", END).encode("utf-8")
		mensagem += '\nCordialmente,\nRUFELIZ - Ligando o Restaurante Universitário com Você'
		mensagem += '\nRUFELIZ é um projeto de Arthur Sampaio para a disciplina de Programação I da UFCG.'
		assunto = self.subject.get()	

		email = SendEmail(self.login,self.senha)
		self.msg['text'] = 'REALIZANDO CONEXÃO'
		
		if email.conexao():
			self.msg ['text'] = 'CONEXÃO REALIZADA COM SUCESSO'
			self.msg ['fg'] = 'green'
		else: 
			self.msg ['text'] = 'ALGUM ERRO OCORREU.'
			self.msg['fg'] = 'red'
		
		adm = Administrador(self.login, self.senha)
		a_enviar = adm.retorna_email()
		enviou = False
		for end in a_enviar: 
			if email.send_mail(end, assunto, mensagem):
				enviou = True
			else: enviou = False
		
		if enviou: 
			self.msg ['text'] = 'EMAILS ENVIADOS COM SUCESSO'
			self.msg['fg'] = 'blue'
				
	def fechar (self): 
		self.toplevel.destroy()

