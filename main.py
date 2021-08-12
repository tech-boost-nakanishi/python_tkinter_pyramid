import tkinter as tk
import menu
import howto
import game

WIDTH = HEIGHT = 0

root = tk.Tk()
root.title('ピラミッド')
root.resizable(False, False)

container = tk.Frame(root)
container.pack()

menuframe = howtoframe = gameframe = tk.Frame(root)

def show_frame(targetFrame):
	global WIDTH, HEIGHT, menuframe, howtoframe, gameframe

	for frame in (menuframe, howtoframe, gameframe):
		frame.destroy()

	if targetFrame == 'メニューフレーム':
		menuframe = menu.Menu(container, root)
		menuframe.pack()
		WIDTH = menuframe.getWidth()
		HEIGHT = menuframe.getHeight()

	elif targetFrame == 'あそびかたフレーム':
		howtoframe = howto.Howto(container, root)
		howtoframe.pack()
		WIDTH = howtoframe.getWidth()
		HEIGHT = howtoframe.getHeight()

	elif targetFrame == 'ゲームフレーム':
		gameframe = game.Game(container, root)
		gameframe.pack()
		WIDTH = gameframe.getWidth()
		HEIGHT = gameframe.getHeight()

	root.update_idletasks()
	x = (root.winfo_screenwidth() // 2) - (WIDTH // 2)
	y = (root.winfo_screenheight() // 2) - (HEIGHT // 2)
	root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))

def launch():
	root.mainloop()

show_frame('メニューフレーム')