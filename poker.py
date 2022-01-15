import cards
from ursina import *

l = cards.Deck() # cards.deck here will be replaced with the object that is the deck in poker.py (this is temporary)

class my_button(Button):
	def __init__(self,x=3.5,y=0,message="",width = 2):
		super().__init__(parent = scene, text = message, color = color.light_gray, texture = "white_cube", highlight_color = color.white, pressed_color = color.dark_gray, position = (x,y), scale = (width,0.5))

class Community_Cards():
	def __init__(self,Cards=[]):
		self.Cards=Cards

	def draw(self):
		if len(self.Cards) == 0:
			self.Cards.append(l.draw())
			self.Cards.append(l.draw())
			self.Cards.append(l.draw())
		elif len(self.Cards) == 3 or len(self.Cards) == 4:
			self.Cards.append(l.draw())
		
class Hand():
	def __init__(self,Cards=[]):
		self.Cards = Cards
		self.Cards.append(l.draw())
		self.Cards.append(l.draw())



app = Ursina()
window.fps_counter.enabled = False

#table = Entity(parent=scene,model="circle",position=(0,0,0),scale=(11,5.5),color=color.color(80,1,0.4))
#table_edge = Entity(parent=scene,model="circle",position=(0,0,1),scale=(12,6),color=color.color(20,1,0.4))
test_chip = Entity(parent=scene,model="quad",position=(4,1,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png")

test_chip_move = Entity(parent=scene,model="quad",position=(4,1,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png")
test_chip_move.animate_position((0,0),duration=1,curve=curve.linear)

pos = Text(text=f"hello {test_chip_move.world_position}",scale = 10,parent = scene, origin=(1,2))
pos2 = Text(text=f"hi {test_chip_move.x}",scale = 10,parent = scene, origin=(1,1))

test_button = my_button(message="disable",x=0,y=2)
test_button.on_click = test_chip_move.disable

def update():
	#pos = Text(text=f"hello {test_chip_move.world_position}",scale = 10,parent = scene, origin=(1,2,-1))
	pos.text = f"hello {test_chip_move.world_position}"
	pos2.text = f"hi {test_chip_move.x}"

app.run()
