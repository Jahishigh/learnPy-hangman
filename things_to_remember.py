# Pour importer des librairies (ou module) :
# Chercher la librairie math et importer toute la librairie avec *
from math import *
# import os

# Déclarer une variable
# On peut y mettre ce qu'on veut, string, int, array, boolean...
nom_de_ma_variable = "string"
# Mettre directement une varible dans une fonction :
variable_print = "Hello"
print(variable_print)

# print une string avec une variable, utiliser +
print("String " + nom_de_ma_variable + "\n")

# ----------------------STRING--------------------------

# Toujours entourer une string avec ""
# Pour créer une nouvelle ligne dans une string utiliser \n
"String\nString\n"
# Utiliser des fonctions avec les string, exemple :
string_exemple = "Hello World\n"
# Pour passer la string en lower case :
string_exemple.lower()
# Pour passer la string en upper case :
string_exemple.upper()
# Check si une string est quelque chose, ici upper case (renvoie True or False)
string_exemple.isupper()
# Combinaison de fonctions, ici passer la string en upper puis check si elle est (renvoie True)
string_exemple.upper().isupper()
# Trouver la longueur d'une string (renvoie 12)
len(string_exemple)
# Voir quel caractère à une position précise (renvoie H)
# Ne pas oublier [] est un tableau et les tableau en python commence par 0
print(string_exemple[0])
# Trouver la position d'un charactère dans la string avec index (renvoie 0 pour la première position)
# Dans index, il faut préciser un paramètre
string_exemple.index("H")
# Index peut être utiliser avec un mot complet (renvoie 6, la position du premier charactère du mot complet
string_exemple.index("Wor")
# Remplacer un charactère par un autre (avec 2 paramètres) :
string_exemple.replace("World", "Planet Earth")
# Pour créer une string avec plusieurs lignes, utiliser ''' '''
multi_line_string = ''' Je suis une string
avec plusieurs
lignes
'''

print(multi_line_string)

# ----------------------NUMBERS--------------------------
# Un nombre s'écrit sans ""
print(2)
# On peut utiliser des nombres négatif ou décimal :
print(-2)
print(2.35)
# Faire des opérations basique :
print(1 + 1)
print(1 - 1)
print(2 * 3)
print(4 / 2)
# Utiliser des parenthèses pour l'ordre d'opération
print(3 * (4 + 5))
# Modulus : donne le reste (donc 1 ici)
print(10 % 3)
# Convertir un nombre en string :
# Si on veut print un nombre avec une string, il faut changer le nombre en string sinon tout explose
num_to_string = 5
print(str(num_to_string) + " est une string maintenant")
# Récuperer la valeur absolue
print(abs(num_to_string))
# Récuper la puissance d'un nombre (2 paramètrs, le nombre et la puissance voulue (ici 4^2 = 16):
print(pow(4, 2))
# Return le nombre le plus grand (min fait l'inverse) ici renvoie 6
print(max(4, 6))
# Arrondir un nombre (renvoie 4 ici) :
print(round(3.7))
# Enlever la décimal (ici renvoie 3)
print(floor(3.7))
# Toujours arrondir au supérieur (ici renvoie 4)
print(ceil(3.2))
# Return la racine carré (ici 6)
print(sqrt(36))
# Il y en a bien plus avec le module math


# ----------------------INPUT--------------------------
# Pour récupérer ce que l'utilisateur écrit dans une variable
# Le paramètre de l'input est le texte pour l'utilisateur
input_du_user = input("Entrer quelque chose: ")
# Une fois qu'on a récupéré l'input dans une variable, on peut le print ou s'en servir pour autre chose
print("Vous avez écrit " + input_du_user)
# Si on veut que l'user entre un chiffre, on doit le convertir car input return un string de base
# Pour un nombre entier utiliser int, pour un décimal (comprend aussi les entiers) utiliser float
num1 = input("Entrer un nombre entier: ")
num2 = input("Entrer un nombre décimal ou entier: ")
print(int(num1) + float(num2))

