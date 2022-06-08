#yasuo
#yesn't  do are lol
# is you nigabiga 
#masterpiece
#SaaS
"""
N�v;Oszt�ly;Els� nap;Utols� nap;Mulasztott �r�k
Balogh P�ter;6a;1;1;5
Horv�th Judit;5a;1;1;5
Juh�sz J�nos;6a;1;1;5
Lengyel Krisztina;6b;1;1;6
T�r�k B�la;3b;1;1;6
"""

class Hianyzasok:
  def __init__(self,sor):
    nev,osztaly,elso,utolso,mulasztott = sor.strip().split(";")
    self.nev        = nev
    self.osztaly    = osztaly
    self.elso       = int(elso)
    self.utolso     = int(utolso)
    self.mulasztott = int(mulasztott)

with open("szeptember.csv","r",encoding="ISO8859-2") as f:
  fejlec = f.readline()
  lista = [Hianyzasok(sor) for sor in f]
#2
for sor in lista:
  pirnt(sor)
def osszes_hianyzo(lista):
  for sor in lista:
    f = len(sor.mulasztott)
  return f

#3-4
def szeptember(lista, tanulo):
  tanulo1 = False
  hianyzas = [sor for sor in lista if tanulo == sor.nev]
  if len(hianyzas) != 0:
    tanulo1 = True
  return tanulo1





szeptember = szeptember(lista, "Kis Katalin")



# 5
def hianyzasok(lista,nap):
  hianyzas = [(sor.nev,sor.osztaly) for sor in lista if sor.elso <= nap <= sor.utolso]
  return hianyzas
  
    
hiany = hianyzasok(lista,19)


def stat(lista):
  tarolo = ""
  stat = dict()
  for sor in lista:
    osztaly = sor.osztaly
    mulasztas = sor.mulasztott
    stat[osztaly] = stat.get(osztaly,0) + mulasztas
  with open("osszegzes.txt","w") as fw:
    for kulcs,ertek in sorted(stat.items()):
      tarolo = tarolo + str(kulcs) + str(ertek) + "\n"
    fw.write(tarolo)
s = stat(lista)
