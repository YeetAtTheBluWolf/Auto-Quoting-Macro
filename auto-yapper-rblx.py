"""Module to automate the pulling of quotes and macroing them into roblox."""

from time import sleep
from random import randint,choice
from argparse import ArgumentParser
from quote import quote
from pyautogui import write, click, moveTo
from pywinauto.keyboard import send_keys

artist = [ "Frank Zappa",
          "Albert Einstein",
          "J.K. Rowling",
          "Friedrich Nietzsche",
          "Ralph Waldo Emerson",
          "Mother Teresa",
          "Oscar Wilde",
          "Mark Twain",
          "Aristotle",
          "Johnny Depp",
          "Confucious" ]

def quoter(author, num_searches):
    """This function returns a quote from the requested author."""
    try:
        result = quote(author, num_searches)
        index = num_searches - 1
        return result[index].get("quote")
    except IndexError as e:
        return f"{e}\nThe script was unable to find a quote or author."
    except TypeError as e:
        return f"The script was unable to find type and returned a bad value.\n{e}"

def random_set(search_limit):
    """Returns a random quote from a random artist from the artist list."""
    try:
        # Grabs a random number for the number of searches
        search_index = randint(1, search_limit)

        # Grabs a viable index to quote an artist
        random_author = choice(artist)

        return (random_author, search_index)
    except TypeError as e:
        print(f"{e}\nThe script attempted to get a random artist but the script failed.")
        return ("Albert Einstein", 1)
    except IndexError as e:
        print(f"{e}\nFailed to chose a random string from list.")
        return ("Albert Einstein", 1)

def rblx_chat_macro(screen_x, screen_y):
    """This function is the main macro to print quotes to the roblox client."""
    try:
        while True:
            i = randint(1, 10)
            sleep(randint(1, 5))
            moveTo(screen_x - 50, screen_y - 50)
            moveTo(screen_x + 50, screen_y + 50)
            moveTo(screen_x, screen_y)
            click(x=screen_x, y=screen_y)
            sleep(0.5)
            set_quote = random_set(i)
            write(quoter(set_quote[0], set_quote[1]))
            sleep(1)
            send_keys('{ENTER}')
            send_keys('{ENTER}')
    except KeyboardInterrupt as key_msg:
        print(f"{key_msg}\nClosing program...")

def register_args():
    """This function registers arguments for the script."""
    parser = ArgumentParser(prog="auto_yapper_rblx",
                            description="A script to automatically spam chat with quotes.")
    parser.add_argument("--x",
                        type=int,
                        help="X coordinate of the screen.",
                        default=238,
                        action="store")
    parser.add_argument("--y",
                        type=int,
                        help="Y coordinate of the screen.",
                        default=83,
                        action="store")
    return parser.parse_args()

if __name__ == "__main__":
    args = register_args()
    # DEFAULT X and Y is x=127 and y=352
    X = args.x
    Y = args.y
    rblx_chat_macro(X, Y)
