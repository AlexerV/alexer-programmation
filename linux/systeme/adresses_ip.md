# Adresse IPv4 et Plages Réservées
Une adresse IPv4 est utilisée pour identifier de manière unique un dispositif sur un réseau informatique. Elle est codée sur 32 bits, soit 4 octets, généralement exprimée sous la forme de quatre nombres décimaux séparés par des points (par exemple, 192.168.1.1).

## Classes d'adresses IPv4
Les adresses IPv4 sont divisées en plusieurs classes selon leur plage d'adresses, et chacune de ces classes est utilisée pour des réseaux de tailles différentes. Ces classes sont définies par les premiers bits de l'adresse.

- Classe A
  - Plage d'adresses : 0.0.0.0 à 127.255.255.255
  - Plage privée : 10.0.0.0 à 10.255.255.255
  - Masque de sous-réseau : 255.0.0.0 (ou /8 en notation CIDR)
  - Utilisation : Réseaux très grands (plus de 16 millions d'adresses).
  - Adresse de réseau : Le premier octet (de 0 à 127) représente la partie réseau. Le reste représente les hôtes dans ce réseau.
- Classe B
  - Plage d'adresses : 128.0.0.0 à 191.255.255.255
  - Plage privée : 172.16.0.0 à 172.31.0.0
  - Masque de sous-réseau : 255.255.0.0 (ou /16 en notation CIDR)
  - Utilisation : Réseaux de taille moyenne (de 65 536 à 1 million d'adresses).
  - Adresse de réseau : Les deux premiers octets représentent la partie réseau. Les deux autres octets représentent les hôtes.
- Classe C
  - Plage d'adresses : 192.0.0.0 à 223.255.255.255
  - Plage privée : 192.168.0.0 à 192.168.255.255
  - Masque de sous-réseau : 255.255.255.0 (ou /24 en notation CIDR)
  - Utilisation : Réseaux de petite taille (jusqu'à 256 adresses).
  - Adresse de réseau : Les trois premiers octets représentent la partie réseau, et le dernier octet représente les hôtes.
- Plage réservée pour le localhost (adresse de boucle locale)
  - Plage d'adresses : 127.0.0.0/8
  - Exemple : 127.0.0.1 est l'adresse locale de l'ordinateur, souvent appelée localhost.
  - Utilisation : Elle est utilisée pour les communications réseau locales sur l'ordinateur, c'est-à-dire pour tester la connectivité interne à la machine.

## Adresses IP privées
Les adresses IP privées sont des adresses réservées pour une utilisation interne dans un réseau local (LAN). Ces adresses ne sont pas routables sur Internet et ne sont donc pas directement accessibles à partir de l'extérieur. Elles sont principalement utilisées dans les réseaux domestiques ou d'entreprise.

Voici les plages réservées pour les adresses IP privées selon les classes :
- Classe A (plage privée) : 10.0.0.0/8 (c'est-à-dire de 10.0.0.0 à 10.255.255.255)
- Classe B (plage privée) : 172.16.0.0/12 (c'est-à-dire de 172.16.0.0 à 172.31.255.255)
- Classe C (plage privée) : 192.168.0.0/16 (c'est-à-dire de 192.168.0.0 à 192.168.255.255)

Ces plages sont utilisées à des fins de réseautage interne, permettant à plusieurs dispositifs de partager une même adresse IP publique (lorsqu'ils accèdent à Internet via un NAT — Network Address Translation).

**Exemple de représentation** :
- Adresse privée de classe A : 10.0.0.1 (exemple typique d'une IP privée dans un grand réseau interne).
- Adresse privée de classe B : 172.16.25.10 (parfait pour des entreprises ou des réseaux ayant plusieurs sous-réseaux).
- Adresse privée de classe C : 192.168.1.5 (très courante dans les réseaux domestiques, comme dans les routeurs Wi-Fi).

## Résumé des plages privées :
| **Classe**   | **Plage d'adresses privées**            | **Masque de sous-réseau** |
| ------------ | --------------------------------------- | ------------------------- |
| **Classe A** | 10.0.0.0 à 10.255.255.255               | /8                        |
| **Classe B** | 172.16.0.0 à 172.31.255.255             | /12                       |
| **Classe C** | 192.168.0.0 à 192.168.255.255           | /16                       |
| **Loopback** | 127.0.0.0 à 127.255.255.255 (localhost) | /8                        |
