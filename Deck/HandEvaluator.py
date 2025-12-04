from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    ranks = [card.rank.value for card in hand]
    suits = [card.suit for card in hand]
    rank_counts = {}
    for r in ranks:
        rank_counts[r] = rank_counts.get(r, 0) + 1
    sorted_counts = sorted(rank_counts.values(), reverse=True)
    suit_counts = {}
    for s in suits:
        suit_counts[s] = suit_counts.get(s, 0) + 1

    flush_suit = None
    for s, c in suit_counts.items():
        if c >= 5:
            flush_suit = s
            break

    unique_ranks = sorted(set(ranks))
    if 14 in unique_ranks:
        unique_ranks.append(1)
        unique_ranks = sorted(unique_ranks)

    straight = False
    for i in range(len(unique_ranks) - 4):
        seq = unique_ranks[i:i+5]
        if seq[4] - seq[0] == 4 and len(set(seq)) == 5:
            straight = True
            break

    if flush_suit is not None:
        flush_cards = sorted([card.rank.value for card in hand if card.suit == flush_suit])
        ranks_f = set(flush_cards)
        if 14 in ranks_f:
            ranks_f.add(1)
        ranks_f = sorted(ranks_f)

        for i in range(len(ranks_f) - 4):
            seq = ranks_f[i:i+5]
            if seq[4] - seq[0] == 4 and len(set(seq)) == 5:
                return "Straight Flush"

    if sorted_counts[0] == 4:
        return "Four of a Kind"
    if sorted_counts[0] == 3 and sorted_counts[1] >= 2:
        return "Full House"
    if flush_suit is not None:
        return "Flush"
    if straight:
        return "Straight"
    if sorted_counts[0] == 3:
        return "Three of a Kind"
    if sorted_counts[0] == 2 and sorted_counts[1] == 2:
        return "Two Pair"
    if sorted_counts[0] == 2:
        return "One Pair"
    return "High Card" # If none of the above, it's High Card
