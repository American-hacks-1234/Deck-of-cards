import random

print('welcome to the digital python deck of CARDS V1.02')
print('controls: enter[key] = draw')

names = {1: 'ace', 11: 'jack', 12: 'queen', 13: 'king'}
suits = {1: 'diamonds', 2: 'clubs', 3: 'spades', 4: 'hearts'}

for _ in range(9999):
    if input() == '':
        b = names.get(random.randint(1, 13), str(random.randint(2, 10)))
        c = suits[random.randint(1, 4)]
        print(f'you drew the {b} of {c}')
