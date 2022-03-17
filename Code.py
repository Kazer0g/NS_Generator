import os

import random

from docx import Document
from docx.shared import Inches


from tkinter import *
import tkinter as tk


class Main_Window (tk.Tk):
	def __init__(self):
		super().__init__()

		self.actnum = 1

		self.cc = []
		self.mm = []

		self.li_full = []
		self.li_mark = []

		self.str_full = ""
		self.str_mark = ""
		self.st = ""

		self.left = ""
		self.right = ""
		self.left_cc = ""
		self.right_cc = ""

		self.varinants = []

		self.li_answears = []

		#-------------------------------------------------------------------------------------------------------------------Выбор один/много ответов)
		self.lot = IntVar()

		self.lotbtn = tk.Checkbutton (self, text="Одно решение", variable=self.lot)
		self.lotbtn.place (x=0, y=100)


		#------------------------------------------------------------------------------------------------------------Выбор активных систем счисления)
		self.lbl_numeralsystem = tk.Label (self, text="Системы счисления") 
		self.lbl_numeralsystem.place (x=0, y=0)

		self.c_2 = IntVar()
		self.c_10 = IntVar()
		self.c_16 = IntVar()

		self.cbtn_2 = tk.Checkbutton (self, text="2", variable=self.c_2)
		self.cbtn_2.place (x=0, y=20)
		self.cbtn_10 = tk.Checkbutton (self, text="10", variable=self.c_10)
		self.cbtn_10.place (x=0, y=40)
		self.cbtn_16 = tk.Checkbutton (self, text="16", variable=self.c_16)
		self.cbtn_16.place (x=0, y=60)
		
		#------------------------------------------------------------------------------------------------------------------Выбор диапазона значений)
		self.lbl_minmax = tk.Label (self, text="Диапазон от до") 
		self.lbl_minmax.place (x=160, y=0)

		self.ent_minval = tk.Entry (self, width=12)
		self.ent_minval.place (x=160, y=20)
		self.ent_maxval = tk.Entry (self, width=12)
		self.ent_maxval.place (x=160, y=40)

		#---------------------------------------------------------------------------------------------------------------------------Выбор сложности)
		self.lbl_difficult = tk.Label (self, text="Сложность 0-100") 
		self.lbl_difficult.place (x=280, y=0)

		self.ent_difficult = tk.Entry (self, width=12)
		self.ent_difficult.place (x=280, y=20)

		#---------------------------------------------------------------------------------------------------------------------------Кол-во примеров)
		self.lbl_times = tk.Label (self, text="Кол-во") 
		self.lbl_times.place (x=400, y=0)


		self.ent_times = tk.Entry (self, width=12)
		self.ent_times.place (x=400, y=20)
		#---------------------------------------------------------------------------------------------------------------------------Кнопка создания)
		self.btn_generate = tk.Button (self, text="Создать", command=self.generate)
		self.btn_generate.place (x=0, y=165)

	#----------------------------------------------------------------------------------------------------------------------Функция проверки integer)
	def int_check (self, a):
		try:
			int(a)
			return True
		except ValueError:
			return False
	
	#----------------------------------------------------------------------------------------------------------Функция создания дирикторий и файлов)
	def generate (self):
		self.createNum ()
		self.createTests ()
		self.createnewdir ()
		self.createfiles ()
		
		os.chdir("..")
		os.chdir("..")

		self.li_full.clear()
		self.li_mark.clear()
	
	#---------------------------------------------------------------------------------------------------------------------Функция создания равенства)
	def createNum (self):
		self.collectCC ()
		print ("Выбранные системы: ", self.cc)
		self.collectMM()
		print ("Max/Min:", self.mm)
		for i in range (int(self.ent_times.get())):
			self.rand()
			self.mark (self.left, self.right)
			if self.lot.get() != 1:
				self.li_full.append("Загаданное число в десятичной системе:" + str(self.actnum)+ "\n" + self.str_full)
				self.li_mark.append(self.str_mark)
			elif self.lot.get() == 1:
				self.li_full.append("Загаданное число в десятичной системе:" + str(self.actnum)+ "\n" + self.str_full)
				self.minvar ()
		print(self.li_full)
		print (self.li_mark)
		
	#------------------------------------------------------------------------------------------------------Функция сбора актуальных систем счисления)
	def collectCC (self):
		self.cc = []
		if self.c_2.get() == 1:
			self.cc.append (2)
		if self.c_10.get() == 1:
			self.cc.append(10)
		if self.c_16.get() == 1:
			self.cc.append(16)

	#--------------------------------------------------------------------------------------------------------------Функция сведения ответов к одному)
	def minvar (self):
		lr = self.str_mark.split("=")
		left = lr[0]
		right = lr[1]

		if len(left) >= len(right):
			self.variant (right, self.right_cc, self.left_cc)
		else:
			self.variant (left, self.left_cc, self.right_cc)

		
	#-----------------------------------------------------------------------------------------------------------------------Функция поиска вариантов)
	def variant (self, num, cc_num, cc_side):
		print (cc_num)
		print (num)
		count = 0
		self.varinants.clear()
		for i in str(num):
			if i == "*":
				count = count + 1
		print (count)

		for calk in range (cc_num**count):
			
			if cc_num == 2:
				cc_calk = bin(calk)
			elif cc_num == 10:
				cc_calk = int(calk)
			elif cc_num == 16:
				cc_calk = hex(calk)
			str_calk = str(cc_calk)
			str_num = str(num)

			if (len(str_calk) > 1) and (str_calk[1] == "x"):
				while len(str_calk[2:]) < count:
					str_calk = str_calk[:2] + "0" + str_calk[2:]
			else:
				while len(str_calk) < count:
					str_calk = "0" + str_calk

			if (len(str_calk) > 1) and (str_calk[1] == "x"):
				for letter in str_calk[2:]:
					str_num = str_num.replace ("*", letter, 1)
			else:
				for letter in str_calk:
					str_num = str_num.replace ("*", letter, 1)

			self.varinants.append(str_num)
		
		self.cutvar (num, cc_num, cc_side)
	#--------------------------------------------------------------------------------------------------------Функция сокращения количества вариантов)
	def cutvar (self, num, cc_num, cc_side):
		str_num = str(num)

		counter = dict()

		if (len(str_num) > 1) and (str_num[1] == "x"):
			for i in range (len(str_num)-2):
				for case in self.varinants:
					if case[2+i] in counter:
						counter[case[2+i]] = counter[case[2+i]] + 1
					else:
						counter[case[2+i]] = 1

		else:
			for i in range (len(str_num)):
				for case in self.varinants:
					if case[i] in counter:
						counter[case[i]] = counter[case[i]] + 1
					else:
						counter[case[i]] = 1
		print (counter)

	#------------------------------------------------------------------------------------------Функция сбора диапазона значений генерируегмого числа)
	def collectMM (self):
		numMin = self.ent_minval.get()
		numMax = self.ent_maxval.get()
		self.mm = []
		if self.int_check (numMin) == True:
			numMin = int(numMin)
			self.mm.append(numMin)
		else:
			print ("Некоректно введено минимальное значение")
			self.mm = []

		if self.int_check (numMax) == True:
			numMax = int(numMax)
			self.mm.append(numMax)
		else:
			print ("Некоректно введено максимальное значение")
			self.mm = []

		if numMin >numMax:
			print ("Некоректно введен диапазон")

	#---------------------------------------------------------------------------------------------------------Функция генерации рандомного равенства)
	def rand (self):
		self.actnum = random.randint(self.mm[0], self.mm[1])
		self.left_cc = self.cc[random.randint(0, len(self.cc))-1]
		self.right_cc = self.left_cc
		while self.left_cc == self.right_cc:
			self.right_cc = self.cc[random.randint(0, len(self.cc))-1]	
		if self.left_cc == 2:
			left = bin(self.actnum)
		elif self.left_cc == 10:
			left = int(self.actnum)
		elif self.left_cc ==16:
			left = hex(self.actnum)
		if self.right_cc == 2:
			right = bin(self.actnum)
		elif self.right_cc == 10:
			right = int(self.actnum)
		elif self.right_cc ==16:
			right = hex(self.actnum)

		self.left = left
		self.right = right

		self.str_full = str(left) + "=" + str(right)

	#-------------------------------------------------------------------------------------------------------Функция генерации закрашенного равенства)
	def mark (self, left, right):
		count = []
		procent = int(self.ent_difficult.get())
		self.str_mark = self.marker(left, procent) + "=" + self.marker(right, procent)

	#----------------------------------------------------------------------------------------------------------------------Функция расчета сложности)
	def marker (self, num, procent):
		self.st = str(num)

		pref = ""

		if self.st[0] == "0":
			pref = self.st[:2]
			self.st = self.st[2:]

		count = round((len(self.st)/100)*procent)
		for i in range (count):
			self.markering (self.st, procent)

		return pref + self.st
	
	#-----------------------------------------------------------------------------------------------------------------Функция закрашивания равенства)
	def markering (self, st, procent):
		index = random.randint(0, len(st)-1)
		if st[index] == "*":
			self.markering (st, procent)
		elif st[index] != "*":
			self.st = st[:index] + "*" + st[index+1:]
		return self.st

	#---------------------------------------------------------------------------------------------------------------Функция создания папки с тестами)
	def createTests (self):
		try:
			os.mkdir("Tests")
			os.chdir("Tests")
		except FileExistsError:
			os.chdir("Tests")
	
	#--------------------------------------------------------------------------------------------------------Функция создания папки с новыми тестами)
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
	
	#------------------------------------------------------------------------------------------------------------------------Функция создания файлов)
	def createfiles (self):
		#------------------------------------------------------------------------------------------------------------------------------------Задания)
		tasks = Document()
		tasks.add_heading ("Цифровая электроника", 0)
		tasks.add_heading ("Ученика(цы) __ класса \"___\" _______________________ ", 2)
		for i in self.li_mark:
			tasks.add_paragraph (i)

		tasks.save("Задачи.docx")

		#------------------------------------------------------------------------------------------------------------------------------------Ответы)
		answers = Document()
		answers.add_heading("Цифровая электроника", 0)
		for j in self.li_full:
			answers.add_paragraph(j)
		answers.save("Ответы.docx")
		

if __name__ == "__main__":
	main_window = Main_Window ()

	main_window.title ("NS")
	main_window.geometry ("500x400")

	main_window.mainloop()