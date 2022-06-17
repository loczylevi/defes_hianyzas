#Név;Neme;Részleg;Belépés;Bér
#Beri Dániel;férfi;beszerzés;1979;222943

class Berek2020:
  def __init__(self,sor):
    nev,neme,reszleg,belepes,ber = sor.strip().split(";")
    self.nev = nev
    self.neme = neme
    self.reszleg = reszleg
    self.belepes = int(belepes)
    self.ber = int(ber)

with open("berek2020.txt","r",encoding="utf-8") as f:
  fejlec = f.readline()
  lista = [Berek2020(sor) for sor in f]

def hany_dolgozo(lista):
  return len(lista)

hany_dolgozo = hany_dolgozo(lista)

print(f"3.feladat: Dolgozók száma: {hany_dolgozo} fő")

def atlag_berek(lista):
  berek = [sor.ber for sor in lista]
  ossz = sum(berek)
  atlag = ossz / len(berek)
  atlag = atlag / 1000
  atlag = f'{atlag:.1f}'
  atlag = str(atlag)
  atlag = atlag.replace(".",",")
  return atlag
  
atlag_berek = atlag_berek(lista)
print(f"4.feladat: Bérek átlaga: {atlag_berek} eFt")

def legtobbet_kereso_adott_reszlegen(lista,reszleg):
  megadott_reszleg = [(sor.ber,sor) for sor in lista if sor.reszleg == reszleg]
  if len(megadott_reszleg) > 0:
    nagy,adat = max(megadott_reszleg)
  else:
    return "A megadott részleg nem létezik a cégnél!"
  tarolo = ""
  szamlalo = 0
  while szamlalo <= 3:
    if szamlalo == 0:
      tarolo = tarolo + "       " + "Név: " + adat.nev + "\n"
    if szamlalo == 1:
      tarolo = tarolo + "       " + "Neme: " + adat.neme + "\n"
    if szamlalo == 2:
      tarolo = tarolo + "       " + "Belépés: " + str(adat.belepes) + "\n"
    if szamlalo == 3:
      tarolo = tarolo + "       " + "Bér: " + str(nagy) + " Forint" + "\n"
    szamlalo = szamlalo + 1

  #de csunya ez HE! de müködik :)
  
  return tarolo


legtobbet_kereso_adott_reszlegen = legtobbet_kereso_adott_reszlegen(lista,"beszerzés") # lényegében ez az 5.feladat a bekeres!

print("6.feladat: A legtöbbet kereső dolgozó a megadott részlegen")
print(legtobbet_kereso_adott_reszlegen)


def stat(lista):
  tarolo = ""
  stat = dict()
  for sor in lista:
    reszleg = sor.reszleg
    stat[reszleg] = stat.get(reszleg,0) + 1
  for reszleg,db in stat.items():
    tarolo = tarolo + "       " + reszleg + " - " + str(db) + " Fő\n"

  return tarolo

stat = stat(lista)
print(f"""7.feladat: Statisztika: 
{stat}""")
