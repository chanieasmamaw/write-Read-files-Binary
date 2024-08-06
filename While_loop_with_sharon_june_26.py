from icecream import ic
"""

def is_substring_while(str1, str2) -> bool:
    # Check if str2 is longer than str1, if so, str2 can't be a substring of str1
    if len(str2) > len(str1):
        return False
    # Initialize the index
    i = 0
    while i <= len(str1) - len(str2):
        # Check if the substring of str1 starting from index i matches str2
        if str1[i:i + len(str2)] == str2:
            return True
        i += 1
    return False

# Input strings from the user
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

# Print the result of the substring check
print(is_substring_while(str1, str2))
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
The HangPerson game 😵 !!!

RULES:
- Create a game where the user has to guess a word.
- The word is randomly chosen by the computer from a list.
- The user has to guess the word one letter at a time.
- The user has a limited number of attempts to guess the word.
- If the user guesses a letter that is not in the word, the number of attempts decreases by 1.
- If the user guesses a letter that is in the word, the letter is revealed in the word, and they have to guess the remaining letters.
- If the user guesses the word correctly within the number of attempts, they win the game.

UX/UI BONUS:
- Add a graphic to the game (the hangman).
- Add a timer to the game.

EXAMPLE OF GAME OUTPUT:

You have 3 lives left.
Guess this word: ______

Type a letter: a
Congratulations, the letter 'a' appears 1 time!

You have 3 lives left
Guess this word: _a____

Type a letter: x
Sorry, 'x' is not in the word. Try again!

..... (etc)

You have 1 lives left
Guess this word: bab___

Type a letter: n
Congratulations, the letter 'n' appears 1 time!

You have 1 lives left
Guess this word: bab__n

Type a letter: o
Congratulations, the letter 'o' appears 2 times!

You win! Congratulations, the word was: baboon
You have 1 lives remaining.

"""
from random_word import RandomWords
r = RandomWords()

def create_random_word():
  random_word = r.get_random_word()
  return list(random_word)


def create_underline_word_list(random_word):
  underline_word_list = ["_"] * len(random_word)
  #print(f"Guess this word: {' '.join(underline_word_list)}")
  return underline_word_list


def guess_letters_by_user():
  lives = 3
  while lives > 0 and "_" in create_underline_word_list:
    #print("You have {lives} lives left.")
    #print(f"Guess this word: {' '.join(underline_word_list)}")
    guess_char = str(input("Guess a letter: "))
    guess_char = guess_char.lower()

    if guess_char in random_word:
      for index, letters in enumerate(random_word):
        if letters == guess_char:
          create_underline_word_list(random_word)[index] = guess_char
          #print(create_underline_word_list(random_word)[index])
    else:
      print(f"Sorry, '{guess_char}' is not in the word. Try again!")

      print(f"You have {lives} lives left.")
      print(f"Guess this word: {create_underline_word_list(random_word)}")

    lives -= 1
guess_letters_by_user()

def main():
  print("Welcome to the game!")
  random_word = create_random_word()
  print(random_word)
  underline_world_list = create_underline_word_list(random_word)
  guess_letters_by_user(random_word, underline_world_list)
main()


"""
from random_word import RandomWords

# Create an instance of RandomWords
r = RandomWords()


def create_random_word():
    random_word = r.get_random_word()
    return list(random_word)


def create_underline_word_list(random_word):
    underline_word_list = ["_"] * len(random_word)
    return underline_word_list


def guess_letters_by_user(random_word, underline_word_list):
    lives = 5
    while lives > 0:
        print(f"You have {lives} lives left.")
        print(f"Guess this word: {' '.join(underline_word_list)}")
        guess_char = input("Guess a letter: ").lower()
        
        if guess_char in random_word:
            for index, letter in enumerate(random_word):
                if letter == guess_char:
                    underline_word_list[index] = guess_char
            
            if "_" not in underline_word_list:
                print(f"Congratulations! You guessed the word: {''.join(random_word)}")
                return
        else:
            lives -= 1
            print(f"Sorry, '{guess_char}' is not in the word. Try again!")
        
        if lives == 0:
            print(f"Game over! The word was: {''.join(random_word)}")


def main():
    print("Welcome to the game!")
    random_word = create_random_word()
    underline_word_list = create_underline_word_list(random_word)
    guess_letters_by_user(random_word, underline_word_list)


# Run the game
main()





















