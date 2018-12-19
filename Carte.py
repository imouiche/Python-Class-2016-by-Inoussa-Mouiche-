from random import choice

def ajouterCarte(mesCartes, joueur):
    carte = choice(mesCartes)
    joueur.append(carte)
    mesCartes.remove(carte)

cartes = list(range(10))

carte_joueur_1 = []
carte_joueur_2 = []

while cartes:
    ajouterCarte(cartes, carte_joueur_1)
    ajouterCarte(cartes, carte_joueur_2)

print(carte_joueur_1)
print(carte_joueur_2)
