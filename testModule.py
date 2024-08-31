# Käytetään tätä tiedostoa esimerkkinä, miten toisesta
# python tiedostosta voi importoida (=tuoda) toiminnallisuutta
# toiseen python tiedostoon tai moduliin.

if(__name__ == '__main__'):
  print("nyt suoritit moduulin")
  print("itsenäisenä")

import numpy as np

def printtaa(p):
    print("p:n arvo = ",p)

def distance2D(x1,y1,x2,y2):
  print("funktion inputit")
  print(x1,y1)
  print("x1 =", x1)
  print("x2 =", x2)
  print("y1 =", y1)
  print("y2 =", y2)
  xt=x2-x1
  print("etäisyydet x2-x1 =", xt)
  yt=y2-y1
  print("etäisyydet y akselilla y2-y1 = ", yt)

  eta=np.sqrt(xt+yt)
  print("EROTUS = ", eta)

