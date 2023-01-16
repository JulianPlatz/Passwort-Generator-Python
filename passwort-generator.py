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

    option = input("wählen sie jetzt bitte ihre gewünschte Zahl >> ")
    stellenwahl = int(input("Wählen sie jetzt bitte noch die Anzahl der Stellen >> "))

    zeichen_uppercaseletters_numbers = list(string.ascii_uppercase + string.digits)
    zeichen_lowercaseletters_symboles = list(string.ascii_lowercase + string.punctuation)
    zeichen_numbers = list(string.digits)
    zeichen_letters_numbers = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    zeichen_all = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    stelle = 1
    passwort = ""

    if option == "1":
        while stelle < stellenwahl + 1:
            symbol = random.choice(zeichen_uppercaseletters_numbers)
            stelle = stelle + 1
            passwort = passwort + symbol

    elif option == "2":
        while stelle < stellenwahl + 1:
            symbol = random.choice(zeichen_lowercaseletters_symboles)
            stelle = stelle + 1
            passwort = passwort + symbol

    elif option == "3":
        while stelle < stellenwahl + 1:
            symbol = random.choice(zeichen_numbers)
            stelle = stelle + 1
            passwort = passwort + symbol

    elif option == "4":
        while stelle < stellenwahl + 1:
            symbol = random.choice(zeichen_letters_numbers)
            stelle = stelle + 1
            passwort = passwort + symbol

    elif option == "5":
        while stelle < stellenwahl + 1:
            symbol = random.choice(zeichen_all)
            stelle = stelle + 1
            passwort = passwort + symbol

    else:
        print("--------------------\n"
              f"{Fore.LIGHTRED_EX}Das war leider falsch.{Style.RESET_ALL} "
              "Wählen sie bitte nur eine Zahl zwischen 1 und 5\n"
              "--------------------")
        print(generate_passwort())

    print(f"\nIhr {Fore.BLUE} Passwort {Style.RESET_ALL} lautet: {Fore.RED}" + passwort + f"{Style.RESET_ALL}")

    if stellenwahl < 4:
        print(str(stellenwahl) + f" Stellen:{Fore.LIGHTRED_EX} sehr schlecht {Style.RESET_ALL}\n\n")

    elif stellenwahl < 7:
        print(str(stellenwahl) + f" Stellen:{Fore.LIGHTYELLOW_EX} schlecht {Style.RESET_ALL}\n\n")

    elif stellenwahl < 9:
        print(str(stellenwahl) + f" Stellen:{Fore.LIGHTGREEN_EX} gut {Style.RESET_ALL}\n\n")

    elif stellenwahl < 11:
        print(str(stellenwahl) + f" Stellen:{Fore.LIGHTBLUE_EX} seht gut {Style.RESET_ALL}\n\n")

    else:
        print(str(stellenwahl) + f" Stellen:{Fore.LIGHTMAGENTA_EX} stark {Style.RESET_ALL}\n\n")


# Code-Ablauf
print_menu()

while True:
    generate_passwort()
