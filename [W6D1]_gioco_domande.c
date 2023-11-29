#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

#define NUM_DOMANDE 10
#define MAX_RISPOSTE 4

// Array domande
char* domande[NUM_DOMANDE] = {
    "Qual è la capitale della Cina?",
    "Chi è l'autore del libro \"Il Nome della Rosa\"?",
    "Chi ha dipinto la \"Notte Stellata\"?",
    "Qual è il più grande oceano sulla Terra?",
    "Qual è l'organo responsabile della produzione dei globuli rossi nel corpo umano?",
    "Chi ha scritto \"Viaggio al centro della Terra\"?",
    "Quale dei seguenti animali è un mammifero marino?",
    "Quale delle seguenti lingue non utilizza l'alfabeto latino?",
    "Quale grande fiume attraversa l'Antico Egitto?",
    "Qual è il metallo più pesante?",
};



// Array risposte
char* risposte[NUM_DOMANDE][MAX_RISPOSTE] = {
    {"Pechino", "Hong Kong", "Bangkok", "Shanghai"},
    {"Italo Calvino", "Giovanni Verga", "Umberto Eco", "Luigi Pirandello"},
    {"Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo Buonarroti"},
    {"Oceano Indiano", "Oceano Atlantico", "Oceano Artico", "Oceano Pacifico"},
    {"Milza", "Rene", "Midollo osseo", "Fegato"},
    {"Jules Verne", "Antoine de Saint-Exupéry", "Mark Twain", "Victor Hugo"},
    {"Squalo", "Balena", "Murena", "Anguilla" },
    {"Spagnolo", "Tedesco", "Greco", "Arabo"},
    {"Tigri", "Nilo", "Eufrate", "Gange" },
    {"Oro", "Piombo", "Uranio", "Platino"},
};


// Array risposte esatte
char risposte_esatte[NUM_DOMANDE] = {'A', 'C', 'A', 'D', 'C', 'A', 'B', 'D', 'B', 'C'};

void intestazione() {
    printf("**********************************\n");
    printf("*         Benvenuto a            *\n");
    printf("*  Chi vuol essere poveraccio    *\n");
    printf("**********************************\n\n");
}

void presentazione() {
    printf("Scegli cosa vuoi fare:\n");
    printf("A) Iniziare una nuova partita\n");
    printf("B) Uscire dal gioco\n");
}

int esci() {
    printf("Grazie per aver giocato!\n");
    return 0;
}

void prepara_domanda(int indice_domanda) {
    char lettera_iniziale = 'A';
    
    printf("%s\n", domande[indice_domanda]);
    
    for(int i=0; i < MAX_RISPOSTE; i++) {
        printf("%c) ", lettera_iniziale + i);
        printf("%s\n", risposte[indice_domanda][i]);
    }
}

int main() {
    char scelta;
    
    intestazione();

    while(true) {
        int punteggio = 0;
        presentazione();
        scanf(" %c", &scelta);
    
        if(toupper(scelta) == 'B') {
            break;
        }
    
        char nome[15];
        printf("Inserisci il tuo nome: ");
        scanf("%s", nome);
        printf("Ciao, %s! Cominciamo la partita.\n\n", nome);
    
        for(int i=0; i < NUM_DOMANDE; i++) {
            prepara_domanda(i);
            char risposta;
            scanf(" %c", &risposta);
    
            // Valuta la risposta
            if (toupper(risposta) == risposte_esatte[i]) {
                punteggio++;
                printf("Risposta corretta!\n\n");
            } else {
                printf("Risposta sbagliata!\n\n");
            }
        } 
    
        printf("Il tuo punteggio finale è: %d\n\n", punteggio);
    };
    
    return esci();
}
