import pandas as pd
import matplotlib.pyplot as plt

SEVERNA = 1
VZHODNA = 2
JUŽNA = 3
ZAHODNA = 4

df = pd.read_csv("Podatki\\Kibergrad.csv")

N = df[df.cetrt == SEVERNA]
E = df[df.cetrt == VZHODNA]
S = df[df.cetrt == JUŽNA]
W = df[df.cetrt == ZAHODNA]

n = 100 # Velikost vzorca

#-----------------------  Naloga (a) -----------------------%

N1 = N.sample(n=n)
E1 = E.sample(n=n)
S1 = S.sample(n=n)
W1 = W.sample(n=n)
vzorci = [N1, E1, S1, W1]
combined = pd.concat(vzorci)

boxplot = combined.boxplot(column='dohodek', by='cetrt')
plt.show()

#-----------------------  Naloga (b) -----------------------%

N2 = N.sample(n=n)
N3 = N.sample(n=n)
N4 = N.sample(n=n)
N5 = N.sample(n=n)

data = pd.DataFrame({"N1": N1.dohodek, "N2": N2.dohodek, "N3": N3.dohodek, "N4": N4.dohodek, "N5": N5.dohodek})
boxplot = data[['N1', 'N2', 'N3', 'N4', 'N5']].plot(kind='box', title='boxplot')
plt.show()

#-----------------------  Naloga (c) -----------------------%