# ----------------------LIST AND 2D LIST--------------------------
# Pour déclarer un tableau :
# On peut mettre ce qu'on veut dans un tableau
array = ["String", 5, True, input_du_user]
# Pour afficher tous le tableau :
print(array)
# Pour afficher une position précise dans le tableau (ici 5):
print(array[1])
# Pour afficher une position en partant de la fin (noter que la fin commence à -1) :
print(array[-1])
# Pour afficher à partir d'une position jusqu'à la fin :
print(array[1:])
# Pour afficher à partir d'une position jusqu'à une autre (n'inclue pas la position d'arrivé :
print(array[1:3])
# Pour modifier une valeur du tableau :
array[1] = "Nouvelle string"
print(array)
# Ajouter un tableau à la fin d'un autre tableau
second_array = ["Second Tableau", 42, False]
array.extend(second_array)
print(array)
# Ajouter un élément à la fin de la liste
array.append("Nouvel élément")
# Ajouter un élément à une position précise (ce qui pousse les autres de 1 place
array.insert(1, "Element à la 2ième place")
# Enlever un élément du tableau
array.remove("Nouvelle string")
# Enlever le dernier élément du tableau
array.pop()
# Donne la position dans le tableau de l'élément en paramètre
array.index("String")
# Donne le nombre de fois que l'élément apparait dans le tableau
array.count("String")
# Ranger la liste dans l'ordre alphabétique ou croissant si c'est des int
array_to_sort = [3, 2, 8, 7]
array_to_sort.sort()
# Inverser l'ordre de la liste
array.reverse()
# Faire une copie d'une liste dans un nouveau tableau
copie_de_array = array.copy()
# Vider le tableau
array.clear()
# Pour créer une liste 2D, créer un tableau et mettez y plus de tableau pour un max de tableau
# Ceci crée donc une tableau où l'on voit les lignes et les colonnes, ce qui va servir à appeler les éléments
tableau_en_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Ici, on print l'élément ligne 0 colonne 0, donc l'élément 1
print(tableau_en_2d[0][0])

# ----------------------TUPLES--------------------------
# Les tuples sont dans listes dans lesquelles on ne peut rien modifier
# Ni les éléments, ni l'ordre, rien
new_tuples = ("Hello", 25, False)
# Pour afficher un élément du tuple
print(new_tuples[0])
# Créer une liste de tuples
liste_de_tuples = [(1, 2), (3, 4), (5, 6)]


# ----------------------FONCTION--------------------------
# Permet de mettre des bouts de code dans une fonction, et appeler cette fonctions plusieurs fois
# sans devoir reécrire tous le code à chaque fois
# Pour créer une fonction :
# les parenthèses après le nom de la fonction sont pour passer des paramètres
# Dans cette fonction, je dois donner 2 paramètres : un nom et un age, sinon la fonction ne fonctionne pas
# Le nom des paramètres n'a pas d'importance à part la clareté du code
def nom_de_la_fonction(nom, age):
    print("Bonjour " + nom + ", tu as " + str(age) + "ans")


nom_de_la_fonction("Maxence", 28)


# RETURN permet à la fonction de donner directement une information en retour à utiliser dans le code
# Ici, la fonction return 8
def return_cest_pratique(num):
    return num + num


print(return_cest_pratique(4))
# IMPORTANT : Le code écrit après return dans une fonction n'est pas pris en commpte
# return fini la fonction et en sort

# ----------------------IF ELiF ELSE--------------------------
# Permet de donner des conditions au code pour effectuer un code à un certain moment ou dans certain cas
# Ici, if vérifie si la variable cest_vrai est True, si c'est le cas, le print s'effectue
# Si cest_vrai est False, alors le code entre dans le else
cest_vrai = True
if cest_vrai:
    print("C'était bien vrai")
else:
    print("C'était pas vrai")
# if permet de vérifier plusieurs condition à la fois
# Ici or permet de vérifier si l'un ou l'autre est True, alors le code entre dans le if
cest_vrai = True
cest_beau = True
if cest_vrai or cest_beau:
    print("C'était bien vrai et beau")
# Ici and permet de vérifier si les deux sont True
cest_vrai = True
cest_beau = True
if cest_vrai and cest_beau:
    print("C'était bien vrai et beau")
# elif permet d'ajouter un nouveau cas de condition possible après un premier if
# not(variable) permet de vérifier si une varible est False
cest_vrai = True
cest_beau = False
if cest_vrai and cest_beau:
    print("C'était bien vrai et beau")
elif cest_vrai and not cest_beau:
    print("C'est vrai mais c'est pas beau")
# if permet aussi de comparer des chiffres par exemple
# Type de comparaison : > < >= <= != ==
if 5 < 6:
    print("C'était évident")
# Ou comparer des string
if "ceci" == "ceci":
    print("Ceci est bien ceci")

# ----------------------DICTIONARY--------------------------
# Un dictionary permet d'associer une valeur à une autre
# Par exemple une string et une string, ou une string et un int
mon_dico = {
    "Jan": "Janvier",
    "Feb": "Fevrier",
    "Mar": "Mars",
    "Num": 5,
    10: "Dix"
}
print(mon_dico["Feb"])
print(mon_dico["Num"])
# On peut aussi utiliser une fonction pour appeler une value du dico :
print(mon_dico.get("Jan"))
# Si la value n'est pas dans le dico, on peut fournir une valeur de base en parametre pour prévenir de l'erreur
print(mon_dico.get("Avr", "C'est pas dans le dico"))

