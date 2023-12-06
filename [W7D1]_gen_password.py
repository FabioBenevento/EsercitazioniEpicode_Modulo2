import string
import random
from enum import Enum

LUNGHEZZA_PASSWD_SEMPLICE = 8
LUNGHEZZA_PASSWD_COMPLESSA = 20

def passwd_generator(passwd_len):
    pwd = ""
    for i in range(0,passwd_len):
        pwd += random.choice(string.ascii_letters + string.digits); 
    return pwd

def main():
    lunghezza_password = LUNGHEZZA_PASSWD_SEMPLICE

    while True:
        selezione = int(input("Digita 1 per generare una password semplice, 2 per generare un password complessa:\n"))
        if selezione == 1:
            lunghezza_password = LUNGHEZZA_PASSWD_SEMPLICE
            break  
        elif selezione == 2:
            lunghezza_password = LUNGHEZZA_PASSWD_COMPLESSA
            break
        else:
            print("Valore inserito non valido! Inserire 1 o 2")

    print(passwd_generator(lunghezza_password))

if __name__ == "__main__":
    main()