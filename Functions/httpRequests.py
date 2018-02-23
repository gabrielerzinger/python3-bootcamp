import requests
import termcolor
import pyfiglet
import random

text = termcolor.colored(pyfiglet.figlet_format(
    "Jokes on you"), color="cyan", attrs=["blink"])
print(text)

theme = input("Tell me a theme that you want to hear a joke about ")

url = "https://icanhazdadjoke.com/search"


res = requests.get(
    url, headers={"Accept": "application/json"},
    params={"term": theme})

data = res.json()

if(len(data["results"]) > 1):
    print("Ok i got {} jokes about {}!".format(len(data["results"]), theme))
    print("Here's one! : ")
    print(data["results"][random.randint(0, len(data["results"])-1)]["joke"])

elif len(data["results"]) == 1:
    print("Got only one joke! Here it is: ")
    print(data["results"][0]["joke"])

else:
    print("Sorry me haz no joke about {}".format(theme))
