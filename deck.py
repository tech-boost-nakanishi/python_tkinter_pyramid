import tkinter as tk
import random
from PIL import Image, ImageTk

class Deck():

	def __init__(self, imagewidth, imageheight):
		self.cards = []
		self.suits = ['diamond', 'club', 'heart', 'spade']
		self.imagewidth = imagewidth
		self.imageheight = imageheight

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

	def shuffleCards(self):
		random.shuffle(self.cards)

	# def paint(self, canvas, cardslist, bgcolor):
		# canvas.create_image(50, 50, image = cardslist[0].getImage(), anchor = tk.NW, tags = cardslist[0].getTags())
		# canvas.create_line(50, 50, 50, 50 + self.imageheight, fill = bgcolor, tags = cardslist[0].getTags() + 'line')
		# canvas.create_line(50, 50, 50 + self.imagewidth, 50, fill = bgcolor, tags = cardslist[0].getTags() + 'line')
		# canvas.create_line(50 + self.imagewidth, 50, 50 + self.imagewidth, 50 + self.imageheight, fill = bgcolor, tags = cardslist[0].getTags() + 'line')
		# canvas.create_line(50, 50 + self.imageheight, 50 + self.imagewidth, 50 + self.imageheight, fill = bgcolor, tags = cardslist[0].getTags() + 'line')

		# canvas.create_image(350, 350, image = cardslist[1].getImage(), anchor = tk.NW, tags = cardslist[1].getTags())
		# canvas.create_line(350, 350, 350, 350 + self.imageheight, fill = bgcolor, tags = cardslist[1].getTags() + 'line')
		# canvas.create_line(350, 350, 350 + self.imagewidth, 350, fill = bgcolor, tags = cardslist[1].getTags() + 'line')
		# canvas.create_line(350 + self.imagewidth, 350, 350 + self.imagewidth, 350 + self.imageheight, fill = bgcolor, tags = cardslist[1].getTags() + 'line')
		# canvas.create_line(350, 350 + self.imageheight, 350 + self.imagewidth, 350 + self.imageheight, fill = bgcolor, tags = cardslist[1].getTags() + 'line')
		