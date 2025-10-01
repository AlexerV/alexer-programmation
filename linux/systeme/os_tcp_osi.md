# Modèles OSI et TCP/IP
Le modèle OSI (Open Systems Interconnection) et le modèle TCP/IP sont deux modèles conceptuels utilisés pour comprendre et décrire comment les données transitent dans un réseau informatique. Voici une explication détaillée des deux modèles :

## Modèle OSI (7 couches)
- Couche 1 : Physique
  - Rôle : Cette couche définit l'encodage des signaux électriques ou optiques, la transmission physique des bits à travers un support de transmission (comme des câbles, fibres optiques, ondes radio), ainsi que les connecteurs, câbles et autres aspects matériels de la communication.
  - Exemples : Ethernet, Wi-Fi, fibre optique, connecteurs RJ45, câblage, etc.

- Couche 2 : Liaison de données
  - Rôle : Elle est responsable de la transmission fiable des données sur un support physique. Elle regroupe les bits reçus de la couche physique en trames et fournit un contrôle d'accès au média, détecte les erreurs de transmission et effectue des corrections.
  - Protocoles : Ethernet, PPP, Wi-Fi, LLC (Logical Link Control), MAC (Media Access Control).
  - Exemple : La couche 2 gère l'adressage MAC des interfaces réseau (adresse MAC unique des cartes réseau).

- Couche 3 : Réseau
  - Rôle : Elle est responsable de l'adressage logique (par exemple, l'adresse IP), du routage des paquets entre différents réseaux et de la sélection des meilleurs chemins pour la transmission de données à travers un inter-réseau.
  - Protocoles : IPv4, IPv6, ICMP, ARP.
  - Exemple : Lorsque vous utilisez un ping pour tester une connexion réseau, le protocole ICMP fonctionne au niveau de la couche 3.

- Couche 4 : Transport
  - Rôle : Cette couche assure le transport des données entre les systèmes de manière fiable (en garantissant l'ordre des paquets, la gestion des erreurs, etc.). Elle segmente les données en paquets et les transmet entre les hôtes. Elle gère également l'établissement et la fermeture des connexions.
  - Protocoles : TCP (Transmission Control Protocol), UDP (User Datagram Protocol).
  - Exemple : Le TCP est responsable de la gestion de la transmission fiable des données, tandis que UDP est utilisé pour des communications plus rapides, mais sans garantie de fiabilité.

- Couche 5 : Session
  - Rôle : Elle gère les sessions de communication entre les applications, garantissant l'ouverture, la gestion et la fermeture de sessions. Elle peut aussi gérer la synchronisation des données entre les applications.
  - Exemples : Protocole NetBIOS, RPC (Remote Procedure Call).

- Couche 6 : Présentation
  - Rôle : Cette couche s'assure que les données sont dans un format compréhensible par l'application. Elle gère la syntaxe et la sémantique des données transmises. Cela inclut le chiffrement, la compression, et la conversion de formats de données.
  - Exemples : SSL/TLS pour le chiffrement, JPEG pour la compression d'images.

- Couche 7 : Application
  - Rôle : Elle fournit des services applicatifs aux utilisateurs, comme l'accès à des fichiers, le transfert de données, ou la communication entre applications. Elle interagit directement avec l'utilisateur ou le logiciel.
  - Exemples : HTTP, FTP, SMTP, DNS, SFTP.

## Modèle TCP/IP (4 couches)
Le modèle TCP/IP est un modèle plus simple que le modèle OSI. Il a été conçu spécifiquement pour les protocoles de communication utilisés sur Internet et est basé sur une structure en 4 couches.

- Accès au réseau (couches 1 et 2 d'OSI)
  - C'est la couche qui correspond aux couches physiques et de liaison de données du modèle OSI. Elle définit la manière dont les données sont transmises sur le réseau local, y compris le câblage, l'interface, et la transmission des données.
  - Exemples : Ethernet, Wi-Fi, ARP, PPP.
- Internet (couche 3 d'OSI)
  - Cette couche correspond à la couche réseau du modèle OSI. Elle gère l'adressage IP, le routage et le passage de données d'un réseau à un autre.
  - Exemples : IP (Internet Protocol), ICMP (Internet Control Message Protocol), IPv4, IPv6.
- Transport (couche 4 d'OSI)
  - La couche de transport du modèle TCP/IP correspond à la couche transport du modèle OSI. Elle gère la communication de bout en bout entre les systèmes et la segmentation des données. Elle fournit également un contrôle de flux et de la fiabilité.
  - Exemples : TCP, UDP.
- Application (couches 5, 6, et 7 d'OSI)
  - La couche application dans TCP/IP englobe les couches session, présentation, et application du modèle OSI. Elle s'occupe des échanges de données entre applications et utilisateurs.
  - Exemples : HTTP, FTP, SMTP, DNS, POP3, IMAP.

## Rôle et Protocoles de la Couche 2 : Liaison de données
La couche 2 (Liaison de données) a pour fonction principale de regrouper les bits en trames et de gérer les erreurs pendant la transmission des données sur le support physique (câble, fibre optique, etc.). Cette couche se charge également de la détection et de la correction des erreurs, ainsi que du contrôle de flux, en garantissant que la quantité de données envoyée ne dépasse pas la capacité de la réception.

**Rôle spécifique :**

- Regroupement en trames : Les données provenant de la couche réseau (couche 3) sont encapsulées dans des trames, qui ajoutent des informations de contrôle telles que l'adresse MAC.
- Contrôle des flux : La couche 2 peut gérer la quantité de données envoyées à un moment donné pour éviter la congestion.
- Détection d'erreurs : En utilisant des mécanismes comme le CRC (Cyclic Redundancy Check), elle peut détecter les erreurs de transmission.

**Protocoles en couche 2 :**

- LLC (Logical Link Control) : Il fournit un contrôle d'accès au média en assurant un contrôle de flux et une gestion des erreurs. Le rôle de LLC est de rendre la couche MAC plus fiable en garantissant la réception correcte des données.
- MAC (Media Access Control) : C'est la partie de la couche de liaison qui gère l'accès au média. Elle est responsable de l'adressage physique (par exemple, adresse MAC des cartes réseau) et de la gestion de la communication entre les différents dispositifs sur le même réseau local.
- PPP (Point-to-Point Protocol) : Protocole utilisé pour établir une connexion directe entre deux périphériques, souvent utilisé dans les connexions réseau via ligne téléphonique ou connexion série.
- Ethernet : Il s'agit du protocole le plus couramment utilisé dans les réseaux locaux (LAN). Ethernet se base sur un mécanisme de communication à diffusion (broadcast), et chaque machine dans un réseau Ethernet a une adresse MAC unique.

**Exemple pratique**

- Ethernet (Protocole en Couche 2) :
  - Une machine envoie une trame Ethernet à une autre machine sur le même réseau local. Cette trame contient l'adresse MAC de la machine émettrice, l'adresse MAC de la machine destinataire et les données à transmettre.
  - L'adresse MAC est unique et sert à identifier de manière locale un appareil dans un réseau physique.
