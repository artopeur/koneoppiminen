# Käytetään tätä tiedostoa esimerkkinä, miten toisesta
# python tiedostosta voi importoida (=tuoda) toiminnallisuutta
# toiseen python tiedostoon tai moduliin.

if(__name__ == '__main__'):
  print("nyt suoritit moduulin")
  print("itsenäisenä")

import numpy as np
import matplotlib as mpl

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

def functionx(rangeOfX, h):
  print("Original input: ", rangeOfX)
  exes = rangeOfX**2
  print("F(x)=x^2: ", exes)
  jakaja = [h for i in rangeOfX]
  print("h: ", jakaja)
  fxh = (rangeOfX+jakaja)**2 #antaa f(x+h) arvon jokaiseen alkioon
  print("f(x+h)", fxh)
  deriv = ((exes + fxh) / jakaja)
  print("Derivated (f(x)+f(x+h)) /h: ", deriv)


  '''
  tulos=np.arange(0,rangeOfX.size)
  #tulos = [0. for i in rangeOfX]
  ftulos = [0. for i in rangeOfX]
  print("tulos: ", tulos)
  jakaja = 0.001
  ftulos = [np.float64(i**2) for i in rangeOfX]
  
  print("tulos:", tulos)
  print("ftulos:", ftulos)
  '''
  
''''
for i in rangeOfX:
    print(i)
    ftulos = i**2
    tulos = (i**2 + (i**2 + jakaja)) / jakaja
'''