import json
import pickle
import gzip


read = True
write = False

if write: # Process = Pickle to bytes, gzip to compress, Pickle to file.
	with open('postflop_lookup.json', 'r') as f:
		lookup = json.load(open('postflop_lookup.json', 'r'))

	lookup = pickle.dumps(lookup)
	lookup = gzip.compress(lookup)

	with open('Postflop_lookup_b.pkl', 'wb') as f:
		pickle.dump(lookup, f)

if read: # Process = Pickle to open file, gzip to decompress, pickle to dict.
	with open('Postflop_lookup_b.pkl', 'rb') as f:
		lookup = pickle.load(f)
	lookup = gzip.decompress(lookup)
	print(type(lookup))
	lookup = pickle.loads(lookup)
	print(type(lookup))




#pickle.dump(lookup, open('Postflop_lookup_b.pkl','wb'))
#print(zlib.decompress(output_hand[0]).decode())