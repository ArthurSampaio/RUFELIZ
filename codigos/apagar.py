import Tkinter as tk
from Tkinter import *
import tkMessageBox
import os,sys,sqlite3
from tkFileDialog import *
from Admin import Administrador

class App():
	def __init__(self, root):
		adm = Administrador('rufelizp1@gmail.com','projetoru')
		self.master = root
		self.master.protocol("WM_DELETE_WINDOW", self.close_window)
		self.text = tk.Text(root)
		a = adm.__str__()
		self.text.insert(END,a)
			
		self.text.pack()

	def close_window(self):
		text = self.text.get("1.0",END).encode("utf-8")
		print text
		self.master.destroy()

root = tk.Tk()
app = App(root)
root.mainloop()


