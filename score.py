class Score:
	def __init__(self, cards = [[]], points=0):
		self.cards = cards
		self.points = points

	def scores(self):
		print(self.cards,"cards in the hand")
		#print(self.cards[0],"first card in hand")
		flush, straight, pair, three, four = self.check()
		twoPair = []
		
		if flush == True and straight[-1] == 14: total = 1000
		elif flush == True and straight != []: total = 100
		elif four != []: total = 90
		elif pair[-1] != [] and three != []: total = 80
		elif flush == True: total = 70
		elif straight != []: total = 60
		elif three != []: total = 50
		
	def straight(self,nums):
		bye = []
		for i in nums:
			aaaa = [x for x in range(i, i+5) if i <= (max(nums)-4)]
			if all(elem in nums for elem in aaaa) and aaaa != []:
				bye = aaaa
			else:
				pass
		return bye
	
	def check(self):
		H,S,C,D = 0,0,0,0
		for i in self.cards:
			if i[1] == "S": S += 1
			if i[1] == "H": H += 1
			if i[1] == "C": C += 1
			if i[1] == "D": D += 1
		if S > 4 or H > 4 or C > 4 or D > 4: Flush = True
		else: Flush = False
		nums = []
		for i in self.cards:
			try:
				nums.append(i[0])
			except:
				break

		duplicates = {i:nums.count(i) for i in nums}
				
		print(duplicates)
		Pair,Three,Four = [],[],[]
		for (k,v) in duplicates.items():
			if v == 4: Four = [k]
			elif v == 3: Three = [k]
			elif v == 2: Pair.append(k)
		print(Pair,Three,Four)
			
		if len(nums)>5:
			nums = sorted(nums)
			straight = self.straight(nums)
			try: straight = straight[-1]
			except: straight = False

		return Flush, straight, Pair, Three, Four
