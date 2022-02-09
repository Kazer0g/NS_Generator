import os

from docx import Document
from docx.shared import Inches


from tkinter import *
import tkinter as tk

class Save_Window (tk.Tk):
	def __init__(self, parent):
		super().__init__()

class Main_Window (tk.Tk):
	def __init__(self):
		super().__init__()

		self.lbl_numeralsystem = tk.Label (self, text="Системы счисления")
		self.lbl_numeralsystem.place (x=0, y=0)

		c_2 = IntVar()
		c_10 = IntVar()
		c_16 = IntVar()


		self.cbtn_2 = tk.Checkbutton (self, text="2", variable=c_2)
		self.cbtn_2.place (x=0, y=20)
		self.cbtn_10 = tk.Checkbutton (self, text="10", variable=c_10)
		self.cbtn_10.place (x=0, y=40)
		self.cbtn_16 = tk.Checkbutton (self, text="16", variable=c_16)
		self.cbtn_16.place (x=0, y=60)

		self.btn_save = tk.Button (self, text="Дополнительные настройки", command=self.open_save)
		self.btn_save.place (x=0, y=140)

		

		self.btn_generate = tk.Button (self, text="Создать", command=self.generate)
		self.btn_generate.place (x=0, y=165)

	def open_save (self):
		save_window = Save_Window(self)

	def generate (self):
		self.createTests ()
		self.createnewdir ()
		self.createfiles ()
		os.chdir("..")
		os.chdir("..")
		

	def createTests (self):
		try:
			os.mkdir("Tests")
			os.chdir("Tests")
		except FileExistsError:
			os.chdir("Tests")

	def createnewdir (self):
		flag = False
		i = 1
		while flag == False:
			try:
				os.mkdir("Ребусы " + str(i))
				flag = True
			except FileExistsError:
				i += 1
		
		os.chdir("Ребусы " + str(i))

	def createfiles (self):
		tasks = Document()
		tasks.add_heading ("Заголовок")
		tasks.save("Задачи.docx")

		answers = Document()
		answers.add_heading("Заголовок")
		answers.save("Ответы.docx")
		

if __name__ == "__main__":
	main_window = Main_Window ()

	main_window.title ("NS")
	main_window.geometry ("500x400")

	main_window.mainloop()