#https://infojegyzet.hu/vizsgafeladatok/okj-programozas/szoftverfejleszto-200204/
#Dana Allison;1991-04-12;1991-05-23;215;75

class Balkezesek:
  def __init__(self,sor):
    nev, elso, utolso, suly, magassag = sor.strip().split(";")
    self.nev = nev
    self.elso = elso
    self.utolso = utolso
    self.suly = int(suly)
    self.magassag = int(magassag) * 2.54
    self.elso_ev = int(elso[0:4])
    self.utolso_ev = int(utolso[0:4])

with open("balkezesek.csv",encoding="latin2") as f:
  fejlec = f.readline()
  lista = [Balkezesek(sor) for sor in f]

def hany_adatsor(lista):
  return len(lista)

feladat3 = hany_adatsor(lista)
print(f"3.feladat: {feladat3}")

def utoljara(lista):
  tarolo = ""
  kereso = [sor for sor in lista if "1999-10" in sor.utolso]
  for sor in kereso:
    magassag = f"{sor.magassag:.1f}"
    magassag = str(magassag)
    magassag = magassag.replace(".",",")
    tarolo = tarolo + f"       " + sor.nev + ", " + magassag + " cm\n"
  return tarolo


feladat4 = utoljara(lista)
print("4.feladat:")
print(feladat4)
print("5.feladat:")

  
def bekeres(ev):
  hiba = "Hibás adat, kérek egy 1990 és 1999 közötti évszámot!"
  if 1990 <= ev <= 1999:
    return ev
  else:
    print(hiba)
    return False

feladat5 = bekeres(1995)
print(feladat5)

def atlag_suly_adott_evben(feladat5,lista):
  if feladat5 == False:
    return False
  else:
    sulyok = [sor.suly for sor in lista if sor.elso_ev <= feladat5 <= sor.utolso_ev]
    ossz = sum(sulyok)
    atlag = ossz / len(sulyok)
    atlag = f"{atlag:.2f}"
    atlag = str(atlag)
    atlag = atlag.replace(".",",")
  return atlag


feladat6 = atlag_suly_adott_evben(feladat5,lista)
if feladat6 == False:
  print("6.feladat: Hibás adat!")
else:
  print(f"6.feladat: {feladat6} font")

