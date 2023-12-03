PI = 3.14

def calc_perimetro_quadrato(lato):
    return lato * 4;

def calc_perimetro_cerchio(raggio):
    return 2*PI*raggio

def calc_perimetro_rettangolo(base, altezza):
    return 2*(base + altezza)
    
def input_pos_float(messaggio):
    num = 0
    while (num <= 0):
        try:
            num = float(input(messaggio + '> '))
            if(num <= 0):
                print("Inserire un numero reale positivo")
                break
        except ValueError:
            print("Errore: Inserire un numero reale positivo valido.")
    return num

lato = input_pos_float("Inserisci il lato del quadrato:\n")
perimetro_quadrato = calc_perimetro_quadrato(lato)
print(f"Il perimetro del quadrato di lato {lato} è {perimetro_quadrato:.2f}\n")

raggio = input_pos_float("Inserisci il raggio del cerchio:\n")
perimetro_cerchio = calc_perimetro_cerchio(raggio)
print(f"La circonferenza del cerchio di raggio {raggio} è {perimetro_cerchio:.2f}\n")

base = input_pos_float("Inserisci la base del rettangolo:\n")
altezza = input_pos_float("Inserisci l'altezza del rettangolo:\n")
perimetro_rettangolo = calc_perimetro_rettangolo(base, altezza)
print(f"Il perimetro del rettangolo di base {base} e altezza {altezza} è {perimetro_rettangolo:.2f}\n")

