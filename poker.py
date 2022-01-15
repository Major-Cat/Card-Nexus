import cards
from ursina import *

l = cards.Deck() # cards.deck here will be replaced with the object that is the deck in poker.py (this is temporary)

class my_button(Button):
	def __init__(self,x=3.5,y=0,message="",width = 2):
		super().__init__(parent = scene, text = message, color = color.light_gray, texture = "white_cube", highlight_color = color.white, pressed_color = color.dark_gray, position = (x,y), scale = (width,0.5))

class Community_Cards():
	def __init__(self,Cards=[]):
		self.Cards=Cards
		
class Hand():
	def __init__(self,Cards=[]):
		self.Cards = Cards
		self.Cards.append(l.draw())
		self.Cards.append(l.draw())



app = Ursina()
window.fps_counter.enabled = False

def run():
	print(Hand().Cards)
	table = Entity(parent=scene,model="circle",position=(0,0,0),scale=(11,5.5),color=color.color(80,1,0.4))
	table_edge = Entity(parent=scene,model="circle",position=(0,0,1),scale=(12,6),color=color.color(20,1,0.4))
	test_chip = Entity(parent=scene,model="quad",position=(4,1,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png")
	test_chip_move = Entity(parent=scene,model="quad",position=(4,1,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png")
	test_chip_move.animate_position((0,0),duration=1,curve=curve.linear)
	

	app.run()


run()