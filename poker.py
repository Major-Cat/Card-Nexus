import cards
from ursina import *
Debug = True
l = cards.Deck() # cards.deck here will be replaced with the object that is the deck in poker.py (this is temporary)

app = Ursina() # FSR: I think this is causing the errors (multiple showcase exception) so remember to remove later.
window.fps_counter.enabled = False

class my_button(Button):
	def __init__(self,x=3.5,y=0,message="",scale = (2,0.5),enabled=True):
		super().__init__(parent = scene, text = message, color = color.light_gray, texture = "white_cube", highlight_color = color.white, pressed_color = color.dark_gray, position = (x,y), scale = scale,enabled=enabled)

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
	def __init__(self):
		self.Cards = []
		self.Cards.append(l.draw())
		self.Cards.append(l.draw())

#def call(money,pot):
#	change = pot.bet - money.bet
#	money.money -= change

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
	def __init__(self,money,hand,human=False):
		self.money = money
		self.hand = hand
		self.human = human

class Central():
	def __init__(self,pot,Community_Cards):
		self.pot = pot
		self.Com_Cards = Community_Cards

def Win(centre,winner_bet,winner,bets,player):
	centre.visible = False
	for i in bets:
		if i[1] == winner_bet:
			i[1].visible = True
			i[1].animate_position((centre.world_position),duration=0,curve=curve.linear)
			i[1].animate_position((i[0]),duration=1,curve=curve.linear)
	bets = []

def change_vis(entity,vis=False):
	if vis == False:
		entity.visible = False
	else:
		entity.visible = True

def change_enable(*entities):
	for i in entities:
		if i.enabled == False:
			i.enabled = True
		else:
			i.enabled = False

def Bet(bet_chip,centre,bets,player,amount,call=False): 
	initial_pos = bet_chip.world_position
	bets.append([bet_chip.world_position,bet_chip])
	s = Sequence(Func(bet_chip.animate_position,duration=1,value=centre.world_position,curve=curve.linear), 1,Func(change_vis,entity=bet_chip),Func(change_vis,entity=centre,vis=True),Func(bet_chip.animate_position,duration=1,value=initial_pos,curve=curve.linear),1,Func(change_vis,entity=bet_chip,vis=True))
	s.start()
	if amount < player.money.money:
		player.money.bet += amount
		player.money.money -= amount
		central.pot.bet = amount
		central.pot.total += amount
	else:
		amount = player.money.money
		player.money.bet += amount
		player.money.money -= amount
		central.pot.bet = amount
		central.pot.total += amount

	global call_amount
	call_amount = central.pot.bet - player.money.bet
	if call_amount < 0:
		call_amount = 0

def Final_Button_func(bet_chip,centre,bets,player,bet_slider,Final_Button):
	Bet(bet_chip,centre,bets,player,bet_slider.value)
	bet_slider.max = player.money.money
	bet_slider.value = bet_slider.min
	change_enable(bet_slider,Final_Button)

bets = []
central = Central(pot(),Community_Cards())
central.pot.bet = 10	#testing
central.pot.total = 10	#testing

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

player1_card1 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.5,0.005,0.7),position=(-0.5,-3,-0.5),rotation=(270,0,0))
player1_card2 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.5,0.005,0.7),position=(0.55,-3,-0.5),rotation=(270,0,0))

player2_card1 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(-5,-1.6,-0.4),rotation=(325,90,270))
player2_card2 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(-5.4,-0.8,-0.4),rotation=(325,90,270))

player3_card1 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(-5.3,0.9,-0.4),rotation=(10,90,270))
player3_card2 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(-5.2,1.8,-0.4),rotation=(10,90,270))

player4_card1 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(-2.75,3,-0.4),rotation=(60,90,270))
player4_card2 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(-1.9,3.3,-0.4),rotation=(60,90,270))

player5_card1 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(0.55,3,-0.4),rotation=(100,90,270))
player5_card2 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(1.4,2.8,-0.4),rotation=(100,90,270))

player6_card1 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(4.2,2.2,-0.4),rotation=(130,90,270))
player6_card2 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(4.9,1.6,-0.4),rotation=(130,90,270))

player7_card1 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(5.5,-0.5,-0.4),rotation=(170,90,270))
player7_card2 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(5.5,-1.4,-0.4),rotation=(170,90,270))

player8_card1 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(3.05,-2.45,-0.4),rotation=(225,90,270))
player8_card2 = Entity(parent=scene,model="Cards/Other pngs/block.obj",texture="Cards/Front pngs/s_a.png",scale=(0.4,0.005,0.56),position=(2.4,-3,-0.4),rotation=(225,90,270))

card_models = [player1_card1, player1_card2, player2_card1, player2_card2, player3_card1, player3_card2, player4_card1, player4_card2, player5_card1, player5_card2, player6_card1, player6_card2, player7_card1, player7_card2, player8_card1, player8_card2]

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

Fold_Button = my_button(message="Fold",x=-2,y=-3.5,scale=(1.5,0.65))

