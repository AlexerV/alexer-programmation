package main

import (
	"encoding/json"
	"fmt"
	"math"
	"os"
	"strings"
	"sync"
	"time"
)

// ========== STRUCTURES ==========

type Personne struct {
	Nom   string `json:"nom"`
	Age   int    `json:"age"`
	Ville string `json:"ville"`
	Actif bool   `json:"actif"`
}

type Animal interface {
	Parler() string
	Deplacer() string
}

type Chien struct {
	Nom string
}

func (c Chien) Parler() string {
	return fmt.Sprintf("%s dit: Wouf!", c.Nom)
}

func (c Chien) Deplacer() string {
	return fmt.Sprintf("%s court", c.Nom)
}

type Chat struct {
	Nom string
}

func (c Chat) Parler() string {
	return fmt.Sprintf("%s dit: Miaou!", c.Nom)
}

func (c Chat) Deplacer() string {
	return fmt.Sprintf("%s marche silencieusement", c.Nom)
}

type Rectangle struct {
	Largeur float64
	Hauteur float64
}

func (r Rectangle) Aire() float64 {
	return r.Largeur * r.Hauteur
}

func (r Rectangle) Perimetre() float64 {
	return 2 * (r.Largeur + r.Hauteur)
}

func (r *Rectangle) Doubler() {
	r.Largeur *= 2
	r.Hauteur *= 2
}

// ========== FONCTIONS ==========

func addition(a, b int) int {
	return a + b
}

func division(a, b float64) (float64, error) {
	if b == 0 {
		return 0, fmt.Errorf("division par zéro impossible")
	}
	return a / b, nil
}

func statistiques(nombres []int) (min, max int, moyenne float64) {
	if len(nombres) == 0 {
		return 0, 0, 0
	}

	min, max = nombres[0], nombres[0]
	somme := 0
	for _, n := range nombres {
		if n < min {
			min = n
		}
		if n > max {
			max = n
		}
		somme += n
	}
	moyenne = float64(somme) / float64(len(nombres))
	return
}

func sommeVariadique(nombres ...int) int {
	total := 0
	for _, n := range nombres {
		total += n
	}
	return total
}

func afficherAnimal(a Animal) {
	fmt.Println(a.Parler())
	fmt.Println(a.Deplacer())
}

func travailConcurrent(id int, wg *sync.WaitGroup, resultats chan<- string) {
	defer wg.Done()
	temps := time.Duration(id) * 100 * time.Millisecond
	time.Sleep(temps)
	resultats <- fmt.Sprintf("Travail %d terminé après %v", id, temps)
}

// ========== DÉMONSTRATIONS ==========

func demonstrationVariables() {
	fmt.Println("\n========== VARIABLES ET TYPES ==========")
	var entier int = 42
	var decimal float64 = 3.14159
	var texte string = "Hello Go"
	var vrai bool = true
	nom := "Alexer"
	age := 21
	const Pi = 3.14159
	fmt.Printf("Entier: %d, Décimal: %.2f, Texte: %s, Bool: %t\n", entier, decimal, texte, vrai)
	fmt.Printf("Nom: %s, Age: %d\n", nom, age)
	fmt.Printf("Pi: %.5f\n", Pi)
}

func demonstrationOperations() {
	fmt.Println("\n========== OPÉRATIONS NUMÉRIQUES ==========")
	a, b := 10, 3
	fmt.Printf("Addition: %d + %d = %d\n", a, b, a+b)
	fmt.Printf("Soustraction: %d - %d = %d\n", a, b, a-b)
	fmt.Printf("Multiplication: %d * %d = %d\n", a, b, a*b)
	fmt.Printf("Division entière: %d / %d = %d\n", a, b, a/b)
	fmt.Printf("Modulo: %d %% %d = %d\n", a, b, a%b)
	fmt.Printf("Puissance: %.0f\n", math.Pow(2, 8))
	fmt.Printf("Racine carrée de 16: %.0f\n", math.Sqrt(16))
	fmt.Printf("Arrondi de 3.7: %.0f\n", math.Round(3.7))
}

func demonstrationConditions() {
	fmt.Println("\n========== CONDITIONS ==========")
	note := 15
	if note >= 16 {
		fmt.Println("Mention Très Bien")
	} else if note >= 14 {
		fmt.Println("Mention Bien")
	} else if note >= 12 {
		fmt.Println("Assez Bien")
	} else if note >= 10 {
		fmt.Println("Admis")
	} else {
		fmt.Println("Refusé")
	}

	jour := 3
	switch jour {
	case 1:
		fmt.Println("Lundi")
	case 2:
		fmt.Println("Mardi")
	case 3:
		fmt.Println("Mercredi")
	default:
		fmt.Println("Autre jour")
	}
}

func demonstrationBoucles() {
	fmt.Println("\n========== BOUCLES ==========")
	for i := 0; i < 5; i++ {
		fmt.Printf("%d ", i)
	}
	fmt.Println()
	fruits := []string{"Pomme", "Banane", "Orange"}
	for i, fruit := range fruits {
		fmt.Printf("%d: %s\n", i, fruit)
	}
}

