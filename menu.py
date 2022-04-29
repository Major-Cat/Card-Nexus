from ursina import *	#graphics engine

class my_button(Button):	# The button I will use instead of the default
	def __init__(self,x=0,y=0,message="",width = 2):
		super().__init__(parent = scene, text = message, color = color.light_gray, texture = "white_cube", highlight_color = color.white, pressed_color = color.dark_gray, position = (x,y), scale = (width,0.5))

def run(app):	#function called by main.py to call this file
	def new_game():		#start new game
		scene.clear()	#removes all items (button and stuff) from the app
		import poker	#this crashes the app

	def load_game():	#load a saved game
		scene.clear()
		import poker	#this crashes the app

	Text.size = 0.02
	Text.default_resolution = 1080 * 0.05#


	close = my_button(message="quit",x=3)
	close.on_click = application.quit
	play = my_button(message="new game",x=-3)
	play.on_click = new_game
	load = my_button(message="load game")
	load.on_click = load_game

	title_background = Entity(parent=scene,model="quad",position=(0,1.6,0.1),scale=(5,1),texture = "white_cube")
	title = Text(text="Ewan's Poker",scale = 15,parent = scene, origin=(0,-5), background=False,color = Color(0,0,0,0.8))

