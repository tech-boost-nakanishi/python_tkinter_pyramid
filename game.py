import tkinter as tk
import main

class Game(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 700
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)

		tk.Label(self, text = 'ゲーム').pack()

		tk.Button(self, text = 'メニュー', command = lambda: main.show_frame('メニューフレーム')).pack()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT
