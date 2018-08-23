import random
#Daníel Örn Sigurðsson
#21/8/2018

#Strengir
strengur = input("Sláðu inn setningu:")

#Punktur 1
def finnafjoldiOrda(strengur):
    fjoldi = strengur.split()
    return len(fjoldi)
print("Fjöldi orða er:", finnafjoldiOrda(strengur))

#Punktur 2
def finnaFyrstuFimm(strengur):
    fyrstu5 = strengur[0:5]
    return fyrstu5
print("Fyrstu fimm orðin eru:", finnaFyrstuFimm(strengur))

#Punktur 3
def finnaFjogurSeinustu(strengur):
    seinustu4 = strengur[-4:]
    return seinustu4
print("Seinustu fjórir stafirnir eru:", finnaFjogurSeinustu(strengur))

#Punktur 4
def finnaMidju(strengur):
    if len(strengur) %2 !=0:
        lengd = len(strengur)
        stadsetning = int(lengd/2)
        return "Þessi stafur er í miðjuni:", strengur[stadsetning]
    else:
        return "Strengurinn er slétttala og er ekkert í miðjuni"
print(finnaMidju(strengur))

#Punktur 5
def finnaS(strengur):
    nyrstr=" "
    for x in strengur:
        if x=="s" or x=="S" or x == " ":
            nyrstr = nyrstr + x
        else:
            nyrstr = nyrstr + "$"
    return nyrstr
print(finnaS(strengur))

#Listar
rlisti = []
nlisti = []

#Punktur 1
def random100tolur(rlisti):
    for x in range(100):
        randomtolur = random.randrange(34, 69)
        rlisti.append(randomtolur)
    return rlisti
print("100 random tölur á milli 34 og 69:", random100tolur(rlisti))

#Punktur 2
def rodun(rlisti):
    return sorted(rlisti)
print("Röðun listans frá lægstu til hæstu:", rodun(rlisti))

#Punktur 3
def tolur100(rlisti):
    return len(rlisti)
print("Hversu margar tölur eru:", tolur100(rlisti))

def summalistans(rlisti):
    return sum(rlisti)
print("Summa listans:", summalistans(rlisti))

def medaltalListans(rlisti):
    medaltal = summalistans(rlisti) / tolur100(rlisti)
    return medaltal
print(format(medaltalListans(rlisti), ".2f"))

#Punktur 4
def minnstaTala(rlisti):
    mintala = min(rlisti)
    return mintala
print("Minnsta talan í listanum er:", minnstaTala(rlisti))

def haestaTala(rlisti):
    maxtala = max(rlisti)
    return maxtala
print("hæsta talan í listanum er:", haestaTala(rlisti))

#Punktur 5
def yfir4500(rlisti):
    while summalistans(rlisti) > 4500:
        rlisti.pop()
    return rlisti
print(yfir4500(rlisti))

#Punktur 6
nyrlisti = []
def hendaUt5(rlisti, nlisti):
    for x in rlisti:
        if x % 5 != 0:
            nlisti.append(x)
    return nlisti
print("Hent út öllum tölum sem ganga í 5:", hendaUt5(rlisti, nlisti))

#Punktur 7
listi40 = []
def serListi40(rlisti):
    for x in rlisti:
        if x == 40:
            listi40.append(x)
    return listi40
print("Allar 40 tölur:", serListi40(rlisti))

