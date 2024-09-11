import random

# create word bank
word_bank = ['seahawks', 'resident evil', 'halo', 'alpha', 'final fantasy']

# use random module to select random word from word bank
word = random.choice(word_bank)

# greet user
name = input('What is your name? ').title()
print(f'Hello {name}, lets play some Hangman!')

# player guesses
guesses = ' '

# number of turns
turns = 6


# create a while loop
while turns > 0:
    
    # make a failed flag
    failed = False
    
    
    # loop every character in word
    for char in word:
        # check if character is in player guess
        if char in guesses:
            print(char, end=' ')
        else:
            # if character is not found
            print('_', end=' ')
            failed = True
            
            
    # if loop finds every letter in guesses
    if not failed:
        print(f'Congrats, you guessed the word: "{word}"!')
        break
    
    
    # user guess character
    guess = input('Guess a letter: ')
    
    # set players guess to guesses
    guesses += guess
    
    
    # if the guess is not found in the word
    if guess not in word:
        # decrease turns
        turns -= 1
        # print you lose, if turns is equal to zero
        if (turns > 0):
            # print wrong guess message
            print(f'Wrong guess, try again! You have {turns} turns left!')
        else:
            print(f'Your out of turns! You loseeeee. The chosen word was: "{word}"')
            
        