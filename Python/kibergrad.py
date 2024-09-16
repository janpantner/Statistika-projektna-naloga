import pandas as pd
import matplotlib.pyplot as plt

SEVERNA = 1
VZHODNA = 2
JUŽNA = 3
ZAHODNA = 4

n = 100 # Velikost vzorca
random = 9311

df = pd.read_csv('Podatki\\Kibergrad.csv')

N = df[df.cetrt == SEVERNA]
E = df[df.cetrt == VZHODNA]
S = df[df.cetrt == JUŽNA]
W = df[df.cetrt == ZAHODNA]

#-----------------------  Naloga (a) -----------------------#

N1 = N.sample(n=n, random_state=random)
E1 = E.sample(n=n, random_state=random)
S1 = S.sample(n=n, random_state=random)
W1 = W.sample(n=n, random_state=random)

data = pd.DataFrame({'N1': N1.dohodek, 'E1': E1.dohodek, 'S1': S1.dohodek, 'W1': W1.dohodek})
bp1 = data[['N1', 'E1', 'S1', 'W1']].plot(kind='box', title='Vzorci dohodkov po četrteh')
bp1.set_xticklabels(['Severna četrt', 'Vzhodna četrt', 'Južna četrt', 'Zahodna četrt'])
bp1.set_ylabel('Dohodki')
plt.grid(axis = 'y', color = 'gray', linewidth = 0.4)
plt.tight_layout()

#-----------------------  Naloga (b) -----------------------#

N2 = N.sample(n=n, random_state=2)
N3 = N.sample(n=n, random_state=3)
N4 = N.sample(n=n, random_state=4)
N5 = N.sample(n=n, random_state=5)

medians = [N1.median().dohodek, N2.median().dohodek, N3.median().dohodek, N4.median().dohodek, N5.median().dohodek]


data = pd.DataFrame({'N1': N1.dohodek, 'N2': N2.dohodek, 'N3': N3.dohodek, 'N4': N4.dohodek, 'N5': N5.dohodek})
bp2 = data[['N1', 'N2', 'N3', 'N4', 'N5']].plot(kind='box', title='Vzorci dohodkov severne četrti')
bp2.set_xticklabels(['1', '2', '3', '4', '5'])
bp2.set_ylabel('Dohodki')
plt.grid(axis = 'y', color = 'gray', linewidth = 0.4)
plt.tight_layout()

#plt.show()

#-----------------------  Naloga (c) -----------------------#

pop = len(df.index)
population = [len(N.index), len(E.index), len(S.index), len(W.index)]
mean = df.mean().dohodek
means = [N.mean().dohodek, E.mean().dohodek, S.mean().dohodek, W.mean().dohodek]
variances = [N.var().dohodek, E.var().dohodek, S.var().dohodek, W.var().dohodek]


varB = 0
varW = 0
for i in range(4):
    wi = population[i] / pop
    varB += wi * (means[i] - mean) ** 2
    varW += wi * variances[i]

varB = round(varB)
odklonB = varB ** (1/2)
varW = round(varW)


print(f'Pojasnjena varianca je {varB}.\nNepojasnjena varianca je {varW}.')
print(f'Pojasnjeni stadardni odklon je {round(odklonB)}.')

#for i in range(4):
#    print(round(means[i]))