#include <stdio.h>
#include <math.h>

int main() {
    float input, area_quadrato, area_cerchio, area_triangolo;
    printf("Inserisci un numero reale:\n");
    scanf("%f", &input);
    area_quadrato = pow(input, 2);
    area_cerchio = M_PI * pow(input, 2);
    area_triangolo = (sqrt(3) / 4) * pow(input, 2);
    printf("L'area del quadrato di lato %.3f è:' %.3f:\n", input, area_quadrato);
    printf("L'area del cerchio di diametro %.3f è:' %.3f:\n", input, area_cerchio);
    printf("L'area del triangolo equilatero di lato %.3f è:' %.3f:\n", input, area_triangolo);
    return 0;
}