call_amount = central.pot.bet - Player1.money.bet
Call_Button = my_button(message="Call/Check",x=-6,y=-3.5,scale=(2.5,0.65))
Call_Button.on_click = lambda: Bet(player1_bet_chips,centre_chips,bets,Player1,call_amount,True)

bet_slider = Slider(x=-.7,y=-.35,enabled=False,min = call_amount + 1, max = Player1.money.money,step=1)
Final_Button = my_button(message="confirm",x=-5.5,y=-2,scale=(1.5,0.65),enabled=False)
Raise_Button = my_button(message="Raise",x=-3.75,y=-3.5,scale=(1.5,0.65))
Raise_Button.on_click = lambda: change_enable(bet_slider,Final_Button)
Final_Button.on_click = lambda: Final_Button_func(player1_bet_chips,centre_chips,bets,Player1,bet_slider,Final_Button)

Debug = False

if Debug == True: # Debug mode doesn't work anymore, Bet() missing 'amount' argument.
	Bet_button = my_button(message="Bet",x=-1,y=-3,scale=(1,0.25))
	Bet_button.on_click = lambda: Bet(player1_bet_chips,centre_chips,bets,Player1)
	Win_button = my_button(message="Win",x=-2,y=-3,scale=(1,0.25))
	Win_button.on_click = lambda: Win(centre_chips,player1_bet_chips,player1_chips,bets,Player1)

	Bet2_button = my_button(message="p2Bet",x=-5,y=-3,scale=(1,0.25))
	Bet2_button.on_click = lambda: Bet(player2_bet_chips,centre_chips,bets,Player2)
	Win2_button = my_button(message="p2Win",x=-5,y=-2.5,scale=(1,0.25))
	Win2_button.on_click = lambda: Win(centre_chips,player2_bet_chips,player2_chips,bets,Player2)

	Bet3_button = my_button(message="p3Bet",x=-6,y=0.5,scale=(1,0.25))
	Bet3_button.on_click =lambda: Bet(player3_bet_chips,centre_chips,bets,Player3)
	Win3_button = my_button(message="p3Win",x=-6,y=1,scale=(1,0.25))
	Win3_button.on_click =lambda: Win(centre_chips,player3_bet_chips,player3_chips,bets,Player3)

	Bet4_button = my_button(message="p4Bet",x=-2,y=3,scale=(1,0.25))
	Bet4_button.on_click =lambda: Bet(player4_bet_chips,centre_chips,bets,Player4)
	Win4_button = my_button(message="p4Win",x=-2,y=3.5,scale=(1,0.25))
	Win4_button.on_click =lambda: Win(centre_chips,player4_bet_chips,player4_chips,bets,Player4)

	Bet5_button = my_button(message="p5Bet",x=2,y=3,scale=(1,0.25))
	Bet5_button.on_click =lambda: Bet(player5_bet_chips,centre_chips,bets,Player5)
	Win5_button = my_button(message="p5Win",x=2,y=3.5,scale=(1,0.25))
	Win5_button.on_click =lambda: Win(centre_chips,player5_bet_chips,player5_chips,bets,Player5)

	Bet6_button = my_button(message="p6Bet",x=6,y=1,scale=(1,0.25))
	Bet6_button.on_click =lambda: Bet(player6_bet_chips,centre_chips,bets,Player6)
	Win6_button = my_button(message="p6Win",x=6,y=1.5,scale=(1,0.25))
	Win6_button.on_click =lambda: Win(centre_chips,player6_bet_chips,player6_chips,bets,Player6)

	Bet7_button = my_button(message="p7Bet",x=6,y=-1.5,scale=(1,0.25))
	Bet7_button.on_click =lambda: Bet(player7_bet_chips,centre_chips,bets,Player7)
	Win7_button = my_button(message="p7Win",x=6,y=-1,scale=(1,0.25))
	Win7_button.on_click =lambda: Win(centre_chips,player7_bet_chips,player7_chips,bets,Player7)

	Bet8_button = my_button(message="p8Bet",x=3,y=-3.5,scale=(1,0.25))
	Bet8_button.on_click =lambda: Bet(player8_bet_chips,centre_chips,bets,Player8)
	Win8_button = my_button(message="p8Win",x=3,y=-3,scale=(1,0.25))
	Win8_button.on_click =lambda: Win(centre_chips,player8_bet_chips,player8_chips,bets,Player8)

P1_money = Text(text=f"p1 money:{Player1.money.money}",scale = 15,parent = scene, origin=(-2,9),color = Color(0,0,0,0.8))

def update():
	P1_money.text = f"p1 money:{Player1.money.money}"
	#player1_card1.rotation_z += 1
	#player2_card1.rotation_z += 1 # flip card to reveal
	#player3_card1.rotation_z += 1
	#player3_card1.rotation_y += 1
	#player3_card1.rotation_x -= 1
	#print(player3_card1.rotation)
	for crd in card_models:
		crd.rotation_z += 1


app.run()