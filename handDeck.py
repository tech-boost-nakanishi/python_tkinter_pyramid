import tkinter as tk
import threading
import time

class HandDeck():

	def __init__(self, imagewidth, imageheight, gwidth, gheight):
		self.cards = []
		self.tosscards = []
		self.cardPressed = False
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

		self.cardPressed = True

	def getCards(self):
		return self.cards

	def getTossCards(self):
		return self.tosscards

	def handCardAnim(self, canvas):
		if self.cards[0].getState() == 2:
			return

		canvas.create_image(self.handcardsX, self.Y, image = self.cards[0].getImage(), anchor = tk.NW, tags = self.cards[0].getTags())
		splitcount = 5
		x = (self.handcardsX - self.drawcardX) / splitcount
		for i in range(splitcount):
			canvas.move(self.cards[0].getTags(), -x, 0)
			time.sleep(0.1)

	def tossCardAnim(self, canvas):
		if self.tosscards[-1].getState() == 2:
			return

		canvas.create_image(self.drawcardX, self.Y, image = self.tosscards[-1].getImage(), anchor = tk.NW, tags = self.tosscards[-1].getTags())
		splitcount = 5
		x = (self.drawcardX - self.tossX) / splitcount
		for i in range(splitcount):
			canvas.move(self.tosscards[-1].getTags(), -x, 0)
			time.sleep(0.1)

	def paint(self, canvas, bgcolor, hidetags):
		handcardthread = threading.Thread(target=self.handCardAnim, args=(canvas,))
		tosscardthread = threading.Thread(target=self.tossCardAnim, args=(canvas,))
		handcardthread.setDaemon(True)
		tosscardthread.setDaemon(True)

		if self.cardPressed == True and len(self.cards) > 0 and handcardthread.is_alive() == False:
			handcardthread.start()

		if self.cardPressed == True and self.getDrawCount() > 1 and tosscardthread.is_alive() == False:
			tosscardthread.start()

		# 残りのカード
		if len(self.cards) > 1:
			canvas.create_rectangle(self.handcardsX, self.Y, self.handcardsX + self.imagewidth, self.Y + self.imageheight, fill = 'firebrick', outline = 'black', width = 1, tags = 'handcards')

		# 引かれたカード
		if self.cards[0].getTags() in hidetags:
			self.cards[0].setState(2)
		else:
			if self.getDrawCount() > 0:
				if len(self.cards) > 0:
					if handcardthread.is_alive() == False:
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
				if len(self.tosscards) > 1:
					canvas.create_image(self.tossX, self.Y, image = self.tosscards[-2].getImage(), anchor = tk.NW, tags = self.tosscards[-2].getTags())
				if tosscardthread.is_alive() == False:
					canvas.create_image(self.tossX, self.Y, image = self.tosscards[-1].getImage(), anchor = tk.NW, tags = self.tosscards[-1].getTags())
				canvas.create_line(self.tossX, self.Y, self.tossX, self.Y + self.imageheight, fill = bgcolor, tags = self.tosscards[-1].getTags() + 'line')
				canvas.create_line(self.tossX, self.Y, self.tossX + self.imagewidth, self.Y, fill = bgcolor, tags = self.tosscards[-1].getTags() + 'line')
				canvas.create_line(self.tossX + self.imagewidth, self.Y, self.tossX + self.imagewidth, self.Y + self.imageheight, fill = bgcolor, tags = self.tosscards[-1].getTags() + 'line')
				canvas.create_line(self.tossX, self.Y + self.imageheight, self.tossX + self.imagewidth, self.Y + self.imageheight, fill = bgcolor, tags = self.tosscards[-1].getTags() + 'line')

		self.cardPressed = False