#!/usr/bin/python3

import os
import hackWallet
import preparePhishing
import prepareEmail

# Wiadomość powitalna
welcome_message = """#################################################################
##### SUDI - Narzędzie do testów bezpieczeństwa kryptowalut #####
#################################################################"""

# Słownik z opcjami menu
menu_options1 = {
    1: 'Utwórz phishingową stronę do logowania',
    2: 'Wyślij phishingowy mail do ofiary',
    0: 'Exit',
}

# Słownik z opcjami głównego menu
menu_options = {
    1: 'Phishing - tworzenie strony i email',
    2: 'Atak brute-force na portfel',
    0: 'Exit',
}

# Wyświetlanie opcji menu
def print_menu(menu_opt):
    for key in menu_opt.keys():
        print (key, '--', menu_opt[key] )

# Funkcja uruchamiająca pierwsze narzędzie
def option1():
    while(True):
        initialization()
        print_menu(menu_options1)
        option = ''
        try:
            option = int(input('Wybierz opcję: '))
        except:
            print('Zły wybór. Wprowadź liczbę...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option11()
        elif option == 2:
            option12()
        elif option == 0:
            print('Narazie!')
            break
        else:
            print('Zły wybór. Wybierz liczbę od 1 do 2...')


# Funkcja uruchamiająca drugie narzędzie
def option2():
    #os.system("python3 hackBTCwallet.py")
    hackWallet.bruteForceWallet()

# Funkcja uruchamiająca trzecie narzędzie
def option11():
     preparePhishing.phishing_site()

# Funkcja uruchamiająca czwarte narzędzie
def option12():
     print('Przygotowanie phishingowego maila...')
     prepareEmail.main()

# Funkcja uruchamiająca informację powitalną
def initialization():
    print(welcome_message)

# Główna funkcja main
if __name__=='__main__':
    os.system('clear')
    while(True):
        initialization()
        print_menu(menu_options)
        option = ''
        try:
            option = int(input('Wybierz opcję: '))
        except:
            print('Zły wybór. Wprowadź liczbę...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 0:
            print('Narazie!')
            exit()
        else:
            print('Zły wybór. Wybierz liczbę od 1 do 2...')


