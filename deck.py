import random
from decimal import Decimal, ROUND_HALF_UP
from PIL import Image, ImageTk

class Deck():

	def __init__(self):
		self.cards = []
		self.suits = ['diamond', 'club', 'heart', 'spade']
		self.reduction_ratio = 10  #縮小率
		self.imagewidth = int(Decimal(str(712 / self.reduction_ratio)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
		self.imageheight = int(Decimal(str(1008 / self.reduction_ratio)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

		import card
		for suit in self.suits:
			for num in range(1, 14):
				img=ImageTk.PhotoImage(Image.open('images/' + suit + '/' + str(num) + '.png').convert('RGB').resize(size=(self.imagewidth, self.imageheight)))

				obj = card.Card(
					suit = suit,
					num = num,
					state = 0,
					image = img
				)
				self.cards.append(obj)

	def shuffleCards(self):
		random.shuffle(self.cards)
		