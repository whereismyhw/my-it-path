import random

def generate_bingo():
    numbers = random.sample(range(1, 76), 25)
    
    bingo = []
    for i in range(0, 25, 5):
        row = numbers[i:i+5]
        bingo.append(row)
    
    bingo[2][2] = 0
    
    return bingo