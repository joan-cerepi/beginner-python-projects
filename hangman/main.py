import random
import sys
from hangman import Hangman


def get_wordlist(words: str) -> list:
    """Open a wordlist file, go through it and return a list of all the words.

    Parameters
        words: wordlist file

    Return
        rtype: list
        data: words from the wordlist file"""
    wordlist = []
    with open(words) as wordlist_file:
        for word in wordlist_file.readlines():
            clean_word = word.strip()
            wordlist.append(clean_word)
    return wordlist


def print_banner(text: str) -> None:
    """Display a banner with a text of your choice.

    Parameters
        text: text you want to be displayed on the screen

    Return
        rtype: None"""
    try:
        import pyfiglet
    except ModuleNotFoundError:
        print()
        print(text.upper())
        print()
    else:
        pyfiglet.print_figlet(text)


def main() -> None:
    """This is where everything comes together."""
    words = get_wordlist('words.txt')
    random_word = random.choice(words)
    hangman_game = Hangman(random_word)

    print_banner('Hangman')
    hangman_game.display_image()
    hangman_game.display_word()
    print()

    while hangman_game.get_failed_tries() < 6:
        user_input = input('Guess a letter: ').upper()
        if not hangman_game.has_letter_been_used(user_input):
            hangman_game.update_letters(user_input)
        else:
            print(
                f"Letter '{user_input}' has been used before. Try a different letter.")
            print()
            continue
        hangman_game.display_image()
        hangman_game.display_word()

        if hangman_game.check_if_complete():
            print(f'You win! Your word is: {random_word.upper()}')
            sys.exit()

    print(f"Game Over! You lose. The correct word was '{random_word}'.")
    print()


if __name__ == '__main__':
    main()
