import json
from tqdm import tqdm
from interpolation_test import bilinear_interpolation

raw = json.load(open('postflop_lookup_raw.json', 'r'))
output = json.load(open('postflop_lookup.json', 'r'))
grid = [(1,0,20.0),(1,100,100.0),(217,0,0.1),(217,100,100.0)]

for item in tqdm(raw['Hands'].items()):
	# item = ("10C10D10H10S11C": [142, 142]),
	draws = item[1][0]
	wins = item[1][1]
	ratio = round((wins/draws)*100,2)
	try:
		weight = round(bilinear_interpolation(draws, ratio, grid),3)
	except ValueError:
		print()
		print(item)
		print(f'Draws = {draws}')
		print(f'Ratio = {ratio}')
		quit()
	output['Hands'][item[0]] = weight

with open('postflop_lookup.json', 'w') as f:
	json.dump(output, f)