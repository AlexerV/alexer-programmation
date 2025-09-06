import requests  # Pour effectuer des requêtes HTTP
from bs4 import BeautifulSoup  # Pour analyser les pages HTML
from urllib.parse import urljoin, urlparse  # Pour manipuler les URLs
import re  # Pour les expressions régulières (si nécessaire pour extraire des données spécifiques)

class WebCrawler:
    def __init__(self, base_url):
        """Initialisation du crawler avec l'URL de base et l'ensemble des URLs visitées."""
        self.base_url = base_url  # URL de départ pour le crawl
        self.visited_urls = set()  # Ensemble des URLs visitées (afin d'éviter les visites répétées)

    def is_valid_url(self, url):
        """Vérifie si l'URL est valide (c'est-à-dire qu'elle possède un domaine et un schéma)."""
        parsed = urlparse(url)  # Parse l'URL pour en extraire les différentes parties
        return bool(parsed.netloc) and bool(parsed.scheme)  # Si l'URL contient un domaine et un schéma (http/https)

    def crawl(self, url):
        """Fonction principale pour crawler les pages web."""
        self.visited_urls.add(url)  # Ajouter l'URL actuelle à la liste des URLs visitées
        print(f"Crawling: {url}")  # Affiche l'URL en cours d'exploration

        try:
            # Effectuer une requête GET sur l'URL
            response = requests.get(url)
            response.raise_for_status()  # Si la requête échoue, lever une exception
        except requests.exceptions.RequestException as e:
            # Si une erreur de requête survient (erreur réseau, page introuvable, etc.), afficher l'erreur
            print(f"Failed to retrieve {url}: {e}")
            return  # Sortir de la fonction si la page ne peut pas être récupérée

        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Parcours tous les liens 'a' (ancres) sur la page
        for link in soup.find_all('a', href=True):
            next_url = link.get('href')  # Récupère l'URL du lien
            next_url = urljoin(url, next_url)  # Résout l'URL relative en URL absolue
            next_url = next_url.split('#')[0]  # Supprime les fragments d'URL (#partie)

            # Si l'URL n'a pas encore été visitée et est valide, on continue le crawl
            if next_url not in self.visited_urls and self.is_valid_url(next_url):
                self.crawl(next_url)  # Appel récursif pour crawler cette nouvelle URL

if __name__ == "__main__":
    start_url = 'URL'  # Remplacer 'URL' par l'URL de départ
    crawler = WebCrawler(start_url)  # Crée une instance du crawler
    crawler.crawl(start_url)  # Lance le crawl à partir de l'URL de départ
