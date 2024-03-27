from math import pi
import random
wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie ** 12
tekst = str(potega)
wartosc_pi = pi
losowa = random.choice([1,2,3,4,5])

tekst = f"Wartosc:{tekst}"
print(len(tekst))
print(tekst[1:4])
print(dir(tekst))
tekst = tekst.upper()
print(tekst)
tekst = tekst.replace("A","p")
print(tekst)

lista = list(tekst)
print(lista)
lista = lista[0:8]
print(lista)
lista = lista + [1,2,3,4,5]
print(lista)
lista.remove(':')
print(lista)

lista2 = [1,2,3,"banan",100]

lista3 = []
for i in  range(0,len(lista2)):
    if lista2[i] != "banan":
        lista3.append(lista2[i] **2) 
print(lista3)


lista4 = range(2,16,2)

print(lista2)
print(lista3)
print(lista4)


ja = {}
ja['imie'] = 'Bartosz'
ja['nazwisko'] = 'Skora'
ja['wiek'] = 22
rodzice = [{'imie':'Danuta', 'wiek': 56}, {'imie':'Robert', 'wiek': 55}]
ja['rodzice'] = rodzice
print(ja['rodzice'])

print(ja.keys())

for n in ja:
    if ja != 'rodzenstwo':
        print(False)

krotka1 = (1,2,"3",4,2,5)
print(len(krotka1))
print(krotka1[0])
nr = 0
for n in range(0,len(krotka1)):
    if krotka1[n] == 2:
        nr +=1

print(nr)

#krotka1[0] = 2

X = set("kalarepa")
Y = set("lepy")
print(X & Y)


imiona = ["sss","sadsa"]

for i in enumerate(imiona):
    print(i)


liczba = 100
if liczba >0 & liczba%2 == 0:
    print("Liczba jest dodatnia i  parzysta")

if liczba != 0:
    print("Liczba jest różna od zera")
owoc = 'jabłko'
owoce = ['jabłko', 'banan', 'pomarańcza']
for i in owoce:
    if owoc == i:
        print("Owoc jest dostępny")
x=0
y = 0
# while True:
#     if y > 100:
#         print(y)
#         exit()
#     else:
#         x = input("podaj liczbe: ")
#         x = int(x)
#         y = y + x

L = [1,2,3,4] 
M = [1,2,3,L,4] 
print(f"Wartość zmiennej M przed zmianą L: {M}")
L[1] = "woooow" 
print(f"Wartość zmiennej M po zmianie L: {M}")

L = [4,5,6] 
X = L * 4 
Y = [L] * 4 
print(f"X: {X}, Y: {Y}")


L[1] = "wow" 
print(f"X: {X}, Y: {Y}") 
L = [4,5,6] 
Y = [list(L)] * 4 
L[1] = "wow" 
print(f"Y: {Y}") 
Y[0][1] = "wow"
print(f"Y: {Y}") 


with open('teksty.json', 'r') as file: 
    content = file.read() 


import re
content = content.lower()

content = content.split()

znaki = [",","."]     
for i in content:                              
      if i in znaki:                        
        content = content.replace(i, "")
                                  

for i in content:
    if len(i) != 0:
        for j in range(0,len(i)):
            i[0].replace(i[0],i[0].upper())
            i[j].replace(i[j],i[j].upper())
            print(i)
    