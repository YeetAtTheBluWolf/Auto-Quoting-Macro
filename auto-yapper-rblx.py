from pyautogui import write, click, moveTo
from time import sleep
from random import randint
from quote import quote
from pywinauto.keyboard import send_keys
from argparse import ArgumentParser

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

def quoter(artist, num_searches):
    try:
        result = quote(artist, num_searches)
        index = num_searches - 1
        return result[index].get("quote")
    except: 
        return "SOMETHING IS NOT RIGHT"
    
def random_set(search_limit):
    try:
        # Grabs a random number for the number of searches
        search_index = randint(1, search_limit)

        # Grabs a viable index to quote an artist
        artist_index = randint(1, 12) - 1
        
        return (artist[artist_index], search_index)
    except:
        return (artist[0], 1)
    
def rblx_chat_macro(screen_x, screen_y):
    try:
        while(True):
            i = randint(1, 10)
            sleep(randint(1, 5))
            moveTo(screen_x - 10, screen_y - 10)
            moveTo(screen_x, screen_y)
            click(x=screen_x, y=screen_y)
            sleep(0.5)
            set_quote = random_set(i)
            write(quoter(set_quote[0], set_quote[1]))
            sleep(1)
            send_keys('{ENTER}')
            send_keys('{ENTER}')
    except KeyboardInterrupt as keyMsg:
        print("Closing program...")
    except:
        print("Something went wrong...")

def registerArgs():
    parser = ArgumentParser(description="A script to automatically spam chat with quotes.")
    parser.add_argument("--x", nargs=int)

if __name__ == "__main__":
    chat_box_x = 127
    chat_box_y = 352
    rblx_chat_macro(chat_box_x, chat_box_y)
