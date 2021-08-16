import tkinter as tk
import random
from PIL import Image, ImageTk

class Deck():

	def __init__(self, imagewidth, imageheight, gwidth):
		self.cards = []
		self.jokers = []
		self.suits = ['diamond', 'club', 'heart', 'spade']
		self.imagewidth = imagewidth
		self.imageheight = imageheight
		self.gwidth = gwidth
		self.basisX = self.gwidth // 2
		self.jokerY = 30
		self.infos = [
			[self.basisX - self.imagewidth * 4 + 10, self.jokerY],
			[self.basisX - self.imagewidth * 3 + 20, self.jokerY],
			[self.basisX + self.imagewidth * 3 - 10, self.jokerY],
			[self.basisX + self.imagewidth * 2 - 20, self.jokerY],
		]

		import card
		for suit in self.suits:
			for num in range(1, 14):
				img=ImageTk.PhotoImage(Image.open('images/' + suit + '/' + str(num) + '.png').convert('RGB').resize(size=(self.imagewidth, self.imageheight)))

				obj = card.Card(
					suit = suit,
					num = num,
					state = 0,
					tags = suit + str(num),
					image = img
				)
				self.cards.append(obj)

		# ジョーカー4枚生成
		img=ImageTk.PhotoImage(Image.open('images/joker.png').convert('RGB').resize(size=(self.imagewidth, self.imageheight)))
		for i in range(4):
			obj = card.Card(
				suit = 'joker',
				num = 0,
				state = 1,
				tags = 'joker' + str(i + 1),
				image = img
			)
			self.jokers.append(obj)

	def shuffleCards(self):
		random.shuffle(self.cards)

	def getJokers(self):
		return self.jokers

	def getNumWithTags(self, cards, tag):
		for card in cards:
			if card.getTags() == tag:
				return card.getNum()

		return False

	def paintJokers(self, canvas, bgcolor, hidetags):
		i = 0
		for card in self.jokers:
			if card.getTags() in hidetags:
				card.setState(2)
				i += 1
				continue

			canvas.create_image(self.infos[i][0], self.infos[i][1], image = card.getImage(), anchor = tk.NW, tags = card.getTags())
			canvas.create_line(self.infos[i][0], self.infos[i][1], self.infos[i][0], self.infos[i][1] + self.imageheight, fill = bgcolor, tags = card.getTags() + 'line')
			canvas.create_line(self.infos[i][0], self.infos[i][1], self.infos[i][0] + self.imagewidth, self.infos[i][1], fill = bgcolor, tags = card.getTags() + 'line')
			canvas.create_line(self.infos[i][0] + self.imagewidth, self.infos[i][1], self.infos[i][0] + self.imagewidth, self.infos[i][1] + self.imageheight, fill = bgcolor, tags = card.getTags() + 'line')
			canvas.create_line(self.infos[i][0], self.infos[i][1] + self.imageheight, self.infos[i][0] + self.imagewidth, self.infos[i][1] + self.imageheight, fill = bgcolor, tags = card.getTags() + 'line')

			i += 1