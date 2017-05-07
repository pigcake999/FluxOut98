#Imports
from sys import *
import os
import urllib

# Classes
class Gui():
	def __init__(self):
		self.hasHeader = False
		self.guiheader = None
	def tc(self, val):
		self.textCol = val
	def bc(self, val):
		self.backCol = val
	def header(self, titleX, tcY, bcZ):
		self.hasHeader = True
		self.guiheader = {
			'title': titleX,
			'bc': bcZ,
			'tc': tcY
		}

class Terminal():
	def __init__(self):
		self.actions = []
	def Print(self, string,end):
		self.actions.append("PRINT")
		self.actions.append(string)
		self.actions.append(end)
	def PrintV(self, v,end):
		self.actions.append("PRINTV")
		self.actions.append(v)
		self.actions.append(end)
	def Input(self, txt, v):
		self.actions.append("INPUT")
		self.actions.append(txt)
		self.actions.append(v)
	def let(self, var):
		self.actions.append("LET")
		self.actions.append(var)
	def Quit(self):
		self.actions.append("EXIT_PROGRAM")

class FApplication():
	def __init__(self):
		self.isRunning = False
		self.hasLoaded = True
		self.title = "Flux Out 98"
	def loaded(self):
		return self.hasLoaded
	def Quit(self):
		self.isRunning = False
	def setTitle(self, title):
		self.title = title
	def run(self, usrgui, term):
		self.isRunning = True
		varchar = {}
		while self.isRunning:
			os.system("clear")
			stdout.write("\x1b]2;"+self.title+"\x07")
			if usrgui.hasHeader:
				text = usrgui.guiheader['title']
				starttabs = ""
				endtabs = ""
				if len(text) < 8:
					spaces = 8-len(text)
					i = 0
					if spaces == 1:
						starttabs += "\t"
						endtabs += "\t"
					else:
						while(i<spaces):
							starttabs += " "
							endtabs += "\t"
							i += 1
				if len(text)<8:
					text = starttabs+"\t\t\t\t\t"+text+"\t\t\t\t"+endtabs
				else:
					text = "\t\t\t\t"+text+"\t\t\t\t"
				print('\x1b[1;37;40m' + text + '\x1b[0m')
			j = 0
			frames = 1
			while(j<len(term.actions)):
				if term.actions[j] == "LET" and frames == 1:
					varchar[term.actions[j+1]] = ""
					j += 2
				elif term.actions[j] == "PRINT":
					print(term.actions[j+1], end=term.actions[j+2])
					j += 3
				elif term.actions[j] == "PRINTV":
					print(varchar[term.actions[j+1]], end=term.actions[j+2])
					j += 3
				elif term.actions[j] == "INPUT":
					varchar[term.actions[j+2]] = input(term.actions[j+1])
					j += 3
				elif term.actions[j] == "EXIT_PROGRAM":
					self.Quit()
					j += 1
				frames += 1
			if len(term.actions) == 0:
				input()