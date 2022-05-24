# Import biblioteki wysyłającej maile
import smtplib, ssl

# Dodatkowa bilbioteka potrzebna do utworzenia maili
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from getpass import getpass

phishing_options = {
    1: 'Twoje środki zostają wypłacone',
    2: 'Wymagane jest działanie na Twoim koncie',
    3: 'Zmień swoje hasło',
    4: 'Nieautoryzowane logowanie',
    0: 'Wyjdź',
}

def print_sites(menu):
    for key in menu.keys():
        print (key, '--', menu[key] )

def send_mail(temptype, subj):
    msg = MIMEMultipart()
    msg['Subject'] = subj
    me = 'mikisz1@interia.pl'
    msg['From'] = me
    ofiara = str(input("Podaj email ofiary: "))
    msg['To'] = ofiara
    msg.preamble = 'Login to your account!'


    raport_file = open('email_templates/{}.txt'.format(temptype),'rb')
    message = MIMEText(raport_file.read(), 'plain', 'utf-8')
    raport_file.close()
    msg.attach(message)

    port = 465  # SSL
    #password = input("Podaj hasło do poczty: ")
    print("Podaj hasło do poczty: ")
    password = password = getpass()
    context=ssl.create_default_context()

    s = smtplib.SMTP_SSL("poczta.interia.pl", port=port, context=context)
    wyslano = 1
    try:
        s.login(me, password)
        s.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        print("Błąd logowania do poczty")
        wyslano = 0
    except:
        print("Problem z wysłaniem wiadomości")
        wyslano = 0
    s.quit()
    print("MAIL WYSŁANY!") if wyslano else print("Mail nie wyslany!")


def main():
    while True:
        print_sites(phishing_options)
        menu = ''
        try:
            menu = int(input("Wybierz opcję: "))
        except:
            print('Zły wybór. Wprowadź liczbę...')
        if menu == 1:
            send_mail('balance', 'Utworzono nowe zlecenie wypłaty środków z Twojego konta!')
        elif menu == 2:
            send_mail('account', 'Wymagane jest działanie na Twoim koncie BitFlyer')
        elif menu == 3:
            send_mail('password', 'Obowiązkowa cykliczna zmiana hasła na BitFlyer')
        elif menu == 4:
            send_mail('auth', 'Nieautoryzowane logowanie do serwisu BitFlyer')
        elif menu == 0:
            print("Bye")
            break
        else:
            print('Zły wybór. Wybierz liczbę od 1 do 2...')
