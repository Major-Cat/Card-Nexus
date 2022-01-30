def scoring(community, hands):
    def formatting(cards):
        ranks = '23456789TJQKA'
        formated_cards = []
        for card in cards:
            formated_cards.append(str(ranks[card.value-2]+card.suit))
        return formated_cards

    def evaluate(hand):
        ranks = '23456789TJQKA'
        rcounts = {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
        if len(hand) > 5: return max([evaluate(hand[:i] + hand[i+1:]) for i in range(len(hand))]) # a comparison here could determine if top 5 cards are from community, if so then return second highest (instead of max)
        score, ranks = zip(*sorted((cnt, rank) for rank, cnt in {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items())[::-1])
        if len(score) == 5:
            if ranks[0:2] == (12, 3): #adjust if 5 high straight
                ranks = (3, 2, 1, 0, -1)
            straight = ranks[0] - ranks[4] == 4
            flush = len({suit for _, suit in hand}) == 1
            '''no pair, straight, flush, or straight flush'''
            score = ([(1,), (3,1,1,1)], [(3,1,1,2), (5,)])[flush][straight]
        return score, ranks

    scores = []
    community = formatting(community)
    for i, hand in enumerate(hands):
        hand = formatting(hand)
        scores.append((i, evaluate(hand+community)))
    winner = sorted(scores , key=lambda x:x[1])[-1][1]
    return [x[0] for x in filter(lambda x: x[1] == winner, scores)]


