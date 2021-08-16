import tkinter as tk
import main
from tkinter import messagebox
from decimal import Decimal, ROUND_HALF_UP

class Game(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 700
		self.bgcolor = 'forestgreen'
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)

		# 選ばれたカードの情報を一時保存 index 0=数字, 1=キャンバスタグ
		self.tempinfos = []

		# 消化して非表示にするキャンバスタグを格納
		self.hidetags = []

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
		for i in range(28):
			self.pyramiddeck.addCard(self.cards[0])
			self.cards.pop(0)

		import handDeck
		self.handdeck = handDeck.HandDeck(self.imagewidth, self.imageheight, self.WIDTH, self.HEIGHT)
		for i in range(24):
			self.handdeck.addCard(self.cards[0])
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
		elif tag == 'handcards':
			self.handdeck.drawOneCard()
			self.tempinfos.clear()
			self.repaint()
		else:
			num = -1
			if (num := self.deckobj.getNumWithTags(self.pyramiddeck.getCards(), tag)) != False:
				pass
			elif (num := self.deckobj.getNumWithTags(self.handdeck.getCards(), tag)) != False:
				pass
			elif (num := self.deckobj.getNumWithTags(self.handdeck.getTossCards(), tag)) != False:
				pass
			elif (num := self.deckobj.getNumWithTags(self.deckobj.getJokers(), tag)) != False:
				pass

			if len(self.tempinfos) == 0:
				# 1枚目の選択
				if num == 13:
					self.hidetags.append(tag)
				else:
					self.tempinfos.append([num, tag])

			elif len(self.tempinfos) == 1:
				# 2枚目の選択
				if num + self.tempinfos[0][0] == 13 or self.tempinfos[0][0] == 0 or num == 0:
					self.hidetags.extend([tag, self.tempinfos[0][1]])

				self.tempinfos.clear()

			self.repaint()
			if self.pyramiddeck.gameComplete() == True:
				messagebox.showinfo('メッセージ', '成功です。')
			self.repaint()
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
		self.pyramiddeck.paint(self.canvas, self.bgcolor, self.hidetags)
		self.deckobj.paintJokers(self.canvas, self.bgcolor, self.hidetags)
		self.handdeck.paint(self.canvas, self.bgcolor, self.hidetags)

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