RANK_VALUES = {

    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,

    "J": 10, "Q": 10, "K": 10, "A": 11,

}
 
 
def hand_value(cards):

    total = sum(RANK_VALUES[card] for card in cards)

    aces = cards.count("A")

    while total > 21 and aces > 0:

        total -= 10

        aces -= 1

    return total
 
 
def parse_state(text):

    hand_str, dealer_upcard, flag = [part.strip() for part in text.split("|")]

    hand = [rank.strip() for rank in hand_str.split(",")]
 
    return {

        "hand": hand,

        "dealer_upcard": dealer_upcard,

        "first": flag == "first",

    }
 
 
def generate_actions(state):

    hand = state["hand"]

    
    actions = ["hit", "stand"]
    if action = "stand"
        state = {
    "hand": ["10", "6"],
    "dealer": "9",
    "first": True
}

action = "stand"

if action == "stand":
    result = state

print(result)
 
    if state["first"]:

        actions.append("double")

        actions.append("surrender")
 
        # only for same rank

        if len(hand) == 2 and hand[0] == hand[1]:

            actions.append("split")
 
        if state["dealer_upcard"] == "A":

            actions.append("insurance")
 
    return actions
 
 
def _hand_result(hand, dealer_upcard, first):

    total = hand_value(hand)

    return {

        "hand": hand,

        "dealer_upcard": dealer_upcard,

        "first": first,

        "total": total,

        "busted": total > 21,

    }
 
 
def apply_action(state, action, next_card=None):

    legal = generate_actions(state)

    if action not in legal:

        raise ValueError(f"{action!r} is not legal here (legal actions: {legal})")
 
    hand = state["hand"]

    dealer_upcard = state["dealer_upcard"]
 
    if action == "hit":

        return ...
 
    if action == "stand":

        return ...
 
    if action == "double":
        new_hand = hand.copy()
        new_hand.append(next_card)

        result = _hand_result(
            new_hand,
            dealer_upcard,
            first=False
        )
        result["bet_multiplier"] = 2 
        return result 

 
    if action == "surrender":

        result = _hand_result(hand, dealer_upcard, first=False)

        result["surrendered"] = True

        result["bet_multiplier"] = 0.5

        return result
 
    if action == "split":

        card_a, card_b = hand[0], hand[1]

        hand_a = _hand_result([card_a], dealer_upcard, first=True)

        hand_b = _hand_result([card_b], dealer_upcard, first=True)

        return hand_a, hand_b
 
    if action == "insurance":

        result = _hand_result(hand, dealer_upcard, first=True)
        result["insurance"] = True
        return result

        
 
