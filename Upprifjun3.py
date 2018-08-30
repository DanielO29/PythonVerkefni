import math
#Daníel Örn Sigurðsson
#30/8/2018
#Upprifjun 3 - Skráarvinnsla

def veldisTolur():
    with open("veldistolur.txt", 'w', encoding = 'utf-8') as veldistolur:
        for x in range(0, 21):
            utkoma = math.pow(2, x)
            veldistolur.write(" ")
            veldistolur.write(str(utkoma))
print(veldisTolur())

#Liður A

#Liður B

#Liður C

#Liður D

#Liður E
