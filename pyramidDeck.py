import tkinter as tk

class PyramidDeck():

	def __init__(self, imagewidth, imageheight, gwidth, gheight):
		self.cards = []
		self.imagewidth = imagewidth
		self.imageheight = imageheight
		self.gwidth = gwidth
		self.gheight = gheight

		self.infos = []
		self.startX = self.gwidth // 2 - self.imagewidth // 2
		self.startY = 30
		self.imagewidthhalf = self.imagewidth // 2
		self.imageheighthalf = self.imageheight // 2
		self.margin = 3
		# index 0=x座標, 1=y座標, 2=ペア1, 3=ペア2
		self.infos.append([self.startX, self.startY, 1, 2])
		self.infos.append([self.infos[0][0] - self.imagewidthhalf - self.margin, self.infos[0][1] + self.imageheighthalf, 3, 4])
		self.infos.append([self.infos[0][0] + self.imagewidthhalf + self.margin, self.infos[1][1], 4, 5])
		self.infos.append([self.infos[1][0] - self.imagewidthhalf - self.margin, self.infos[1][1] + self.imageheighthalf, 6, 7])
		self.infos.append([self.infos[3][0] + self.imagewidth + self.margin * 2, self.infos[3][1], 7, 8])
		self.infos.append([self.infos[4][0] + self.imagewidth + self.margin * 2, self.infos[3][1], 8, 9])
		self.infos.append([self.infos[3][0] - self.imagewidthhalf - self.margin, self.infos[3][1] + self.imageheighthalf, 10, 11])
		self.infos.append([self.infos[6][0] + self.imagewidth + self.margin * 2, self.infos[6][1], 11, 12])
		self.infos.append([self.infos[7][0] + self.imagewidth + self.margin * 2, self.infos[6][1], 12, 13])
		self.infos.append([self.infos[8][0] + self.imagewidth + self.margin * 2, self.infos[6][1], 13, 14])
		self.infos.append([self.infos[6][0] - self.imagewidthhalf - self.margin, self.infos[6][1] + self.imageheighthalf, 15, 16])
		self.infos.append([self.infos[10][0] + self.imagewidth + self.margin * 2, self.infos[10][1], 16, 17])
		self.infos.append([self.infos[11][0] + self.imagewidth + self.margin * 2, self.infos[10][1], 17, 18])
		self.infos.append([self.infos[12][0] + self.imagewidth + self.margin * 2, self.infos[10][1], 18, 19])
		self.infos.append([self.infos[13][0] + self.imagewidth + self.margin * 2, self.infos[10][1], 19, 20])
		self.infos.append([self.infos[10][0] - self.imagewidthhalf - self.margin, self.infos[10][1] + self.imageheighthalf, 21, 22])
		self.infos.append([self.infos[15][0] + self.imagewidth + self.margin * 2, self.infos[15][1], 22, 23])
		self.infos.append([self.infos[16][0] + self.imagewidth + self.margin * 2, self.infos[15][1], 23, 24])
		self.infos.append([self.infos[17][0] + self.imagewidth + self.margin * 2, self.infos[15][1], 24, 25])
		self.infos.append([self.infos[18][0] + self.imagewidth + self.margin * 2, self.infos[15][1], 25, 26])
		self.infos.append([self.infos[19][0] + self.imagewidth + self.margin * 2, self.infos[15][1], 26, 27])
		self.infos.append([self.infos[15][0] - self.imagewidthhalf - self.margin, self.infos[15][1] + self.imageheighthalf, 28, 28])
		self.infos.append([self.infos[21][0] + self.imagewidth + self.margin * 2, self.infos[21][1], 28, 28])
		self.infos.append([self.infos[22][0] + self.imagewidth + self.margin * 2, self.infos[21][1], 28, 28])
		self.infos.append([self.infos[23][0] + self.imagewidth + self.margin * 2, self.infos[21][1], 28, 28])
		self.infos.append([self.infos[24][0] + self.imagewidth + self.margin * 2, self.infos[21][1], 28, 28])
		self.infos.append([self.infos[25][0] + self.imagewidth + self.margin * 2, self.infos[21][1], 28, 28])
		self.infos.append([self.infos[26][0] + self.imagewidth + self.margin * 2, self.infos[21][1], 28, 28])

	def addCard(self, card):
		self.cards.append(card)

	def getCards(self):
		return self.cards

	def gameComplete(self):
		count = 0
		for card in self.cards:
			if card.getState() == 2:
				count += 1

		if len(self.cards) == count:
			return True

		return False

	def paint(self, canvas, bgcolor, hidetags):
		for card in self.cards:
			if card.getTags() in hidetags:
				card.setState(2)

		i = 0
		for card in self.cards:
			if card.getState() == 2:
				i += 1
				continue
				
			if i <= 20:
				if self.cards[self.infos[i][2]].getState() == 2 and self.cards[self.infos[i][3]].getState() == 2:
					card.setState(1)

			if i >= 21:
				card.setState(1)

			if card.getState() == 0:
				canvas.create_rectangle(self.infos[i][0], self.infos[i][1], self.infos[i][0] + self.imagewidth, self.infos[i][1] + self.imageheight, fill = 'firebrick', outline = 'black', width = 1)
			elif card.getState() == 1:
				canvas.create_image(self.infos[i][0], self.infos[i][1], image = card.getImage(), anchor = tk.NW, tags = card.getTags())
				canvas.create_line(self.infos[i][0], self.infos[i][1], self.infos[i][0], self.infos[i][1] + self.imageheight, fill = bgcolor, tags = card.getTags() + 'line')
				canvas.create_line(self.infos[i][0], self.infos[i][1], self.infos[i][0] + self.imagewidth, self.infos[i][1], fill = bgcolor, tags = card.getTags() + 'line')
				canvas.create_line(self.infos[i][0] + self.imagewidth, self.infos[i][1], self.infos[i][0] + self.imagewidth, self.infos[i][1] + self.imageheight, fill = bgcolor, tags = card.getTags() + 'line')
				canvas.create_line(self.infos[i][0], self.infos[i][1] + self.imageheight, self.infos[i][0] + self.imagewidth, self.infos[i][1] + self.imageheight, fill = bgcolor, tags = card.getTags() + 'line')
			i += 1