# -*- coding: utf-8

from Tkinter import *
import tkMessageBox
import os,sys,sqlite3
from tkFileDialog import *
from Admin import Administrador

class TabelaDados(object):
	def __init__(self, root, login, senha):
		self.login = login
		self.senha = senha
		self.adm = Administrador(self.login, self.senha)
		self.toplevel = root
		self.toplevel.title('Lista de dados')
		#IMAGEM PRINCIPAL
		self.photo = PhotoImage(file = '/home/petcomputacao/Documentos/sampaio/RUFELIZ/images/ru_dados.gif')	
		self.label = Label(self.toplevel, image = self.photo)
		self.label.image = self.photo
		self.label.grid(row = 0, column = 0, columnspan = 3)
		#recebendo os dados da classe Administrador
		self.matricula, self.email, self.alimentacao = self.adm.retorna_valores_lista()
		COLUNAS = 3 #são tres colunas de valores
		Label(self.toplevel, text = 'MATRICULA', font = ('Arial','11','bold')).grid(row = 2, column = 0, sticky = N+E+S+W)
		Label(self.toplevel, text = 'EMAIL',  font = ('Arial','11','bold')).grid(row = 2, column = 1, sticky = N+E+S+W )
		Label(self.toplevel, text = 'ALIMENTAÇÃO',  font = ('Arial','11','bold')).grid(row = 2, column = 2, sticky = N+E+S+W)
		for i in range(len(self.matricula)):
			label = Label(self.toplevel, text = '%s' %str(self.matricula[i])).grid(row = i+4, column = 0, sticky = N+E+S+W)
			label = Label(self.toplevel, text = '%s' %str(self.email[i])).grid(row = i+4, column = 1,  sticky = N+E+S+W)
			label = Label(self.toplevel, text = '%s' %str(self.alimentacao[i])).grid(row = i+4, column = 2,  sticky = N+E+S+W)
			
			


