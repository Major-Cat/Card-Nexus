import cards
from ursina import *

l = cards.Deck() # cards.deck here will be replaced with the object that is the deck in poker.py (this is temporary)

app = Ursina()
window.fps_counter.enabled = False

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



def chip_reset(chip,dest_chip):
	dest = dest_chip.world_position
	if not chip.world_position == dest:
		chip.animate_position((dest),duration=1,curve=curve.linear)

def chip_vis(chip):
	if chip.visible == False:
		chip.visible = True
	else:
		chip.visible = False

def Win(centre,winner,*bets)
		

def Bet(bet_chips, centre):
	chip_reset(bet_chips,centre)
	if bet_chips.world_position == centre.world_position:
		centre.visible = True
		bet_chips.visible = False


table = Entity(parent=scene,model="circle",position=(0,0,0),scale=(11,5.5),color=color.color(80,1,0.4))
table_edge = Entity(parent=scene,model="circle",position=(0,0,1),scale=(12,6),color=color.color(20,1,0.4))

player1_chips = Entity(parent=scene,model="quad",position=(-1,-2,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png")
player2_chips = duplicate(player1_chips,position=(1,2,-0.1))

player1_bet_chips = Entity(parent=scene,model="quad",position=(-1,-2,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png")
player2_bet_chips= duplicate(player1_bet_chips,position=(1,2,-0.1))

centre_chips = Entity(parent=scene,model="quad",position=(0,0,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png",visible=False)

Bet_button = my_button(message="Bet",x=-3,y=-3)
Bet_button.on_click =lambda: Bet(player1_bet_chips,centre_chips)
Win_button = my_button(message="Win",x=-5,y=-3)
Win_button.on_click =lambda: chip_reset(player1_bet_chips,player1_chips)

Bet2_button = my_button(message="enemy Bet",x=-3,y=3)
Bet2_button.on_click =lambda: Bet(player2_bet_chips,centre_chips)
Win2_button = my_button(message="enemy Win",x=-5,y=3)
Win2_button.on_click =lambda: chip_reset(player2_bet_chips,player2_chips)


#disable_button = my_button(message="invis_bet",x=-3,y=3)
#disable_button.on_click =lambda: chip_vis(player1_bet_chips)
#disable_button = my_button(message="invis_centre",x=0,y=3)
#disable_button.on_click =lambda: chip_vis(centre_chips)
#reset_button = my_button(message="reset",x=-6,y=3)
#reset_button.on_click = lambda: chip_reset(player1_bet_chips,player1_chips)

#def update():
#	pos.text = f"hello {test_chip_move.world_position}"
#	pos2.text = f"hi {test_chip_move.x}"

app.run()