func demonstrationTableauxSlices() {
	fmt.Println("\n========== TABLEAUX ET SLICES ==========")
	nombres := []int{10, 20, 30, 40, 50}
	fmt.Println("Slice:", nombres)
	nombres = append(nombres, 60)
	min, max, moy := statistiques(nombres)
	fmt.Printf("Min=%d Max=%d Moy=%.2f\n", min, max, moy)
}

func demonstrationMaps() {
	fmt.Println("\n========== MAPS ==========")
	ages := map[string]int{"Alexer": 21, "Bob": 30}
	ages["Charlie"] = 35
	for nom, age := range ages {
		fmt.Printf("%s a %d ans\n", nom, age)
	}
}

func demonstrationFonctions() {
	fmt.Println("\n========== FONCTIONS ==========")
	fmt.Println("Addition:", addition(2, 3))
	div, err := division(10, 2)
	if err == nil {
		fmt.Println("Division:", div)
	}
	fmt.Println("Somme variadique:", sommeVariadique(1, 2, 3))
}

func creerCompteur() func() int {
	n := 0
	return func() int {
		n++
		return n
	}
}

func demonstrationStructures() {
	fmt.Println("\n========== STRUCTURES ==========")
	p := Personne{"Alexer", 21, "Paris", true}
	fmt.Printf("%+v\n", p)
}

func demonstrationPointeurs() {
	fmt.Println("\n========== POINTEURS ==========")
	x := 42
	ptr := &x
	fmt.Println("Adresse:", ptr, "Valeur:", *ptr)
	*ptr = 100
	fmt.Println("Nouvelle valeur:", x)
}

func demonstrationMethodes() {
	fmt.Println("\n========== MÉTHODES ==========")
	rect := Rectangle{10, 5}
	fmt.Println("Aire:", rect.Aire())
	rect.Doubler()
	fmt.Println("Aire doublée:", rect.Aire())
}

func demonstrationInterfaces() {
	fmt.Println("\n========== INTERFACES ==========")
	chien := Chien{"Rex"}
	chat := Chat{"Minou"}
	afficherAnimal(chien)
	afficherAnimal(chat)
}

func demonstrationGoroutines() {
	fmt.Println("\n========== GOROUTINES ==========")
	var wg sync.WaitGroup
	resultats := make(chan string, 5)
	for i := 1; i <= 3; i++ {
		wg.Add(1)
		go travailConcurrent(i, &wg, resultats)
	}
	go func() {
		wg.Wait()
		close(resultats)
	}()
	for r := range resultats {
		fmt.Println(r)
	}
}

func demonstrationChannels() {
	fmt.Println("\n========== CHANNELS ==========")
	c := make(chan string, 2)
	c <- "Message 1"
	c <- "Message 2"
	fmt.Println(<-c)
	fmt.Println(<-c)
}

func demonstrationStrings() {
	fmt.Println("\n========== STRINGS ==========")
	texte := "  Hello Go World  "
	fmt.Println("Original:", texte)
	fmt.Println("Trim:", strings.TrimSpace(texte))
	fmt.Println("Upper:", strings.ToUpper(texte))
	fmt.Println("Contains 'Go'?", strings.Contains(texte, "Go"))
	fmt.Println("Split:", strings.Split(texte, " "))
	fmt.Println("Replace:", strings.ReplaceAll(texte, "Go", "Golang"))
}

func demonstrationJSON() {
	fmt.Println("\n========== JSON ==========")
	p := Personne{"Alexer", 21, "Paris", true}
	data, _ := json.MarshalIndent(p, "", "  ")
	fmt.Println(string(data))
	var p2 Personne
	json.Unmarshal(data, &p2)
	fmt.Printf("Décodé: %+v\n", p2)
}

func demonstrationFichiers() {
	fmt.Println("\n========== FICHIERS ==========")
	f, err := os.Create("demo.txt")
	if err != nil {
		fmt.Println("Erreur:", err)
		return
	}
	defer f.Close()
	f.WriteString("Bonjour Go!\n")
	content, _ := os.ReadFile("demo.txt")
	fmt.Println("Contenu lu:", string(content))
	os.Remove("demo.txt")
}

func demonstrationTime() {
	fmt.Println("\n========== TEMPS ==========")
	now := time.Now()
	fmt.Println("Heure actuelle:", now.Format("02/01/2006 15:04:05"))
	fmt.Println("Dans 2h:", now.Add(2*time.Hour))
	fmt.Println("Hier:", now.Add(-24*time.Hour))
}

func demonstrationDeferPanicRecover() {
	fmt.Println("\n========== DEFER / PANIC / RECOVER ==========")
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Récupéré d'une panique:", r)
		}
	}()
	fmt.Println("Avant panic")
	panic("Erreur simulée")
}

// ========== MAIN ==========

func main() {
	demonstrationVariables()
	demonstrationOperations()
	demonstrationConditions()
	demonstrationBoucles()
	demonstrationTableauxSlices()
	demonstrationMaps()
	demonstrationFonctions()
	demonstrationStructures()
	demonstrationPointeurs()
	demonstrationMethodes()
	demonstrationInterfaces()
	demonstrationGoroutines()
	demonstrationChannels()
	demonstrationStrings()
	demonstrationJSON()
	demonstrationFichiers()
	demonstrationTime()
	demonstrationDeferPanicRecover()
}
