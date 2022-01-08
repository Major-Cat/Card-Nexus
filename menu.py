from ursina import *
import json

class usable_button(Button):
	def __init__(self,x=0,y=0,message="",width = 2,command=0):
		super().__init__(
			parent = scene,
			text = message,
			color = color.light_gray,
			texture = "white_cube",
			highlight_color = color.white,
			pressed_color = color.dark_gray,
			position = (x,y,),
			scale = (width,0.5)
			)

def run(app):
	Text.size = 0.02
	Text.default_resolution = 1080 * 0.05#


	close = usable_button(message="quit",x=3)
	close.on_click = application.quit
	play = usable_button(message="new game",x=-3)

	load = usable_button(message="load game")

	poker_background = Entity(parent=scene,model="quad",position=(0,1.6,0.1),scale=(5,1),texture = "white_cube")
	poker = Text(text="Ewan's Poker",scale = 15,parent = scene, origin=(0,-5), background=False,color = Color(0,0,0,0.8))

