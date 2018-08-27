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
print(dictid(dict))

#Liður 2
def larett(erFyrir):
    for x in erFyrir:
        print(x, "er fyrir", (erFyrir)[x])
print(larett(dict))

#Liður 3
def ordidE(stafurinnE):
    return stafurinnE["E"]
print(ordidE(dict))

#Liður 4
def breytaH(hid):
    hid["H"] = "Hannes"
    return hid
print(breytaH(dict))
breytt = breytaH(dict)

#Liður 5
def betraUtlit(dictid):
    for x in dictid:
        print(x, "==>", dictid[x])
print(betraUtlit(breytt))

#Liður 6
def eyda(dictarinn):
    del dictarinn["C"]
    return dictarinn
print(eyda(dict))

#Liður 7
print(betraUtlit(dict))

#Liður 8
