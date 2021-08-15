import tkinter as tk
import main
from decimal import Decimal, ROUND_HALF_UP

class Game(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 700
		self.bgcolor = 'forestgreen'
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)

		self.reduction_ratio = 9  #縮小率
		self.imagewidth = int(Decimal(str(712 / self.reduction_ratio)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
		self.imageheight = int(Decimal(str(1008 / self.reduction_ratio)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

		# 52枚のカードを生成
		import deck
		self.deckobj = deck.Deck(self.imagewidth, self.imageheight, self.WIDTH)
		self.deckobj.shuffleCards()
		self.cards = self.deckobj.cards

		import pyramidDeck
		self.pyramiddeck = pyramidDeck.PyramidDeck(self.imagewidth, self.imageheight, self.WIDTH, self.HEIGHT)
		for i in range(len(self.pyramiddeck.infos)):
			self.pyramiddeck.addCard(self.cards[0])
			self.cards.pop(0)

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
		self.pyramiddeck.paint(self.canvas, self.bgcolor)
		self.deckobj.paintJokers(self.canvas, self.bgcolor)

		# 最初からボタン
		self.canvas.create_rectangle(10, 640, 205, 690, fill = 'chocolate', outline = 'white', width = 1, tags = 'restartrect')
		self.canvas.create_text(110, 665, fill = 'black', text = '最初から', font = ('Arial', 32), tags = 'restart')

		# 遊びかたボタン
		self.canvas.create_rectangle(220, 640, 415, 690, fill = 'chocolate', outline = 'white', width = 1, tags = 'howtorect')
		self.canvas.create_text(320, 665, fill = 'black', text = '遊びかた', font = ('Arial', 32), tags = 'howto')

		# メニューボタン
		self.canvas.create_rectangle(430, 640, 625, 690, fill = 'chocolate', outline = 'white', width = 1, tags = 'menurect')
		self.canvas.create_text(530, 665, fill = 'black', text = 'メニューへ', font = ('Arial', 32), tags = 'menu')

		# マウスイベント
		self.canvas.tag_bind('current', '<Enter>', self.mouseEnter)
		self.canvas.tag_bind('restartrect', '<Leave>', self.repaint)
		self.canvas.tag_bind('howtorect', '<Leave>', self.repaint)
		self.canvas.tag_bind('menurect', '<Leave>', self.repaint)
		self.canvas.tag_bind('current', '<ButtonPress-1>', self.mousePressed)
		# self.canvas.tag_bind('current', '<ButtonRelease-1>', self.repaint)