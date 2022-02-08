from pyfiglet import print_figlet
from termcolor import colored


def header():
    print_figlet("VINYLPLASTIC", font="slant")

    print(colored("VinylPlasticSearch v0.1.0a", attrs=["bold"]))
    print("Search CD & LP on every sites automatically")
    print()
