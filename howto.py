import tkinter as tk
import main

class Howto(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 640
		self.HEIGHT = 360
		self.bgcolor = 'forestgreen'
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		self.pack_propagate(0)

		tk.Label(self, text = '遊びかた', bg = self.bgcolor, font = ('Arial', 32)).pack(pady = 30)

		tk.Button(self, text = 'メニューに戻る', bg = self.bgcolor, highlightbackground = self.bgcolor, command = lambda: main.show_frame('メニューフレーム')).place(x = 35, y = 35)

		self.howtotext = 	'ピラミッド内の表向きのカードどうし\n' \
							'もしくは\n' \
							'ピラミッド内の表向きのカードと\n' \
							'手札か捨て札の1番上のカードの\n' \
							'1枚もしくは2枚の数字の合計が13になれば捨てる\n' \
							'ジョーカーはどれと組み合わせても捨てられる\n\n' \
							'最終的にピラミッドのカードがなくなれば成功'

		tk.Label(self, text = self.howtotext, bg = self.bgcolor, font = ('Arial', 20), fg = 'white').pack()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT