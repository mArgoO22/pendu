import random

def choisir_mot():
    mots = ["baccalaureat", "abracadabra", "francophile", "pandemonium", "chlorophylle","metallurgie", "metamorphose", "montgolfiere", "kaleidoscope", "conquistador","rhododendron", "qualification"," protozoaire", "quadrilatere", "zygomatique", "sorcellerie", "acrostiche","apocalypse", "attraction", "aventurier", "bouillotte", "citrouille"," controverse", "coquelicot", "dissimuler", "flibustier", "forestiere","grenouille", "impossible","labyrinthe", "maharadjah", "prudemment", "quadriceps", "subjective","ane", "axe", "bip", "car", "col"," coq", "cor", "cou", "cri", "gag","gel", "jus","net", "nul", "val", "ski", "sot","tic", "abajoues", "", "adaptateur", "dauphin", "rateau","metal", "malheurs", "metier", "interrgogatif", "adresse","electronique", "administrations"," adverbe", "pacifique", "paléotholongie", "programmer", "parasite","apocalypse", "moulin", "quatre", "querelles", "quantifier","impenetrable", "pharmacie", "puerile", "debrouilliard", "dos","decelere", "ebranler","hallucination", "haillons", "harcelement", "hopital", "radio","raideur", "rafraichir", "raisins", "architecture", "racines"," latéralement", "cicatrices", "cuisine", "simplifier", "sacrifier" ]

    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache

def deviner_mot(mot):
    lettres_trouvees = set()
    nb_chances = 11

    while nb_chances > 0:
        print("\nMot à deviner :", afficher_mot_cache(mot, lettres_trouvees))
        print("Chances restantes :", nb_chances)

        lettre = input("Entrez une lettre : ").lower()

        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre.")
            continue

        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre.")
            continue

        lettres_trouvees.add(lettre)

        if lettre not in mot:
            print("Cette lettre n'est pas dans le mot.")
            nb_chances -= 1

        if set(mot).issubset(lettres_trouvees):
            print("\nFélicitations ! Vous avez deviné le mot :", mot)
            break

    if nb_chances == 0:
        print("\nDommage, essayez une nouvelle fois. Le mot était :", mot)

def jouer_pendu():
    print("Bienvenue, voulez-vous jouer au jeu du pendu ?")
    mot = choisir_mot()
    deviner_mot(mot)
    rejouer = input("\nVoulez-vous faire une nouvelle partie ? (oui/non) : ")
    if rejouer.lower() == "oui":
        jouer_pendu()
    else:
        print("Merci d'avoir joué et tchao !")

# Lancement du jeu
jouer_pendu()