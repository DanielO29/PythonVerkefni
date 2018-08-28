import random
#Daníel Örn Sigurðsson
#27/8/2018
#Upprifjun 2 - Dictionaries

dict = {
    "A": "Api",
    "B": "Banani",
    "C": "Cookies",
    "D": "Danni",
    "E": "Elvar",
    "F": "Fáni",
    "G": "Gúrka",
    "H": "Hjól",
    "I": "Ingi",
    "J": "Jól",
    "K": "Kaka",
    "L": "Lárus",
    "M": "Magni",
    "N": "Nammi",
    "O": "Oreo",
}

#Liður 1
def dictid(dict):
    return dict

#Liður 2
def larett(erFyrir):
    for x in erFyrir:
        print(x, "er fyrir", (erFyrir)[x])

#Liður 3
def ordidE(stafurinnE):
    return stafurinnE["E"]

#Liður 4
def breytaH(hid):
    hid["H"] = "Hannes"
    return hid
breytt = breytaH(dict)

#Liður 5
def betraUtlit(dictid):
    for x in dictid:
        print(x, "==>", dictid[x])

#Liður 6
def eyda(dictarinn):
    del dictarinn["C"]
    return dictarinn

#Liður 7 - sjá neðar

#Liður 8 - popitem() tekur random stak úr dictionary-inu.
def takaRandomitem(dict):
    stak = dict.popitem()
    print(dict)
    print("Random stak úr dict:", stak)

#Liður 9 - sjá neðar

#Liður 10
def afritAfDict(dict):
    dict2 = dict.copy()
    return "Afrit af dict:", dict2

#Liður 11
def eydaDicti(dict):
    del(dict)
    print(dict)

#Liður 12
#Dictionary-ið var eytt og ekki hægt að nota það svo það kemur upp villa.

#Liður 13
def toluDict():
    myDict ={}
    for x in range(1,6):
        randomtala = random.randint(1, 6)
        myDict[x] = randomtala
    return myDict

#Prints
print(dictid(dict))
print(larett(dict))
print(ordidE(dict))
print(breytaH(dict))
print(betraUtlit(breytt))
print(eyda(dict))
#Liður 7
print(betraUtlit(dict))
print(takaRandomitem(dict))
#Liður 9
print(betraUtlit(dict))
print(afritAfDict(dict))

#Liður 14
print(toluDict())
#Sýnir tuple pör úr dictionary-inu
print(toluDict().items())
#Sýnir alla lyklana á dictionary
print(toluDict().keys())
#Sýnir öll gildi á dictionary
print(toluDict().values())
#Tekur allt úr dictionary-inu
print(toluDict().clear())

#Liður 11
print(eydaDicti(dict))
