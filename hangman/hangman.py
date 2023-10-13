class Hangman:

    def __init__(self, selected_word: str) -> None:
        """Initialize attributes.

        Parameters
            selected_word: word that you use to play the game.
        Return
            rtype: None"""
        self.selected_word = [letter.upper() for letter in selected_word]
        self.used_letters = set()
        self.user_guess = [user_guess_letter for user_guess_letter in (
            len(self.selected_word) * '_')]
        self.failed_tries = 0
        self.HANGMAN_IMAGE = [
            '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    def update_letters(self, user_input: str) -> None:
        """When the user provides a letter, this function updates the failed_tries as well as
        makes the correct letters visible in the word that is to be guessed.

        Parameters
            user_input: letter the user inputs into the program.

        Return
            rtype: None"""
        upper_user_input = user_input.upper().strip()
        if upper_user_input in self.selected_word:
            for i, letter in enumerate(self.selected_word):
                if upper_user_input == letter:
                    self.user_guess[i] = letter
                    self.used_letters.add(letter)
        else:
            self.failed_tries += 1
            self.used_letters.add(upper_user_input)

    def has_letter_been_used(self, user_input: str) -> bool:
        """Check if letter has been used before.

        Parameters
            user_input: letter entered by the user
        Return
            rtype: bool"""
        return user_input.upper() in self.used_letters

    def display_image(self) -> None:
        """Display the proper hangman image.

        Return
            rtype: None"""
        print(self.HANGMAN_IMAGE[self.failed_tries])

    def get_failed_tries(self) -> int:
        """Return the number of failed tries."""
        return self.failed_tries

    def check_if_complete(self) -> bool:
        """Check to see if the user has completed the word and guessed what it is.

        Return
            rtype: bool"""
        return self.selected_word == self.user_guess

    def display_word(self) -> None:
        """Display already used letters as well as the word progress.

        Return
            rtype: None"""
        used_letters = ','.join(self.used_letters) if len(
            self.used_letters) > 0 else '[None yet]'
        print(f'Already used letters: {used_letters}')
        print(' '.join(self.user_guess))
