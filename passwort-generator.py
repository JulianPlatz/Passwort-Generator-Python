from colorama import Fore, Style
import random
import string


def print_menu():
    print("--------------------\n"
            "1. Großbuchstaben und Ziffern\n"
            "2. Kleinbuchstaben und Sonderzeichen\n"
            "3. Nur Ziffern\n"
            "4. Alle Buchstaben und Ziffern\n"
            "5. Alle Buchstaben, Ziffern und Sonderzeichen\n"
          "--------------------\n"
            f"1-3 Stellen:{Fore.LIGHTRED_EX} sehr schlecht {Style.RESET_ALL}\n"
            f"4-6 Stellen:{Fore.LIGHTYELLOW_EX} schlecht {Style.RESET_ALL}\n"
            f"7-8 Stellen:{Fore.LIGHTGREEN_EX} gut {Style.RESET_ALL}\n"
            f"9-10 Stellen:{Fore.LIGHTBLUE_EX} sehr gut {Style.RESET_ALL}\n"
            f"11-... Stellen:{Fore.LIGHTMAGENTA_EX} stark {Style.RESET_ALL}\n"
          f"--------------------\n")


def generate_passwort():
    print(f"Damit sie ein {Fore.BLUE} Passwort {Style.RESET_ALL} erstellen können,")

    option = input("wählen sie bitte ihre gewünschte Zahl >> ")
    number_choice = int(input("Wählen sie jetzt bitte noch die Anzahl der Stellen >> "))

    # Dictionary
    characters = {
        "1": string.ascii_uppercase + string.digits,
        "2": string.ascii_lowercase + string.punctuation,
        "3": string.digits,
        "4": string.ascii_uppercase + string.ascii_lowercase + string.digits,
        "5": string.printable,
    }

    passwort = ""

    for i in range(number_choice):
        if option == "1":
            symbol = random.choice(characters["1"])
            passwort += symbol
        elif option == "2":
            symbol = random.choice(characters["2"])
            passwort += symbol
        elif option == "3":
            symbol = random.choice(characters["3"])
            passwort += symbol
        elif option == "4":
            symbol = random.choice(characters["4"])
            passwort += symbol
        elif option == "5":
            symbol = random.choice(characters["5"])
            passwort += symbol
        else:
            print("--------------------\n"
                  f"{Fore.LIGHTRED_EX}Das war leider falsch.{Style.RESET_ALL} "
                  "Wählen sie bitte nur eine Zahl zwischen 1 und 5\n"
                  "--------------------")


    print(f"\nIhr {Fore.BLUE} Passwort {Style.RESET_ALL} lautet: {Fore.RED}" + passwort + f"{Style.RESET_ALL}")

    if number_choice < 4:
        print(str(number_choice) + f" Stellen:{Fore.LIGHTRED_EX} sehr schlecht {Style.RESET_ALL}\n\n")

    elif number_choice < 7:
        print(str(number_choice) + f" Stellen:{Fore.LIGHTYELLOW_EX} schlecht {Style.RESET_ALL}\n\n")

    elif number_choice < 9:
        print(str(number_choice) + f" Stellen:{Fore.LIGHTGREEN_EX} gut {Style.RESET_ALL}\n\n")

    elif number_choice < 11:
        print(str(number_choice) + f" Stellen:{Fore.LIGHTBLUE_EX} seht gut {Style.RESET_ALL}\n\n")

    else:
        print(str(number_choice) + f" Stellen:{Fore.LIGHTMAGENTA_EX} stark {Style.RESET_ALL}\n\n")


# Code-Ablauf
print_menu()

while True:
    generate_passwort()
