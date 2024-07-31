import random

def intro():
    print("Hello! What is your name?")
    user = input()
    print("Nice to meet you, {user}. Let's get ready to play a game of Hangman!")
    print("The rules are simple: enter a letter that might be in the secret word.")
    print("You can make only six wrong guesses before you lose.")
    print("Type 'hint' to reveal one letter of the word.")
    print("Let's Begin!")

def display_graphics(attempts):
    graphics = [
        '''------------
        ''',                 
        '''------------
|         |  
''',
        '''------------
|         |         
|          O
''',
        '''------------
|         | 
|          O 
|         / | 
''',
        '''------------
|         | 
|          O 
|         / | 
|          | 
''',
        '''------------
|         |
|          O 
|         / |
|          |
|         / | 
|            '''
    ]
    # Ensure attempts are within the bounds of the graphics list
    index = min(attempts, len(graphics) - 1)
    print(graphics[index])

def reveal_hint(word, dashes, used_hints):
    available_positions = [i for i in range(len(word)) if dashes[i] == '_']
    if available_positions:
        position = random.choice(available_positions)
        dashes[position] = word[position]
        used_hints.add(position)
    return dashes

def play_game():
    wordlist = ['bee', 'rainbow', 'flamingo', 'science', 'chocolate', 'cables', 'printer', 'blue', 'adventure', 'fountain']
    word = random.choice(wordlist)
    word = list(word)  # Convert word to list of characters
    dashes = ['_'] * len(word)
    used_hints = set()
    
    print(f"The length of the word is: {len(word)}")
    print("Generating secret word! :)")
    print(' '.join(dashes))

    attempts = 0
    guessed_letters = set()

    while attempts < 6:
        letter = input('Enter a letter you would like to guess or type "hint" for a hint: ').lower()

        if letter == 'hint':
            if len(used_hints) < len(word):
                dashes = reveal_hint(word, dashes, used_hints)
                print('Hint revealed!')
                print(' '.join(dashes))
            else:
                print("No hints left to reveal.")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(letter)

        if letter in word:
            print('YAY! The letter is in the word.')
            for index, char in enumerate(word):
                if char == letter:
                    dashes[index] = letter
            print(' '.join(dashes))

            if '_' not in dashes:
                print('Congratulations! You have guessed the word. You win!')
                break

        else:
            print('The letter is not in the word.')
            attempts += 1
            display_graphics(attempts)
            if attempts == 6:
                display_graphics(attempts)  # Display the final state
                print(f'Too many incorrect guesses. You lost! The word was: {"".join(word)}')
                break  # End the game immediately

    print('Goodbye!')

intro()
play_game()
