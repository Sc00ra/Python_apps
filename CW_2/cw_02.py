#6
import this
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print("Rok:", rok)
print("Język:", jezyk)
print("Wersja:", wersja)

#7
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print("Pierwsza:", pierwsza)
print("Środek:", srodek)
print("Ostatnia:", ostatnia)

#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, *_ , zawod= info
print("Imię:", imie)
print("Nazwisko:", nazwisko)
print("Zawod:", zawod)

#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok = dane[0]
jezyk = dane[1][0]
wersja = dane[1][1]
opis = dane[1][2][0]
print("Rok:", rok)
print("Język:", jezyk)
print("Wersja:", wersja)
print("Opis wersji:", opis)

#10
a = b = [1, 2, 3]
b[0] = 'zmieniono'

print("Lista a po zmianie w b:", a)
print("Lista b po zmianie w b:", b)

#11
c = a[:]

c[0] = 'nowa wartość'

print("Lista a:", a)
print("Lista b:", b)
print("Lista c po modyfikacji:", c)

#12
x = y = 10
y = y + 1

print("Wartość x:", x)
print("Wartość y:", y)

#13
K=[1,2]
L=K
K=K+[3,4]
M=[1,2]
N=M
M +=[3,4]

print(K, L, M, N)

#14
imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]

pary_imiona_oceny = zip(imiona, oceny)

for imie, ocena in pary_imiona_oceny:
    print(imie, "ma ocenę:", ocena)


#15
def kwadrat(x):
    return x ** 2

liczby = [1, 2, 3, 4, 5]

kwadraty_liczb = list(map(kwadrat, liczby))

print(kwadraty_liczb)

#16
def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = 'kalafior'
    elif isinstance(arg, int):
        arg = 65482652
    return arg

lista_przed = [1, 2, 3]
print("Lista przed:", lista_przed)
zmien_wartosc(lista_przed)
print("Lista po:", lista_przed)

int_przed = 123
print("Integer przed:", int_przed)
int_po = zmien_wartosc(int_przed)
print("Integer po:", int_po)

#17

def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    wartosc_zamowienia = cena * ilosc
    podsumowanie = f"Nazwa produktu: {nazwa_produktu}, Cena: {cena}, Ilość: {ilosc}, Łączna cena: {wartosc_zamowienia}"
    return wartosc_zamowienia, podsumowanie

zamowienia = []

zamowienia.append(zamowienie_produktu("Mleko", cena=2, ilosc=3))
zamowienia.append(zamowienie_produktu("Chleb", cena=3))
zamowienia.append(zamowienie_produktu("Masło", cena=5, ilosc=2))

for zamowienie in zamowienia:
    print(zamowienie[1])

suma_zamowien = sum(zamowienie[0] for zamowienie in zamowienia)
print("Sumaryczna wartość zamówień:", suma_zamowien)



#19

def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj

potega_2 = stworz_funkcje_potegujaca(2)  
print(potega_2(4))  


#20
#a
def licznik():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment
licznik1 = licznik()
print(licznik1())  # Output: 1
print(licznik1())  # Output: 2

#b
count_global = 0

def licznik():
    global count_global
    count_global += 1
    return count_global


print(licznik())  # Output: 1
print(licznik())  # Output: 2

#c
class Licznik:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count


licznik_instancji = Licznik()
print(licznik_instancji())  # Output: 1
print(licznik_instancji())  # Output: 2

#d
def licznik():
    if not hasattr(licznik, 'count'):
        licznik.count = 0
    licznik.count += 1
    return licznik.count


print(licznik())  # Output: 1
print(licznik())  # Output: 2


# #21
def licznik() -> int:
    count: int = 0
    
    def increment() -> int:
        nonlocal count
        count += 1
        return count
    
    return increment

licznik1 = licznik()
print(licznik1())  # Output: 1
print(licznik1())  # Output: 2

# #22


ksiazki = [
    {'tytul': 'Wiedźmin', 'autor': 'Andrzej Sapkowski', 'rok_wydania': 1993},
    {'tytul': 'Harry Potter i Kamień Filozoficzny', 'autor': 'J.K. Rowling', 'rok_wydania': 1997},
    {'tytul': 'Mistrz i Małgorzata', 'autor': 'Michaił Bułhakow', 'rok_wydania': 1966},
    {'tytul': 'Zbrodnia i Kara', 'autor': 'Fiodor Dostojewski', 'rok_wydania': 1866},
    {'tytul': 'Czysty kod', 'autor': 'Robert C. Martin', 'rok_wydania': 2008}
]

# # a. Sortowanie książek według roku wydania
ksiazki_posortowane = sorted(ksiazki, key=lambda x: x['rok_wydania'])

# # b. Filtracja książek wydanych po 2000 roku
ksiazki_po_2000 = list(filter(lambda x: x['rok_wydania'] > 2000, ksiazki))

# # c. Transformacja listy do listy tytułów
tytuly_ksiazek = list(map(lambda x: x['tytul'], ksiazki))

# # Wyświetlenie wyników
print("Książki posortowane według roku wydania:")
for ksiazka in ksiazki_posortowane:
    print(ksiazka)

print("\nKsiążki wydane po 2000 roku:")
for ksiazka in ksiazki_po_2000:
    print(ksiazka)

print("\nTytuły książek:")
for tytul in tytuly_ksiazek:
    print(tytul)

#23
def generator_dni_tygodnia(y=7):
    dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    return dni_tygodnia[:y]

print(generator_dni_tygodnia())

print(generator_dni_tygodnia(3))