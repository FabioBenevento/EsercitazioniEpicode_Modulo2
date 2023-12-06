def lunghezza_parole(lista_parole):
    len_parole = []
    if isinstance(lista_parole, list):
        for parola in lista_parole:
            try:
                len_parole.append(len(parola))
            except TypeError as e:
                len_parole.append(-1)    
    else:
        print("L'argomento non è una lista")
    return len_parole


def main():
    parole = ["casa", "giardino", "mansarda", "soffitta", "scantinato", "balcone", "terrazza", "soggiorno", "camera", "stanza"]
    print(lunghezza_parole(parole))

if __name__ == "__main__":
    main()