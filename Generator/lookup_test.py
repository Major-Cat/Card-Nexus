from json import load
from random import randint
from time import time
import pickle
import gzip
start_time = time()
compressed = False

if compressed:
	with open('Postflop_lookup_b.pkl', 'rb') as f:
		lookup = pickle.load(f)
	lookup = gzip.decompress(lookup)
	lookup = pickle.loads(lookup)
	'''
	Load time = 1.2398114204406738
	Hand count: 2598960
	Search time = 1.4101152420043945
	Draw Index: 1517602
	Draw: ('12C12D14C3S7S', 30.942)
	[Finished in 1.6s]
	'''
else:
	with open('postflop_lookup.json', 'r') as f:
		lookup = load(f)
	'''
	Load time = 2.393923044204712
	Hand count: 2598960
	Search time = 2.565817356109619
	Draw Index: 584440
	Draw: ('10H12H14D2S9C', 6.273)
	[Finished in 2.7s]
	'''

print(f'Load time = {time()-start_time}')

lookup = lookup['Hands']

hand_count = len(lookup.items())
print(f'Hand count: {hand_count}')
random_draw = randint(0, hand_count)
draw = list(lookup.items())[random_draw]
print(f'Search time = {time()-start_time}')

print(f'Draw Index: {random_draw}')
print(f'Draw: {draw}')
