target = 12
guesses = 1
userChoice = int(input('Guess the number: '))
while userChoice != target:
    guesses = guesses + 1
    if userChoice < target:
        print('Guess higher!')
        userChoice = int(input('Guess the number: '))
    elif UserChoice > target:
        print('Guess lower!')
        userChoice = int(input('Guess the number: '))
else:
    print('It took you' , guesses, 'guesses')
