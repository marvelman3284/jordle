from rich import box
from rich.console import Console
from rich.table import Table


def get_words(file: str) -> tuple[list[str], str]:
    with open(file, "r") as f:
        words = [i.strip("\n") for i in f.readlines()]

    word = "able"

    return words, word


# TODO: re print the table every time and change the letter color


def setup_board(word: str, guess_num: int = 5):
    table = Table(title="Jordle", show_header=False, box=box.ROUNDED)

    for _ in range(len(word)):
        table.add_column("")

    for _ in range(guess_num):
        table.add_row("", "", "")

    console = Console()
    console.print(table)


# TODO: check if the word is valid (need a func)
# TODO: using len(table.columns) add empty spaces in the tables


def add_Columns(table: Table) -> list[str]:
    col = []
    for _ in range(len(table.columns)):
        col.append("")

    return col


def validate_word(guess: str, word:str, words: list[str]) -> bool:
    if len(guess) == len(word):
        if word in words:
            return True
        else:
            return False
    else: return False


def game(table: Table, console: Console, word: str, words: list[str]):
    guess = input("Enter a word: ")

    while not validate_word(guess, word, words):
        print(f"Word is not {len(word)} letters long!")
        guess = input("Enter a word: ")

        if validate_word(guess, word, words): break

    table.add_row(*guess)

    for _ in range(4):
        table.add_row(*add_Columns(table))

    console.print(table)


def guess_ans(word: str, words: list[str]):
    table = Table(title="Jordle", show_header=False, box=box.ROUNDED)
    console = Console()


    game(table, console, word, words)



words, word = get_words("data/words.txt")

setup_board(word)
guess_ans(word, words)
