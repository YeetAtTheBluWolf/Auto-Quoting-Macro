"""Module to automate the pulling of quotes and macroing them into roblox."""

from time import sleep
from random import randint, choice
from quote import quote
from pyautogui import write
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

def mc_chat_macro():
    """This function is the main macro to print quotes to the minecraft client."""
    try:
        while():
            i = randint(1, 10)
            sleep(randint(5, 10))
            write('t')
            sleep(3)
            set_quote = random_set(i)
            write(quoter(set_quote[0], set_quote[1]))
            sleep(5)
            send_keys('{ENTER}')
    except KeyboardInterrupt as key_msg:
        print(f"{key_msg}\nClosing program...")

if __name__ == "__main__":
    mc_chat_macro()
