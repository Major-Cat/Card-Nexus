from cards import *
from better_score import *
import json
from tqdm import tqdm

epochs = 250000 #150,000 takes 30s	#number of tests to be done at a time
file_name = "preflop_lookup.json"

def sort_hand_into_string(list_of_cards):	#similiar to formatting from score, creates a list with all of the values and suits
	temp_list = []
	for card in list_of_cards:
		temp_list.append(str(str(card.value)+str(card.suit)))
	return str(sorted(temp_list)[0]+sorted(temp_list)[1]) # Use this return for Pre-flop

	string = ''
	for x,i in enumerate(temp_list): 
		string += str(sorted(temp_list)[x])
	return string # Use this return for Post-flop


with open(file_name, 'r') as f:
	lookup = json.load(f)

for i in range(epochs):
	deck = Deck()	#creates new deck
	players = 8 	#number of hands to draw for

	# Draw 5 cards for community if doing postflop
	community = []
	for i in range(3): # Scoring function can handle 3,4, or 5 community cards. It uses recursion to only use the best 5 cards.
		community.append(deck.draw())

	# Draw 2 cards for each player
	hands = []	#simple hand system for this generator
	for player in range(players):
		hand = []
		for i in range(2):
			hand.append(deck.draw())
		hands.append(hand)
		# Use this code block for Pre-flop
		if sort_hand_into_string(hand) not in lookup['Hands'].keys():
			lookup['Hands'][sort_hand_into_string(hand)] = 0

		#this is code block for Post-flop
		if sort_hand_into_string(hand+community) not in lookup['Hands'].keys():
			lookup['Hands'][sort_hand_into_string(hand+community)] = [1,0]
		else:
			lookup['Hands'][sort_hand_into_string(hand+community)][0] += 1
		

	winner = scoring(community, hands)
	for win in winner:
		# Use this for Pre-flop wins
		lookup['Hands'][sort_hand_into_string(hands[win])] += 1
		
		# Use this for Post-flop wins
		#lookup['Hands'][sort_hand_into_string(hands[win]+community)][1] += 1
	lookup["Epoch"] += 1

with open(file_name, 'w') as f:
	json.dump(lookup, f, sort_keys=True)


