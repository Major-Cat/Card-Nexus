import cards
from ursina import *
Debug = True
l = cards.Deck() # cards.deck here will be replaced with the object that is the deck in poker.py (this is temporary)

app = Ursina() # FSR: I think this is causing the errors (multiple showcase exception) so remember to remove later.
window.fps_counter.enabled = False

class my_button(Button):
	def __init__(self,x=3.5,y=0,message="",scale = (2,0.5),visible=True):
		super().__init__(parent = scene, text = message, color = color.light_gray, texture = "white_cube", highlight_color = color.white, pressed_color = color.dark_gray, position = (x,y), scale = scale,visible=visible)

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
		
class pot():
	def __init__(self,bet=0,total=0):
		self.bet = bet
		self.total = total

class Hand():
	def __init__(self,Cards=[]):
		self.Cards = Cards
		self.Cards.append(l.draw())
		self.Cards.append(l.draw())

def call(money,pot):
	change = pot.bet - money.bet
	money.money -= change

class money():
	def __init__(self,money=100,bet=0):
		self.money = money
		self.bet = bet

	def Bet(self,pot):
		if self.bet == pot.bet:	
			pass # check/bet/fold
		elif self.bet < pot.bet:
			pass # call/raise/fold

class player():
	def __init__(self,money,Hand,human=False):
		self.money = money
		self.Hand = Hand
		self.human = human

class Central():
	def __init__(self,pot,Community_Cards):
		self.pot = pot
		self.Com_Cards = Community_Cards

def Win(centre,winner_bet,winner,bets): # FSR: Animation functions should have a name that makes it obvious that they just do animations.
	centre.visible = False
	for i in bets:
		if i[1] == winner_bet:
			i[1].visible = True
			i[1].animate_position((centre.world_position),duration=0,curve=curve.linear)
			i[1].animate_position((i[0]),duration=1,curve=curve.linear)
	bets = []

def change_vis(chip,vis=False): # FSR: Animation functions should have a name that makes it obvious that they just do animations.
	if vis == False:
		chip.visible = False
	else:
		chip.visible = True

def Bet(bet_chip,centre,bets): # FSR: Animation functions should have a name that makes it obvious that they just do animations.
	initial_pos = bet_chip.world_position
	bets.append([bet_chip.world_position,bet_chip])
	s = Sequence(Func(bet_chip.animate_position,duration=1,value=centre.world_position,curve=curve.linear), 1,Func(change_vis,chip=bet_chip),Func(change_vis,chip=centre,vis=True),Func(bet_chip.animate_position,duration=1,value=initial_pos,curve=curve.linear),1,Func(change_vis,chip=bet_chip,vis=True))
	s.start()

global bets
bets = []
Central = Central(pot(),Community_Cards())

table = Entity(parent=scene,model="circle",position=(0,0,0),scale=(11,5.5),color=color.color(100,1,0.4))
table_edge = Entity(parent=scene,model="circle",position=(0,0,1),scale=(12,6),color=color.color(20,1,0.4))

Player1 = player(money(),Hand(),True)
Player2 = player(money(),Hand())
Player3 = player(money(),Hand())
Player4 = player(money(),Hand())
Player5 = player(money(),Hand())
Player6 = player(money(),Hand())
Player7 = player(money(),Hand())
Player8 = player(money(),Hand())

