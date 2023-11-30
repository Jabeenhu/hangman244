import random

word_list = ["mango", "melon", "guava", "orange", "grapes"]
#print(word_list)

class Hangman(): 
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # replace _ with guess
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
        else:    
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                if guess not in self.word:
                    self.num_lives -= 1
                print(f"You have {self.num_lives} lives left.")
                print(f"{' '.join(self.word_guessed)}")
                if self.num_lives == 0:
                    print("You lose!")
                    print(f"The word was {self.word}.")
                    break
                elif '_' not in self.word_guessed:
                    print("You win!")
                    break

    def play(self):
        print("Welcome to Hangman!")
        print(f"You have {self.num_lives} lives left.")
        print(f"Your word has {self.num_letters} unique letters.")
        print(f"{' '.join(self.word_guessed)}")
        self.ask_for_input()

hangman = Hangman(word_list)
hangman.play()

