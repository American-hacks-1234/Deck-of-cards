import random
print('welcome to the digetal python deck of CARDS V1.00 open alpha')
print('contolls: enter[key] = draw')
d=2
for d in range(9999):
    a=input()
    if a=='':
        b= random.randint(1, 13)
        c= random.randint(1, 4)
        b=int(b)
        c=int(c)
        if b==13:
            b='king'
        elif b==12:
            b='queen'
        elif b==11:
            b='jack'
        elif b==0:
            b='ace'
        if c==1:
            c='diamonds'
        elif c==2:
            c='clubs'
        elif c==3:
            c='spades'
        elif c==4:
            c='hearts'
    
    
        print(f'you drew the {b} of {c}')
