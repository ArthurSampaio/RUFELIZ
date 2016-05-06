# -*- coding: utf-8

from Tkinter import *
import tkMessageBox
import os,sys,sqlite3
from tkFileDialog import *
from Admin import Administrador

class TabelaDados():
	def __init__(self, root):
		self.adm = Administrador('rufelizp1@gmail.com','projetoru')
		self.master = root
		self.master.title('Lista de dados')
		kanvas = Canvas(self.master, width = 450, height = 100, bg = 'darkblue').grid(row = 0, column = 1, columns = 3,sticky = N+E+S+W )	
		Label(self.master, text = 'DADOS CADASTRADOS', fg = 'darkblue', font = ('Arial', '22', 'bold'), height = 3).grid(row = 1, column = 1, columnspan = 3, sticky = N+E+S+W)
		self.matricula, self.email, self.alimentacao = self.adm.retorna_valores_lista()
		COLUNAS = 3 #são tres colunas de valores
		Label(self.master, text = 'MATRICULA', font = ('Arial','11','bold')).grid(row = 2, column = 1, padx = 10, pady = 10, sticky = N+E+S+W)
		Label(self.master, text = 'EMAIL',  font = ('Arial','11','bold')).grid(row = 2, column = 2,padx = 10, pady = 10, sticky = N+E+S+W )
		Label(self.master, text = 'ALIMENTAÇÃO',  font = ('Arial','11','bold')).grid(row = 2, column = 3, padx = 10, pady = 10, sticky = N+E+S+W)
		for i in range(len(self.matricula)):
			label = Label(self.master, text = '%s' %str(self.matricula[i])).grid(row = i+4, column = 1, sticky = N+E+S+W)
			label = Label(self.master, text = '%s' %str(self.email[i])).grid(row = i+4, column = 2,  sticky = N+E+S+W)
			label = Label(self.master, text = '%s' %str(self.alimentacao[i])).grid(row = i+4, column = 3,  sticky = N+E+S+W)
			
			