# ----------------------WHILE--------------------------
# While permet de boucler le code tant que sa condition n'est pas completé
# Ici, tant que i reste inférieur à 10, le code continue
# Une fois la condition rempli, le code sort du while et print le message non indenté
i = 1
while i <= 10:
    print(i)
    i += 1
print("while est fini")

# ----------------------FOR LOOP--------------------------
# for prend une condition en variable, à chaque passage de la loop la variable va changer jusqu'à arriver à la condition
# la variable après le for peut avoir n'importe quel nom, c'est la condition final qui compte
for letter in "Hello":
    print(letter)

list_de_value = [1, 2, 3]
for value_in_list in list_de_value:
    print(value_in_list)

for chiffre in range(6):
    print(chiffre)
# Si on reprend l'exemple de notre liste 2d (voir plus haut)
# Ici on affiche tous le tableau 2d
for ligne in tableau_en_2d:
    print(ligne)
# Ici on print chaque élément individuelement
for ligne in tableau_en_2d:
    for colonne in ligne:
        print(colonne)

# ----------------------TRY EXCEPT--------------------------
# Ceci permet d'attraper une erreur pour ne pas qu'elle s'affiche et qu'elle bloque notre code
# A la place, on peut s'en occuper et lui donner quelque chose à faire si une erreur arrive
# Dans l'exemple, si on entre autre chose qu'un nombre entier, au lieu de crash le code, on va renvoyer une string
# Pour ce code, on pourrait mettre tout ça dans un while pour donner une nouvelle chance d'entrer un nombre entier
# IMPORTANT : dans le except, il faut préciser le type d'erreur qu'on veut attraper
# Si on ne met rien, il va attraper toutes les erreurs, mais mettre toujours le même message
# Pour afficher le message d'erreur, ajouter as err (qu'importe le nom, pas forcément err) et print err
try:
    nombre = int(input("Entrer un nombre entier"))
    print(nombre)
except ValueError as err:
    print("C'est pas un nombre entier ça")
    print(err)

# ----------------------LIRE UN FICHIER--------------------------
# Pour lire un fichier, on l'ouvre, on donne le nom du fichier dans une string
# Puis on choisie un mode de lecture :
# r pour seulement lire, w pour modifier le fichier, a pour ajouter quelque chose à la fin du fichier
# r+ permet de lire et écrire
# IMPORTANT : Penser à toujours fermer le fichier
# ton_fichier.readable renvoie un boolean pour vérifier si ton fichier est bien lisible
# ton_fichier.read affiche le contenu de ton fichier
# ton_fichier.readline lis la première ligne de ton fichier, puis déplace le curseur à la ligne suivante dans le fichier
# Du coup si tu refais un .readline, tu lis la ligne suivante, donc la deuxième
# ton_fichier.readlines mets toutes les lignes de ton fichier dans un tableau
# Donc en second paramètre tu peux indiquer la position dans le tableau que tu veux afficher (ici la ligne 1)
# Avec une boucle for, tu peux donc afficher toutes les lignes : for ligne in ton_fichier.readlines()
try:
    ton_fichier = open("nom_de_ton_fichier", "r")
    if ton_fichier.readable() is True:
        print(ton_fichier.read)
        print(ton_fichier.readline())
        print(ton_fichier.readlines()[1])
    ton_fichier.close()
except FileNotFoundError:
    print("Evidemment, le fichier n'existe pas hein")

# ----------------------ECRIRE DANS UN FICHIER--------------------------
# Pour écrire dans le fichier, choisir le bon mode déjà, ici par exemple a pour ajouter à la fin
# ton.fichier.write permet d'écrire dans le fichier (selon le mode choisi)
# Attention, si on relance le code ci dessous, le string ne passera pas à la ligne suivante, donc ajouter un \n au début
# Bien penser à mettre la nature de ton fichier (.txt, .html etc..)
try:
    ton_fichier = open("nom_de_ton_fichier", "a")
    ton_fichier.write("String qui s'ajoute à la fin du fichier")
    ton_fichier.close()
except FileNotFoundError:
    print("Evidemment, le fichier n'existe pas hein")
except PermissionError:
    print("y'a pleins d'erreurs comme y'a pas de fichier")
# Ici on utilise le mode w, ça va donc supprimer tout ce qui a sur le fichier et ajouter que cette ligne
# Avec le mode w, si le nom de ton fichier n'existe pas, python va créer le fichier pour toi
# Par exemple, open("index.html", "w") ton_fichier.write("<h1>Titre</h1>") Va créer une page html et un titre dedans
# ATTENTION Si tu run le code, il va te créer le fichier
try:
    ton_fichier = open("nom_de_ton_fichier.txt", "w")
    ton_fichier.write("oups j'ai tout supprimé")
    ton_fichier.close()
