"""

na dzisiaj wystarczy int, float i string (nie ma double'a)
#instrukcja wejscia - input("podaj wage")
instrukcja input zwraca najpierw zawsze string, ale mozna zmieniac typy zmiennej w trakcie
b = int (a)
w pythonie ** - to potega (jest tez pow w bibliotece math)
print(2**5)    -    dwa do piatej, czyli 32
nie ma inkkrementacji i dekrementacji (++ , czy --), trzeba sobie radzic np poprzez a+1

instrukcje warunkowe i petle:

petla for jest bardzo ograniczona, iteruje klasycznie

if warunek:
    instrukcja
    instrukcja
else:               (lub elif war2:)
    instr
    instr

operatory logiczne: and, or, not    (podwojny and jest inny w pythonie a javie, czy c#)
nawiasy do kolejnosci wykonywania dzialan

while warunek:
    instr

for iterator in zestaw:


for znak in range(10):          (zwroci liczbe od 0 do 9)
    print (i**2)

Zadania 1 do 10 korzystamy tylko z typow prostych
"""

"""
def zadanie1():
    wzrost = float(input("Podaj swoj wzrost (w metrach) "))
    waga = float(input("Podaj swoja wage (w kg) "))
    if waga < 0 or wzrost <0:
        print ("nieprawidlowe dane, sprobuj ponownie")
        zadanie1()
    elif (waga/(wzrost**2)) >18.5 and (waga/(wzrost**2)) < 24.9:
        print ("waga prawidlowa")
    elif (waga/(wzrost**2)) < 18.5:
        print("niedowaga")
    else:
        print("nadwaga")
 
zadanie1()
"""

"""
def zadanie2():
    cenaTowaru = float(input("Podaj poczatkowa cene: "))
    liczbaRat = int(input("Podaj liczbe rat: "))
    
    if cenaTowaru <100 or cenaTowaru > 10000:
        print("bledny zakres cen, sprobuj ponownie ")
        return zadanie2()
        
    if liczbaRat >5 and liczbaRat <13:
        miesiecznarata = (cenaTowaru *1.025)/liczbaRat
    elif liczbaRat >12 and liczbaRat <25:
        miesiecznarata = (cenaTowaru *1.05)/liczbaRat
    elif liczbaRat >24 and liczbaRat <49:
        miesiecznarata = (cenaTowaru *1.1)/liczbaRat

    else:
         print("bledna liczba rat, wprowadz ponownie ")
         return zadanie2()
    print ("miesieczna rata wynosi: ", miesiecznarata)

    #za kazdym razem od calej kwoty odejmujemy co zostalo splacone (bez odsetek) do liczenia kolejnych rat
    #mozna jak chcemy jednak to liczyc

zadanie2()

"""

"""
def zadanie3():
    gornaLiczba = int(input("podaj gorna calkowita, dodatnia liczbe: "))
    if gornaLiczba % 1 !=0 or gornaLiczba < 0:
        print("podano bledna liczbe, sprobuj ponownie ")
        return zadanie3()
    dolnaLiczba = int(input("podaj dolna calkowita, dodatnia liczbe: "))
    if dolnaLiczba % 1 !=0 or dolnaLiczba < 0:
        print("podano bledna liczbe, sprobuj ponownie ")
        return zadanie3()
    for iterator in range (dolnaLiczba, gornaLiczba +1):
        if iterator % 2 != 0:
            print (iterator)
            
zadanie3()

"""

"""
def zadanie4():
    n = float(input("Do jakiej wartosci chcesz potegowac? (n): "))
    if n % 1 !=0 or n < 0:
        print("podano bledna liczbe, sprobuj ponownie ")
        return zadanie4()
    a=0
    potegowana = float(input("podaj liczbe, ktora chcesz potegowac: "))
    if potegowana % 1 !=0 or potegowana < 0:
        print("podano bledna liczbe, sprobuj ponownie ")
        return zadanie4()
    while potegowana**a <= n:
        print (potegowana**a)
        a=a+1

zadanie4()
"""

"""
def zadanie5():
    suma = 0
    dodana = 1
    while dodana !=0:
        dodana = float(input("podaj liczbe do zsumowania: "))
        suma = suma+dodana
    print("Suma podanych liczb to: ", suma)

zadanie5()
"""

"""
def zadanie6():
    ciagLiczb = ""
    pierwszaPetla = True
    podaneLiczby=input("Podaj liczby, 0 aby zakonczyc: ")
    while podaneLiczby != "0":
        ciagLiczb += podaneLiczby + " "
        podaneLiczby =input("Podaj liczby, 0 aby zakonczyc: ")
    print ("podany ciag liczb, to: ", ciagLiczb , "0")
    for liczba in ciagLiczb.split():
        liczba = int(liczba)
        if pierwszaPetla:
            min = liczba
            max = liczba
            pierwszaPetla = False
        if liczba < min:
            min = liczba
        if liczba > max:
            max = liczba

    print("minimum: ",min)
    print("maksimum: ", max)
    print ("suma min i max, to: ", (min+max))
    print("srednia: ", (min+max)/2)
        

zadanie6()
"""


"""
import random

def zadanie7():
    trudnosc = int(input("Wybierz poziom trudnosci (1-3): "))
    if trudnosc == 1:
        poziom = 50
    elif trudnosc == 2:
        poziom = 100
    elif trudnosc == 3:
        poziom = 200
    else:
        print("Bledna wartosc, wybierz ponownie ")
        zadanie7()
    
    losowa = random.randint(1, poziom)
    proba = int(input(f"zgadnij liczbe (1-{poziom}) "))
    szanse = 4
    while proba!=losowa and szanse>0:
        if proba > losowa:
            szanse = szanse-1
            print(f"Podales za duza wartosc, masz jeszcze {szanse +1} szanse")
            proba = int(input(f"zgadnij liczbe (1-{poziom}) "))
        elif proba< losowa:
            szanse = szanse-1
            print(f"Podales za mala wartosc, masz jeszcze {szanse+1} szanse")
            proba = int(input(f"zgadnij liczbe (1-{poziom}) "))
    if proba == losowa:
        print("Gratulacje!")

zadanie7()
"""


"""
def zadanie10():
    n = int(input("Podaj liczbe calkowita (n) : "))
    sprawdzenie = 0
    if n == 0 or n == 1:
        print("to nie jest liczba pierwsza")
    else:
        for i in range(2, n):
            if n % i == 0:
                sprawdzenie = sprawdzenie + 1
    if sprawdzenie > 0:
        print("to nie jest liczba pierwsza")
    elif sprawdzenie == 0:
        print("to jest liczba pierwsza")

zadanie10()
"""