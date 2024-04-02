from assets.jokes import jokes_list
from assets.quotes import quotes_list
import time
import random

def jokebot():
    print("Do you want to hear a joke ? y/n")

    user.input = input()
    if user_input == "y":
        print("user said yes")
    elif user_input == "n":
        print("user said no")
    else:
        print("I couldnt understand what you said")
    
print(random.choice(jokes_list))

this_joke = random.choice(jokes_list)

print(this_joke["setup"])
print(this_joke["punchline"])
