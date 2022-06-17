#﻿név;születési_dátum;nemzetiség;rajtszám
#Lewis Hamilton;1985.01.07;brit;44

class Pilotak:
  def __init__(self,sor):
    nev,szuletesi_datum,nemzetiseg,rajtszam = sor.strip().split(";")
    self.nev = nev
    self.szuletesi_datum = szuletesi_datum
    self.nemzetiseg = nemzetiseg
    self.rajtszam = rajtszam
    self.ev = int(szuletesi_datum[:4])

with open("pilotak.csv","r",encoding="utf-8") as f:
  fejlec = f.readline()
  lista = [Pilotak(sor) for sor in f]

def hany_sor(lista):
  return len(lista)

hany_sor = hany_sor(lista)

print(f"3.feladat: {hany_sor}")

def utolso_nev(lista):
  return [sor.nev for sor in lista][-1]

utolso_nev = utolso_nev(lista)

print(f"4.feladat: {utolso_nev}")

def szultetes_XIX_szazadban(lista,ev):
  kisebb_1901 = [sor for sor in lista if sor.ev < ev]
  tarolo = ""
  for sor in kisebb_1901:
    tarolo = tarolo + "       " + sor.nev + " " + "(" + sor.szuletesi_datum + ")\n"  # mi ez a sor XD
  return tarolo

szultetes_XIX_szazadban = szultetes_XIX_szazadban(lista,1901)

print("5.feladat:")

print(szultetes_XIX_szazadban)

def legkisebb_rajtszam(lista):
  rajtszamok = min([(int(sor.rajtszam),sor.nemzetiseg) for sor in lista if sor.rajtszam != ""]) # easy egy sorba miiiiivaaaan 
  return rajtszamok[1]


legkisebb_rajtszam = legkisebb_rajtszam(lista)
print(f"6.feladat: {legkisebb_rajtszam}")

"""
def statisztika(lista):
  stat = dict()
  for sor in lista:
    if sor.rajtszam != "":
      rajtszam = sor.rajtszam
      stat[rajtszam] = stat.get(rajtszam, 0) + 1
  tobb_rajtszam_azonos_pilota =  [print(f"{rajtszam}",end="") for rajtszam, db in stat.items() if int(rajtszam) > 2]
  return tobb_rajtszam_azonos_pilota

statisztika = statisztika(lista)
print(f"7.feladat: {statisztika}")
"""
#_______________________________________________________
"""
statisztika = dict()
for sor in lista:
  if sor.rajtszam != "":
    rajtszam = sor.rajtszam
    statisztika[rajtszam] = statisztika.get(rajtszam, 0) + 1
tobb_rajtszam_azonos_pilota = [ print(f'{rajtszam} - {db} db.',end="") for rajtszam, db in statisztika.items() if db > 2]

print(f'7. feladat: {tobb_rajtszam_azonos_pilota} ')

"""

#7.feladat
rajtszam2 = [int(sor.rajtszam) for sor in lista if sor.rajtszam != ""]
statisztika = dict()
print("7.feladat: ",end="")
for sor in rajtszam2:
    rajtszam = sor
    statisztika[rajtszam] = statisztika.get(rajtszam, 0) + 1
y = [print(f' {rajtszam},',end="") for rajtszam, db in statisztika.items() if db > 1]
