#include <stdio.h>

int main() {
    char nom[50];
    int age;

    printf("Entrez votre nom : ");
    scanf("%s", nom);

    printf("Entrez votre âge : ");
    scanf("%d", &age);

    printf("Bonjour %s, vous avez %d ans.\n", nom, age);

    if (age >= 18) {
        printf("Vous êtes majeur.\n");
    } else {
        printf("Vous êtes mineur.\n");
    }
    return 0;
}
