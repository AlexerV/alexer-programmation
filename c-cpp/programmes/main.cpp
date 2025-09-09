#include <iostream>
#include <string>
using namespace std;

int main() {
    string nom;
    int age;

    cout << "Entrez votre nom : ";
    cin >> nom;

    cout << "Entrez votre âge : ";
    cin >> age;

    cout << "Bonjour " << nom << ", vous avez " << age << " ans." << endl;

    if (age >= 18) {
        cout << "Vous êtes majeur." << endl;
    } else {
        cout << "Vous êtes mineur." << endl;
    }
    return 0;
}
