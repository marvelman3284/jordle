from rich import box
from rich.console import Console
from rich.table import Table
from rich import print
from rich.prompt import Prompt 

guesses = ["", " ", " ", " ", " ", " "]


def get_words(file: str) -> tuple[list[str], str]:
    with open(file, "r") as f:
        words = [i.strip("\n") for i in f.readlines()]

    word = "able"

    return words, word


# TODO: re print the table every time and change the letter color


def format_word(word: str, guess: str):
    wordl = list(guess)
    new_word = []

    for i in range(len(word)):
        if guess[i] in word:
            if guess[i] == word[i]:
                new_word.append(f"[green]{wordl[i]}[/green]")
            else:
                new_word.append(f"[yellow]{wordl[i]}[/yellow]")
        else:
            new_word.append(f"[red]{wordl[i]}[/red]")

    guesses[guesses.index(guess)] = new_word


def setup_board(word: str, guess_num: int = 5):
    table = Table(title="Jordle", show_header=False, box=box.ROUNDED)

    for _ in range(len(word)):
        table.add_column("")

    for _ in range(guess_num):
        table.add_row("", "", "")

    console = Console()
    console.print(table)


def validate_word(guess: str, word: str, words: list[str]) -> bool:
    if len(guess) == len(word) and guess in words:
        return True
    else:
        return False


def game(word: str, words: list[str], guess_num: int):
    table = Table(title="Jordle", show_header=False, box=box.ROUNDED)
    console = Console()

    guess = input("Enter a word: ")

    while not validate_word(guess, word, words):
        print(f"Word is not {len(word)} letters long or a valid word!")
        guess = input("Enter a word: ")

        if validate_word(guess, word, words):
            break

    guesses[guess_num - 1] = guess
    format_word(word, guess)

    for i in guesses[::-1]:
        table.add_row(*i)

    console.print(table)

    if guess == word:
        print("[green]You guessed it![/green]")
        quit()


def guess_ans(word: str, words: list[str]):

    for i in range(6, 0, -1):
        game(word, words, i)


def help():
    print("This is Jordle! You have 6 tries to guess a random word of varying length. Once you get a word the letters will change color:")
    print("[green]Green/your terminals green color means right character, right spot[/green]")
    print("[yellow]Yellow/your terminals yellow color means right character, wrong spot[/yellow]")
    print("[red]Red/your terminals red color means wrong character[/red]")


def main():
    help_input = Prompt.ask("Would you like to play or view the rules?", choices=['Play', 'Rules'])
    if help_input == 'Play':
        words, word = get_words("data/words.txt")

        setup_board(word)
        guess_ans(word, words)
        game(word, words, 5)

    else:
        help()


if __name__ == "__main__":
    main()
