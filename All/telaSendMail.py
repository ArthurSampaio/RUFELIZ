#coding: utf-8

#TELA DE ENVIAR EMAIL 
import anydbm
from SendEmail import SendEmail
from Admin import Administrador
from Tkinter import *
import tkMessageBox
import os,sys,sqlite3
from tkFileDialog import *


class Email(object): 
	def __init__(self, toplevel, login, email): 
		self.login = login
		self.senha = email
		self.toplevel = toplevel 
		self.toplevel.title('RUFELIZ - Envio de emails')
		#fonte utilizada
		self.font1 = ('Arial', '10', 'bold')
	
			
		#IMAGEM PRINCIPAL
		self.photo = PhotoImage(file = './images/ru_send.gif')	
		self.label = Label(self.toplevel, image = self.photo)
		self.label.image = self.photo
		self.label.grid(row = 0, column = 0, columnspan = 2)	
		
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
		
		#menu
		menubar = Menu(toplevel)
		filemenu = Menu(menubar,tearoff=0)
		filemenu.add_command(label = "Novo")	
		filemenu.add_command(label="Salvar Como", command = self.salvar_como)
		filemenu.add_command(label ="Abrir Arquivo")
		filemenu.add_command(label="Sair", command = self.fechar)
		menubar.add_cascade(label="Arquivo",menu=filemenu)
		toplevel.config(menu=menubar)
		
		
		
	def enviar (self): 
		mensagem = self.mensagem.get("1.0", END).encode("utf-8")
		mensagem += '\nCordialmente,\nRUFELIZ - Ligando o Restaurante Universitário com Você'
		mensagem += '\nRUFELIZ é um projeto de Arthur Sampaio para a disciplina de Programação I da UFCG.'
		assunto = self.subject.get()	
		#realiza conexão com o servidor SMTP
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
		
				 
		#Implementando uma caixa de diálogo para aparecer quando ocorrer a ação de enviar (nesta caso, quando for True)
		self.janela_aux = Toplevel(self.toplevel)
		if enviou:
			Label(self.janela_aux, text = 'Emails enviados com sucesso', width = 50, font = self.font1).grid()
		else: 
			Label(self.janela_aux, text = 'Ocorreu um Erro. Tente novamente', width = 50, font = self.font1).grid()
		botao = Button(self.janela_aux,text = 'Ok', command = self.fechar_dialogo).grid()
		#indica que a janela criada é filha da janela mãe "toplevel"0
		self.janela_aux.transient(self.toplevel)
		#Mantém os eventos restritos a janela filha enquanto ela estiver aberta
		self.janela_aux.grab_set()
				
	def fechar (self): 
		self.toplevel.destroy()
		
	
	def salvar_como(self): 
		filename = str(asksaveasfilename(title="Save as File",defaultextension=".txt",filetypes=[('text file','.txt')]))
		if len(filename) > 0:
			f = open(filename,"w")
			text = self.mensagem.get("1.0",END).encode("utf-8")
			f.write(text)
			f.close()
			self.file_name = filename
			self.master.title(filename[filename.rfind("/")+1:] + ": RUFELIZ")
			self.changed = False
        





instancia=Tk()
Email(instancia, 'yuhuh', 'UHUH')
instancia.mainloop()