centre_chips = Entity(parent=scene,model="quad",position=(0,0,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png",visible=False)

player1_chips = Entity(parent=scene,model="quad",position=(-1,-2,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png")
player2_chips = duplicate(player1_chips,position=(-4,-1,-0.1))
player3_chips = duplicate(player1_chips,position=(-4,1,-0.1))
player4_chips = duplicate(player1_chips,position=(-2,2,-0.1))
player5_chips = duplicate(player1_chips,position=(1,2,-0.1))
player6_chips = duplicate(player1_chips,position=(4,1,-0.1))
player7_chips = duplicate(player1_chips,position=(4,-1,-0.1))
player8_chips = duplicate(player1_chips,position=(2,-2,-0.1))

player1_bet_chips = Entity(parent=scene,model="quad",position=(-1,-2,-0.1),scale=(0.6,0.4),texture="Cards/Other pngs/chip.png")
player2_bet_chips = duplicate(player1_bet_chips,position=(-4,-1,-0.1))
player3_bet_chips = duplicate(player1_bet_chips,position=(-4,1,-0.1))
player4_bet_chips = duplicate(player1_bet_chips,position=(-2,2,-0.1))
player5_bet_chips = duplicate(player1_bet_chips,position=(1,2,-0.1))
player6_bet_chips = duplicate(player1_bet_chips,position=(4,1,-0.1))
player7_bet_chips = duplicate(player1_bet_chips,position=(4,-1,-0.1))
player8_bet_chips = duplicate(player1_bet_chips,position=(2,-2,-0.1))

#if Debug == False:

Fold_Button = my_button(message="Fold",x=-2,y=-3.5,scale=(1.5,0.65))
Call_Button = my_button(message="Call/Check",x=-6,y=-3.5,scale=(2.5,0.65))
Raise_Button = my_button(message="Raise",x=-3.75,y=-3.5,scale=(1.5,0.65))
#Debug = False

if Debug == True:
	Bet_button = my_button(message="Bet",x=-1,y=-3,scale=(1,0.25))
	Bet_button.on_click = lambda: Bet(player1_bet_chips,centre_chips,bets)
	Win_button = my_button(message="Win",x=-2,y=-3,scale=(1,0.25))
	Win_button.on_click = lambda: Win(centre_chips,player1_bet_chips,player1_chips,bets)

	Bet2_button = my_button(message="p2Bet",x=-5,y=-3,scale=(1,0.25))
	Bet2_button.on_click = lambda: Bet(player2_bet_chips,centre_chips,bets)
	Win2_button = my_button(message="p2Win",x=-5,y=-2.5,scale=(1,0.25))
	Win2_button.on_click = lambda: Win(centre_chips,player2_bet_chips,player2_chips,bets)

	Bet3_button = my_button(message="p3Bet",x=-6,y=0.5,scale=(1,0.25))
	Bet3_button.on_click =lambda: Bet(player3_bet_chips,centre_chips,bets)
	Win3_button = my_button(message="p3Win",x=-6,y=1,scale=(1,0.25))
	Win3_button.on_click =lambda: Win(centre_chips,player3_bet_chips,player3_chips,bets)

	Bet4_button = my_button(message="p4Bet",x=-2,y=3,scale=(1,0.25))
	Bet4_button.on_click =lambda: Bet(player4_bet_chips,centre_chips,bets)
	Win4_button = my_button(message="p4Win",x=-2,y=3.5,scale=(1,0.25))
	Win4_button.on_click =lambda: Win(centre_chips,player4_bet_chips,player4_chips,bets)

	Bet5_button = my_button(message="p5Bet",x=2,y=3,scale=(1,0.25))
	Bet5_button.on_click =lambda: Bet(player5_bet_chips,centre_chips,bets)
	Win5_button = my_button(message="p5Win",x=2,y=3.5,scale=(1,0.25))
	Win5_button.on_click =lambda: Win(centre_chips,player5_bet_chips,player5_chips,bets)

	Bet6_button = my_button(message="p6Bet",x=6,y=1,scale=(1,0.25))
	Bet6_button.on_click =lambda: Bet(player6_bet_chips,centre_chips,bets)
	Win6_button = my_button(message="p6Win",x=6,y=1.5,scale=(1,0.25))
	Win6_button.on_click =lambda: Win(centre_chips,player6_bet_chips,player6_chips,bets)

	Bet7_button = my_button(message="p7Bet",x=6,y=-1.5,scale=(1,0.25))
	Bet7_button.on_click =lambda: Bet(player7_bet_chips,centre_chips,bets)
	Win7_button = my_button(message="p7Win",x=6,y=-1,scale=(1,0.25))
	Win7_button.on_click =lambda: Win(centre_chips,player7_bet_chips,player7_chips,bets)

	Bet8_button = my_button(message="p8Bet",x=3,y=-3.5,scale=(1,0.25))
	Bet8_button.on_click =lambda: Bet(player8_bet_chips,centre_chips,bets)
	Win8_button = my_button(message="p8Win",x=3,y=-3,scale=(1,0.25))
	Win8_button.on_click =lambda: Win(centre_chips,player8_bet_chips,player8_chips,bets)

P1_money = Text(text=f"p1 money:{Player1.money.money}",scale = 15,parent = scene, origin=(-1,9),color = Color(0,0,0,0.8))

def update():
	P1_money.text = f"p1 money:{Player1.money.money}"


app.run()
