import random
import string

# Create a list of words from a file
# Make sure the words are over four lines long
words = []
with open('words.txt', 'r') as file:
    for line in file:
        if len(line) > 4:
            words.append(line)


# Function to return a random word
def random_word():
    rword = random.choice(words)
    rword = rword.strip()
    rword = rword.upper()
    return rword


def hangman():
    rword = random_word()
    rword_set = set(rword)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 6

    # If lives > 0 the player has run out of tries
    # If len(rword_set) > 0 the player has guessed correctly
    while lives > 0 and len(rword_set) > 0:
        print(f'You have {lives} lives left and the letters you have used are {" ".join(used_letters)}')

        word_list = [letter if letter in used_letters else "_" for letter in rword]
        print(f'Current word:, {" ".join(word_list)}')

        # Take in and evaluate user input
        user_letter = input('Guess a letter: ').upper()
        user_letter = user_letter.strip()

        if (user_letter in alphabet) and (user_letter not in used_letters):
            used_letters.add(user_letter)
            if user_letter in rword_set:
                rword_set.remove(user_letter)
                print('')
            else:
                # The user has got it wrong
                lives = lives - 1
                print(f'\nYour letter {user_letter} is not in the word')

        elif (user_letter in used_letters):
            print('\nYou have already used that letter, Guess Again')

        else:
            print('\n That is not a valid letter')

    if lives == 0:
        print(f'YOU DIED, sorry, the word was, {rword}')
    else:
        print(f'YAAY! you correctly guessed the word {rword} !!')


if __name__ == "__main__":
    hangman()
