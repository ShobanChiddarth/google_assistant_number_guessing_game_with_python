import random, time
print('''Think of a number between 1 and 100
This script will guess it
''')
n=random.randint(1,100)
lower,upper=1,100
time.sleep(1.5)
while True:
    print('The number is',n)
    choice=input('Yes / no? ')
    choice=choice.strip().lower()[0]
    if (choice=='y'):
        print('''
Guessed
''')
        break
    elif (choice=='n'):
        v=input('Higher or Lower? ')
        v=v.strip().lower()[0]
        if (v=='h'):
            if (lower<n):
                lower=n
            n=random.randint(lower,upper)
        elif (v=='l'):
            if (upper>n):
                upper=n
            n=random.randint(lower,upper)
        else:
            print('Invalid choice')
    else:
        print('Invalid choice')
input('Press enter to close')   