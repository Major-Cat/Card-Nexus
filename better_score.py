def scoring(community, hands):
    def formatting(cards):  #formats the cards for easier scoring
        ranks = '23456789TJQKA'
        formated_cards = []
        for card in cards:
            formated_cards.append(str(ranks[card.value-2]+card.suit))   #list of values and suits
        return formated_cards

    def evaluate(hand, community):  #generates the score
        ranks = '23456789TJQKA'
        if len(hand) > 5: return max([evaluate(hand[:i] + hand[i+1:], community) for i in range(len(hand))])
        score, ranks = zip(*sorted((cnt, rank) for rank, cnt in {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items())[::-1])
        if len(score) == 5:
            if ranks[0:2] == (12, 3): #adjust if 5 high straight
                ranks = (3, 2, 1, 0, -1) 
            straight = ranks[0] - ranks[4] == 4     #checks for each possible straight
            flush = len({suit for _, suit in hand}) == 1    #checks for flushes
            #no pair, straight, flush, or straight flush
            score = ([(1,), (3,1,1,1)], [(3,1,1,2), (5,)])[flush][straight] #picks score based on whether it has each hand type 
        if set(hand) == set(community): #think this should prevent someone from winning by using only community cards
            score = (0,)   
        return score, ranks

    scores = []
    community = formatting(community)
    for i, hand in enumerate(hands):
        hand = formatting(hand)
        scores.append((i, evaluate(hand+community, community)))
    winner = sorted(scores , key=lambda x:x[1])[-1][1]
    return [x[0] for x in filter(lambda x: x[1] == winner, scores)]

