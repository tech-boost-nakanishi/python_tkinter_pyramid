import tkinter as tk

class HandDeck():

	def __init__(self, imagewidth, imageheight, gwidth, gheight):
		self.cards = []
		self.tosscards = []
		self.drawcount = 0
		self.imagewidth = imagewidth
		self.imageheight = imageheight
		self.gwidth = gwidth
		self.gheight = gheight
		self.handcardsX = self.gwidth - self.imagewidth * 1.5
		self.drawcardX = self.handcardsX - self.imagewidth - 20
		self.tossX = self.imagewidth * 1.5
		self.Y = self.imageheight * 4.5

	def addCard(self, card):
		self.cards.append(card)

	def getDrawCount(self):
		return self.drawcount

	def addDrawCount(self):
		self.drawcount += 1

	def drawOneCard(self):
		if len(self.cards) < 1:
			return

		if self.getDrawCount() == 0:
			self.addDrawCount()
		elif self.getDrawCount() > 0:
			self.tosscards.append(self.cards[0])
			self.cards.pop(0)
			self.addDrawCount()

	def getCards(self):
		return self.cards

	def getTossCards(self):
		return self.tosscards

	def paint(self, canvas, bgcolor, hidetags):
		# 残りのカード
		if len(self.cards) > 1:
			canvas.create_rectangle(self.handcardsX, self.Y, self.handcardsX + self.imagewidth, self.Y + self.imageheight, fill = 'firebrick', outline = 'black', width = 1, tags = 'handcards')

		# 引かれたカード
		if self.cards[0].getTags() in hidetags:
			self.cards[0].setState(2)
		else:
			if self.getDrawCount() > 0:
				if len(self.cards) > 0:
					canvas.create_image(self.drawcardX, self.Y, image = self.cards[0].getImage(), anchor = tk.NW, tags = self.cards[0].getTags())
					canvas.create_line(self.drawcardX, self.Y, self.drawcardX, self.Y + self.imageheight, fill = bgcolor, tags = self.cards[0].getTags() + 'line')
					canvas.create_line(self.drawcardX, self.Y, self.drawcardX + self.imagewidth, self.Y, fill = bgcolor, tags = self.cards[0].getTags() + 'line')
					canvas.create_line(self.drawcardX + self.imagewidth, self.Y, self.drawcardX + self.imagewidth, self.Y + self.imageheight, fill = bgcolor, tags = self.cards[0].getTags() + 'line')
					canvas.create_line(self.drawcardX, self.Y + self.imageheight, self.drawcardX + self.imagewidth, self.Y + self.imageheight, fill = bgcolor, tags = self.cards[0].getTags() + 'line')

		# 捨て札
		if len(self.tosscards) > 0:
			if self.tosscards[-1].getTags() in hidetags:
				self.tosscards[-1].setState(2)
				self.tosscards.pop(-1)

			if len(self.tosscards) > 0:
				canvas.create_image(self.tossX, self.Y, image = self.tosscards[-1].getImage(), anchor = tk.NW, tags = self.tosscards[-1].getTags())
				canvas.create_line(self.tossX, self.Y, self.tossX, self.Y + self.imageheight, fill = bgcolor, tags = self.tosscards[-1].getTags() + 'line')
				canvas.create_line(self.tossX, self.Y, self.tossX + self.imagewidth, self.Y, fill = bgcolor, tags = self.tosscards[-1].getTags() + 'line')
				canvas.create_line(self.tossX + self.imagewidth, self.Y, self.tossX + self.imagewidth, self.Y + self.imageheight, fill = bgcolor, tags = self.tosscards[-1].getTags() + 'line')
				canvas.create_line(self.tossX, self.Y + self.imageheight, self.tossX + self.imagewidth, self.Y + self.imageheight, fill = bgcolor, tags = self.tosscards[-1].getTags() + 'line')