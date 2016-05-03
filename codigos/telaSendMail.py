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
		self.kanvas = Canvas(toplevel, width = 500, height = 100, bg = 'darkblue').pack()
		self.toplevel = toplevel 
		self.toplevel.title('RUFELIZ - ENVIO DE EMAILS')
		self.frame1 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame2 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame3 = Frame(toplevel, padx = 15, pady = 20).pack()
		self.frame4 = Frame(toplevel, padx = 5, pady = 5).pack()
		self.frame5 = Frame(toplevel, padx = 5, pady = 5).pack()
		
		#MENSAGEM DE TELA 
		Label(self.frame1, text = 'RU FELIZ - ENVIO DE EMAILS', fg = 'darkblue', font = ('Arial', '22', 'bold'), height = 3).pack()
		#Campo do assunto
		font1 = ('Arial', '10', 'bold')
		Label(self.frame2, text = 'Assunto: ', font = font1, width = 14).pack()
		self.subject = Entry(self.frame2, width = 50, font = font1)
		self.subject.focus_force()
		self.subject.pack()
		#Campo da mensagem 
		Label(self.frame3, text = 'Mensagem: ', font = font1, width = 14).pack(side = LEFT)
		self.mensagem = Text(self.frame3, height = 20, padx = 5, pady = 5)
		self.mensagem.pack(side = LEFT)
		#Botoẽs de enviar e fechar tela
		self.enviar = Button(self.frame4, font = font1, text = 'Enviar',  bg='dodgerblue', command= self.enviar).pack(side = TOP)
		self.fechar = Button(self.frame4, font = font1, text = 'Fechar',  bg='dodgerblue', command= self.fechar).pack(side = TOP)
		#MENSAGEM
		self.msg=Label(self.frame5,font=font1, height=3,text='AGUARDANDO...')
		self.msg.pack()
		
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
		

instancia=Tk()
Email(instancia)
instancia.mainloop()
		
