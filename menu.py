import tkinter as tk
import main

class Menu(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 360
		self.bgcolor = 'forestgreen'
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)
		self.setController(controller)

		self.canvas = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		self.canvas.pack()

		self.paint()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def getController(self):
		return self.controller

	def setController(self, con):
		self.controller = con

	def mousePressed(self, event):
		tag = event.widget.gettags('current')[0]

		if tag in ['start', 'startrect']:
			main.show_frame('ゲームフレーム')
		if tag in ['howto', 'howtorect']:
			main.show_frame('あそびかたフレーム')
		elif tag in ['quit', 'quitrect']:
			self.getController().quit()

	def mouseEnter(self, event):
		tag = event.widget.gettags('current')[0]

		if tag in ['start', 'startrect']:
			event.widget.itemconfig('startrect', width = 5)
		if tag in ['howto', 'howtorect']:
			event.widget.itemconfig('howtorect', width = 5)
		elif tag in ['quit', 'quitrect']:
			event.widget.itemconfig('quitrect', width = 5)

	def repaint(self, event = None):
		self.canvas.delete('all')
		self.paint()

	def paint(self):
		self.canvas.create_text(320, 50, fill = 'white', text = 'メニュー', font = ('Arial', 36))

		# 開始ボタン
		self.canvas.create_rectangle(220, 105, 415, 155, fill = 'chocolate', outline = 'white', width = 1, tags = 'startrect')
		self.canvas.create_text(320, 130, fill = 'black', text = 'ゲーム開始', font = ('Arial', 32), tags = 'start')

		# 遊びかたボタン
		self.canvas.create_rectangle(220, 175, 415, 225, fill = 'chocolate', outline = 'white', width = 1, tags = 'howtorect')
		self.canvas.create_text(320, 200, fill = 'black', text = '遊びかた', font = ('Arial', 32), tags = 'howto')

		# 終了ボタン
		self.canvas.create_rectangle(220, 245, 415, 295, fill = 'chocolate', outline = 'white', width = 1, tags = 'quitrect')
		self.canvas.create_text(320, 270, fill = 'black', text = 'ゲーム終了', font = ('Arial', 32), tags = 'quit')

		# マウスイベント
		self.canvas.tag_bind('current', '<Enter>', self.mouseEnter)
		self.canvas.tag_bind('current', '<Leave>', self.repaint)
		self.canvas.tag_bind('current', '<ButtonPress-1>', self.mousePressed)