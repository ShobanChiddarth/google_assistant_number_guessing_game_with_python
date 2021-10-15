import random
n=random.randint(1,100)
print('''This script has thought of a number
It is between 1 and 100
''')
while True:
    v=int(input('Guess the number : '))
    if (v==n):
        print('''
You guessed it right
        ''')
        break
    else:
        if (v>n):
            print('It is lower than your previous guess')
            continue
        else:
            print('It is higher than your previous guess')
            continue
input('Press enter to close')