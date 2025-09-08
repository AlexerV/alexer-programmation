import java.util.Scanner;
import java.util.ArrayList;

public class ExempleComplet {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> noms = new ArrayList<>();

        System.out.println("Combien de noms voulez-vous saisir ?");
        int total = sc.nextInt();
        sc.nextLine(); // pour consommer le retour à la ligne

        // Boucle for : saisir les noms
        for (int i = 0; i < total; i++) {
            System.out.print("Entrez le nom #" + (i + 1) + " : ");
            String nom = sc.nextLine();
            noms.add(nom);
        }

        // Boucle while : vérifier si un nom est dans la liste
        String recherche = "";
        while (!recherche.equalsIgnoreCase("stop")) {
            System.out.print("\nEntrez un nom à rechercher (ou tapez 'stop') : ");
            recherche = sc.nextLine();

            if (noms.contains(recherche)) {
                System.out.println(recherche + " est dans la liste !");
            } else if (!recherche.equalsIgnoreCase("stop")) {
                System.out.println(recherche + " n’est pas dans la liste.");
            }
        }

        // Boucle do...while : menu de tri
        String choix;
        do {
            System.out.println("\n--- MENU ---");
            System.out.println("1. Afficher les noms");
            System.out.println("2. Afficher le nombre total");
            System.out.println("3. Quitter");
            System.out.print("Votre choix : ");
            choix = sc.nextLine();

            switch (choix) {
                case "1":
                    System.out.println("\nListe des noms :");
                    for (String nom : noms) {
                        System.out.println("- " + nom);
                    }
                    break;
                case "2":
                    System.out.println("\nNombre total de noms : " + noms.size());
                    break;
                case "3":
                    System.out.println("\nAu revoir !");
                    break;
                default:
                    System.out.println("Choix invalide.");
            }

        } while (!choix.equals("3"));

        sc.close();
    }
}
