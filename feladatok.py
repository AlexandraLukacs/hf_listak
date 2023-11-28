# Nézzük meg a lottószámok átlagát
def lotto(lista):
    print("Lottó")
    osztas: int= 0
    atlag: int= 0
    for i in range(0, len(lista), 1):
        osztas += lista[i]
        atlag += 1
    return (osztas / atlag)


# Hány 50-nél nagyobb szám van közte?
def nagyobb(lista):
    print("50-nél nagyobb")
    szam: int= 0
    for i in range(0, len(lista), 1):
        if lista[i] >= 50:
            szam += 1
    return szam


# Melyik a legnagyobb szám?
def max(lista):
    print("Legnagyobb szám")
    max: int= lista[0]
    for i in range(0, len(lista), 1):
        if lista[i] > max:
            max = lista[i]
    return max


# Hányadiknak generáltuk a legnagyobb számot?
def hanyadik(lista):
    print("Hányadik hely")
    hely: int= 0
    max: int= lista[0]
    for i in range(0, len(lista), 1):
        if lista[i] > max:
            if max == lista[i]:
                hely = i
    return hely + 1


# Melyik a legkisebb szám?
def min(lista):
     print("Legkisebb szám")
     min: int= lista[0]
     for i in range(0, len(lista), 1):
        if lista[i] < min:
            min = lista[i]
     return min


# A legkisebb és a legnagyobb szám közti különbség?
def max_min(lista):
    print("Különbség")
    max: int= lista[0]
    min: int= lista[0]
    for i in range(0, len(lista), 1):
        if lista[i] > max:
            max = lista[i]
        elif lista[i] < min:
            min = lista[i]
    return (max - min)


# Kérj be a felhasználótól egy számot, és döntsd el, hogy szerepel-e a szám a húzott számok között?
def bekeres(lista):
    print("Bekérés")
    szam: int= int(input("Adjon meg egy lottó számot: "))
    if szam in lista:
        print(f"A {szam} szám szerepel a húzott számok között!")
    else:
        print(f"A {szam} szám nem szerepel a húzott számok között!")