except FileNotFoundError:
    print("Evidemment, le fichier n'existe pas hein")
except PermissionError:
    print("y'a pleins d'erreurs comme y'a pas de fichier")

# Pour supprimer un fichier, il faut import os
# os.remove("nom_de_ton_fichier.txt")
# os.remove("nom_de_ton_fichier")

# ----------------------CLASS ET OBJET--------------------------
# Crée une classe permet de définir autre chose qu'une string ou un boleean mais de représenter un 'objet'
# Lorsqu'on crée une class, un crée une def qui permet de donner des paramètres relié à cet objet
# __init__ sert à recevoir des paramètres et les stocker dans les paramètre donné dans la def
# self.ton_paramètre sert à attribuer à ton objet les paramètres que tu as donné
# Dans l'exemple, en passant un string avec le nom, on le recois dans init puis on l'attribut à l'objet avec self
# IMPORTANT, si on crée la class dans un autre fichier, ce qui est recommandé, penser à l'importer
# Par exemple ici si la class est dans un fichier nommé animals.py : from animals import pet
# Dans le code, on peut appeler la classe en donnant une variable, puis en appelant la class, et donner les paramètres
# Une fois l'objet crée, on peut maintenant facilement accéder à toutes ses informations comme dans le print ci dessous
# On peut aussi def des fonctions que l'on peut appeler avec cet objet, comme ici speak
# A savoir que l'on est pas obligé d'init des paramètre dans la class, on peut juste mettre des fonctions à executer
# Dans une class, on peut aussi avoir un attribut sans le demander en parametre pour l'ajouter plus tard par un autre
# moyens, ici self.is_true n'est pas demandé dans les paramètre de init, mais on pourra l'ajouter plus tard en faisant
# par exemple : self.is_true = False
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_true = True
    def speak(self):
        print("What am i ?")
    def show(self):
        print("Je suis " + self.name + " et j'ai " + str(self.age) + "ans")

p = Pet("Tim", 19)
p.speak()

# Pour faire hériter une class de ce que possède une autre class, ajouter le nom de la class entre parenthèse
# Ici, Cat peut utiliser les paramètre de Pet car il a hésité de sa class, et peut utiliser un fonction exclusive
# qui vient de sa propre class speak("Meow")
class Cat(Pet):
    def speak(self):
        print("Meow")

c = Cat("Nougat", 2)
c.show()
c.speak()

# Si on ne défini rien dans une nouvelle class enfant, on peut mettre pass, ce qui va juste prendre les attribut de sa
# class parente
class Fish(Pet):
    pass

f = Fish("Nemo", 3)
f.show()
f.speak()

# Si on veut rajouter une paramètre à entrer dans init qui n'est pas dans la class parente
# super() appel la class parente, donc ici on appel name et age de Pet et on y ajoute color pour cette class uniquement
class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("Bark")

    def show(self):
        print("Je suis " + self.name + ", j'ai " + str(self.age) + "ans et je suis " + self.color)

d = Dog("Rex", 5, "marron")
d.show()
d.speak()

# Attribut de class
# Ici, number_of_people est un attribut de class, était en dehors de l'init, il ne change pas à chaque objet mais est
# attribué à la class entière
# Du coup, à chaque nouvel objet, je peux incrémenter cette attribut, et l'appeler
class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people)

# Les class method sont des fonctions aggissent sur la class entière et non sur un objet
# Ici, pour calculer le nombre de personne, on appel la fonction add_person à l'intérieur de l'init pour incrémenter
# nb_of_ppl puis on print nb_ppl qui return notre attribut de class
class ppl:
    nb_of_ppl = 0
    def __init__(self, name):
        self.name = name
        ppl.add_person()
    @classmethod
    def nb_ppl(cls):
        return cls.nb_of_ppl
    @classmethod
    def add_person(cls):
        cls.nb_of_ppl += 1

Pa = ppl("Jean")
Pb = ppl("Marc")
print(ppl.nb_ppl())

# Les static method sont des fonctions dans des class qui ne prennent aucun attribut, ni de self ni de cls
# Elle sont dans la class mais n'ont accès à rien et peuvent juste être appelé sans rien changer à la class et ses init
# On les utilise souvent pour ranger des fonctions qui ont une utilité similaire pour les appeler plus facilement
class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))
Math.pr()

# ----------------------FONCTIONS UTILES--------------------------
# type() donne le type de l'élément donné, ici l'exemple renvoie str
print(type("Hello"))

#fonction pour passer une string dans un array
def convert_to_array(string):
    array = []
    array[:0]=string
    return array

def convert_to_string(array):
    return ', '.join(array)
