from pyautogui import write
from time import sleep
from random import randint
from quote import quote
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
    
def mc_chat_macro():
    try:
        while(True):
            i = randint(1, 10)
            sleep(randint(5, 10))
            write('t')
            sleep(3)
            set_quote = random_set(i)
            write(quoter(set_quote[0], set_quote[1]))
            sleep(5)
            send_keys('{ENTER}')
    except KeyboardInterrupt as keyMsg:
        print("Closing program...")
    except Exception as e:
        print("Something went wrong...")
        print(e)

if __name__ == "__main__":
    mc_chat_macro()
