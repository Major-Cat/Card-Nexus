import json
from tqdm import tqdm
from Interpolation_Generator import bilinear_interpolation	#the only time this is used

raw = json.load(open('postflop_lookup_raw.json', 'r'))	#generated results
output = json.load(open('postflop_lookup.json', 'r'))	
grid = [(1,0,20.0),(1,100,100.0),(217,0,0.1),(217,100,100.0)]	#parameters for the interpolation

for item in range(raw['Hands'].items()):
	draws = item[1][0]
	wins = item[1][1]
	ratio = round((wins/draws)*100,2)
	try:
		weight = round(bilinear_interpolation(draws, ratio, grid),3)	#converts the number of wins into a decimal chance of winning
	except ValueError:
		print()
		print(item)
		print(f'Draws = {draws}')
		print(f'Ratio = {ratio}')
		quit()
	output['Hands'][item[0]] = weight

with open('postflop_lookup.json', 'w') as f:
	json.dump(output, f)