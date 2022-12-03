def decode(entry):
    ''' takes the ascii characters and subtracts them to get back
        1, 2 or 3 
        A Starts at 65 so you just do 65 - 64 = 1
        B 66 -64 = 2
        ...

        Y Starts at 88 so the same rule applies
    '''
    return (ord(entry[0]) -64, ord(entry[-1]) -87)

def decode_second(entry):
    their_hand = ord(entry[0]) -64

    if (your_value :=entry[-1]) == "X" : # finally a use for the walrus operator -_-
        if their_hand == 1:
            return their_hand, 3
        else:
            return their_hand, their_hand - 1
    elif your_value == "Z":
        if their_hand == 3:
            return their_hand, 1
        else:
            return their_hand, their_hand + 1
    else:
        return their_hand, their_hand



    return their_hand, your_hand

def play_round(their_hand: int, your_hand: int) -> int:
    '''
    Rock = 1
    Paper = 2
    Scisor = 3

    general case
    x + 1 = y would be a win
    x - 1 = y would be a lost
    x == y would be a tie

    special cases
    x = 1:  x 
    '''
    win = 6
    tie = 3

    if your_hand == their_hand:
        return your_hand + tie
    elif your_hand == 1 and their_hand == 3:
        return your_hand + win
    elif your_hand == 3 and their_hand == 1:
        return your_hand
    elif your_hand -1 == their_hand:
        return your_hand + win
    elif your_hand + 1 == their_hand:
        return your_hand
    

f = open('data/day2.txt', 'r')
data = f.readlines()

results = 0
results_2 = 0
for entry in data:
    your_hand, their_hand = decode(entry.strip("\n")) # stripping the \n at the end
    your_hand_2, their_hand_2 = decode_second(entry.strip("\n")) # stripping the \n at the end
    results += play_round(your_hand, their_hand)
    results_2 += play_round(your_hand_2, their_hand_2)

print(f'Part 1: score at the end: {results}')
print(f'Part 2: Score at the end: {results_2}')