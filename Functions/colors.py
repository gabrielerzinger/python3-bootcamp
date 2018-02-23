import termcolor
import pyfiglet


text = termcolor.colored(pyfiglet.figlet_format(
    "Star Wars"), color="magenta", attrs=["blink"])
print(text)
