import tkinter as tk
import main

class Game(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 700
		self.bgcolor = 'forestgreen'
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)

		# 52枚のカードを生成
		import deck
		self.deckobj = deck.Deck()
		self.deckobj.shuffleCards()
		self.cards = self.deckobj.cards
		self.imagewidth, self.imageheight = self.deckobj.imagewidth, self.deckobj.imageheight

		self.canvas = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		self.canvas.pack()

		self.paint()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def repaint(self, event = None):
		self.canvas.delete('all')
		self.paint()

	def mousePressed(self, event):
		tag = event.widget.gettags('current')[0]

		if tag in ['restart', 'restartrect']:
			main.show_frame('ゲームフレーム')
		elif tag in ['howto', 'howtorect']:
			main.show_frame('あそびかたフレーム')
		elif tag in ['menu', 'menurect']:
			main.show_frame('メニューフレーム')
		else:
			event.widget.itemconfig(tag + 'line', width = 3, fill = 'cyan')

	def mouseEnter(self, event):
		tag = event.widget.gettags('current')[0]

		if tag in ['restart', 'restartrect']:
			event.widget.itemconfig('restartrect', width = 5)
		elif tag in ['howto', 'howtorect']:
			event.widget.itemconfig('howtorect', width = 5)
		elif tag in ['menu', 'menurect']:
			event.widget.itemconfig('menurect', width = 5)

	def paint(self):
		self.canvas.create_image(50, 50, image = self.cards[0].getImage(), anchor = tk.NW, tags = 'image')
		self.canvas.create_line(50, 50, 50, 50 + self.imageheight, fill = self.bgcolor, tags = 'imageline')
		self.canvas.create_line(50, 50, 50 + self.imagewidth, 50, fill = self.bgcolor, tags = 'imageline')
		self.canvas.create_line(50 + self.imagewidth, 50, 50 + self.imagewidth, 50 + self.imageheight, fill = self.bgcolor, tags = 'imageline')
		self.canvas.create_line(50, 50 + self.imageheight, 50 + self.imagewidth, 50 + self.imageheight, fill = self.bgcolor, tags = 'imageline')

		self.canvas.create_image(350, 350, image = self.cards[1].getImage(), anchor = tk.NW, tags = 'image2')
		self.canvas.create_line(350, 350, 350, 350 + self.imageheight, fill = self.bgcolor, tags = 'image2line')
		self.canvas.create_line(350, 350, 350 + self.imagewidth, 350, fill = self.bgcolor, tags = 'image2line')
		self.canvas.create_line(350 + self.imagewidth, 350, 350 + self.imagewidth, 350 + self.imageheight, fill = self.bgcolor, tags = 'image2line')
		self.canvas.create_line(350, 350 + self.imageheight, 350 + self.imagewidth, 350 + self.imageheight, fill = self.bgcolor, tags = 'image2line')

		# 最初からボタン
		self.canvas.create_rectangle(10, 635, 205, 685, fill = 'chocolate', outline = 'white', width = 1, tags = 'restartrect')
		self.canvas.create_text(110, 660, fill = 'black', text = '最初から', font = ('Arial', 32), tags = 'restart')

		# 遊びかたボタン
		self.canvas.create_rectangle(220, 635, 415, 685, fill = 'chocolate', outline = 'white', width = 1, tags = 'howtorect')
		self.canvas.create_text(320, 660, fill = 'black', text = '遊びかた', font = ('Arial', 32), tags = 'howto')

		# メニューボタン
		self.canvas.create_rectangle(430, 635, 625, 685, fill = 'chocolate', outline = 'white', width = 1, tags = 'menurect')
		self.canvas.create_text(530, 660, fill = 'black', text = 'メニューへ', font = ('Arial', 32), tags = 'menu')

		# マウスイベント
		self.canvas.tag_bind('current', '<Enter>', self.mouseEnter)
		self.canvas.tag_bind('current', '<Leave>', self.repaint)
		self.canvas.tag_bind('current', '<ButtonPress-1>', self.mousePressed)
		self.canvas.tag_bind('current', '<ButtonRelease-1>', self.repaint)