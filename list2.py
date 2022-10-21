# Instructions
# Give a definition of the is_leap year function which, given a natural integer n,
# returns the boolean True if n is a leap year, False otherwise.
def is_a_leap_year(year : int) -> bool:
    """Préconditions: year est un entier positif
    returns True if year est bissextile (can be divided by 4, 100 et 400), False otherwise
    """
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

assert is_a_leap_year(2020) == True
assert is_a_leap_year(2000) == True
assert is_a_leap_year(1000) == False
assert is_a_leap_year(1918) == False

# Instructions:
# We now want to know which day of the week falls on any date, for example November 16, 2025.
# Give a definition of the day_of_the_week function which, given three integers corresponding
# respectively to the day, month and year, is greater than or equal to at 1900, returns the
# character string corresponding to the day of the week on which this date falls. Use for this
# the fact that the first of January 1900 fell on a Monday. It is also useful to introduce a
# list containing the number of days in each of the 12 months of the year, as well as a list
# containing the names of the days of the week. It is also useful to call the function of the
# previous question.
def day_of_the_week(day : int, month : int, year : int)-> str:
    """Préconditions: 1<= day <= 31, 1<= month <= 12, year >= 1900
    Days and months define an acceptable date
    """

    nb_days : int = 0
    nb_days_months : List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    a: int
    for a in range(1900, years):
        nb_days = nb_days + 365
        if is_a_leap_year(a):
            nb_days = nb_days + 1
    m: int
    for m in range(0, month - 1):
        nb_days = nb_days + nb_days_months[m]
    if is_a_leap_year(year) and month > 2:
        nb_days = nb_days + 1
    nb_days = nb_days + day - 1
    list_days : List[str] = ['lundi', 'mardi', 'mercredi', 'jeudi', \
                               'vendredi', 'samedi', 'dimanche']
    return list_days[nb_days % 7]

assert day_of_the_week(1,1,2000) == 'saturday'
assert day_of_the_week(11,11,2021) == 'thursday'
assert day_of_the_week(11,11,1918) == 'monday'

#EXERCICE I: Question 1.3
def Dimanche_11_Novembre():
    """"Préconditions: jour est un valeur de type string
    Préconditions: year est compris entre 1919 et 2021
    Préconditions: années est une L de valeurs de type int
    Retourne la L des années depuis 1919 où le 11 novembre est un dimanche
    """
    années = []
    for year in range(1920, 2022):
        jour = day_of_the_week(11, 11, year)
        if jour == "dimanche":
            années.append(year)
    return années

#EXERCICE II: Question 2.1
def intercale(list, e):
    """Préconditions: len(l)>0
    Préconditions: e est un entier
    Préconditions: l est une L de nombres déjà ordonée
    Retourne une liste ordonnée L incluant la valeur e dans la liste L en restant ordonnée
    """
    if len(list)<1 or e > list[-1]:
        list.append(e)
        return list
    for index in range(len(list)):
        if list[index] > e:
            break
    return list[:index] + [e] + list[index:]

# Jeux de tests
assert intercale([1, 2, 2, 4], 0) == [0, 1, 2, 2, 4]
assert intercale([1, 2, 2, 4], 1) == [1, 1, 2, 2, 4]
assert intercale([1, 2, 2, 4], 2) == [1, 2, 2, 2, 4]
assert intercale([1, 2, 2, 4], 3) == [1, 2, 2, 3, 4]
assert intercale([1, 2, 2, 4], 4) == [1, 2, 2, 4, 4]
assert intercale([1, 2, 2, 4], 42) == [1, 2, 2, 4, 42]

#EXERCICE II: Question 2.2
def classe(list):
    result = []
    for i in range(len(list)):
        result = intercale(result, list[i])
    return result

# jeux de tests
assert classe([4, 2, 1, 2]) == [1, 2, 2, 4]

#EXERCICE II: Question 2.3
def toutes_meme_couleur(cartes):
    """
    Retourne True si les cartes de la liste ont la même couleur, False sinon
    """
    if (len(cartes) < 1):
        return True
    couleur = cartes[0][0]
    for i in range(len(cartes)):
        if couleur != cartes[i][0]:
            return False
    return True

#Jeux de tests
assert toutes_meme_couleur([]) == True
assert toutes_meme_couleur([('trefle', 11), ('trefle', 10), \
    ('coeur', 3),('carreau', 11), ('carreau', 12)]) == False
assert toutes_meme_couleur([('trefle', 11), ('trefle', 10), \
    ('trefle', 3), ('trefle', 4), ('trefle', 12)]) == True

#EXERCICE II: Question 2.4
def contient_paire(D, h):
    """
    retournes True si h est une paire dans D, False sinon
    """
    count = 0
    for i in D:
        if i[1] == h:
            count += 1
    return count == 2

# Jeux de tests
assert contient_paire([('trefle', 11), ('trefle', 10), \
    ('coeur', 3), ('carreau', 11), ('carreau', 12)], 11) == True
assert contient_paire([('trefle', 11), ('trefle', 10), \
    ('coeur', 3), ('carreau', 11), ('carreau', 12)], 3) == False
assert contient_paire([('trefle', 11), ('trefle', 10), \
    ('coeur', 3), ('carreau', 11), ('coeur', 11)], 11) == False

#EXERCICE II: Question 2.5
def extrait_couleur(D ,coul):
    """Préconditions: D est une L de tuples de la forme (couleur, valeur)
    Retourne une L de valeurs de la couleur coul
    """
    resultat = []
    for i in D:
        if i[0] == coul:
            resultat.append(i[1])
    return resultat

# Jeux de tests
assert extrait_couleur([('trefle', 11), ('trefle', 10), \
    ('coeur', 3), ('carreau', 11), ('carreau', 12)], 'trefle') == [11, 10]
assert extrait_couleur([('trefle', 11), ('trefle', 10), \
    ('coeur', 3), ('carreau', 11), ('carreau', 12)], 'coeur') == [3]
assert extrait_couleur([('trefle', 11), ('trefle', 10), \
    ('coeur', 3), ('carreau', 11), ('carreau', 12)], 'carreau') == [11, 12]
assert extrait_couleur([('trefle', 11), ('trefle', 10), \
    ('coeur', 3), ('carreau', 11), ('carreau', 12)], 'pique') == []

#EXERCICE II: Question 2.6
def contient_suite(D, h):
    """Préconditions: h est un entier compris entre 1 et 13.
    Retourne True si D contient une suite de cartes de la même couleur et de valeur
    """
    if (len(D) < 1):
        return False
    couleur = D[0][0]
    hauteur_max=[D[0][1]]
    for i in range(1, len(D)):
        hauteur_max.append(D[i][1])
        if couleur != D[i][0]:
            return False
    hauteur_max=classe(hauteur_max)
    return hauteur_max[-1]==h and hauteur_max[0]==h-(len(D)-1)

# Jeux de tests
assert contient_suite([('coeur', 11), ('trefle', 10), \
    ('trefle', 9), ('pique', 8), ('trefle', 12)], 12) == False
assert contient_suite([('trefle', 11), ('trefle', 10), \
    ('trefle', 3), ('trefle', 4), ('trefle', 12)], 12) == False
assert contient_suite([('trefle', 11), ('trefle', 10), \
    ('trefle', 9), ('trefle', 8), ('trefle', 12)], 8) == False
assert contient_suite([('trefle', 11), ('trefle', 10), \
    ('trefle', 9), ('trefle', 8), ('trefle', 12)], 12) == True
