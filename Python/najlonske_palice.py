import math
import scipy.optimize
from scipy.stats import binom
from scipy.optimize import fsolve
import scipy
import numpy as np

#-----------------------  Naloga (a) -----------------------#

palice = [157, 69, 35, 17, 1, 1]
n = sum(palice)
# Izračun logaritma verjetja.
def f(k, n, p):
    return (math.factorial(n)/math.factorial(k)/math.factorial(n-k)) * p ** k * (1-p) ** (n-k)
def l(p, m):
    return sum([math.log(f(k, m, p))*(palice[k]) for k in range(6)])

# Izračun maksimuma verjetja.
result = scipy.optimize.minimize_scalar(lambda x: -l(x, 5), bounds=[0,1], method='bounded')
a = result.x

print(f'(a) Ocena za p po metodi največjega verjetja je {round(a, 5)}.')

# Alternativno:
# 
# data = 157 * [0] + 69 * [1] + 35 * [2] + 17 * [3] + [4, 5]
# 
# d = scipy.stats.fit(binom, data, bounds={"n":[5]}).params
# 
# print(f'(a) Ocena za p po metodi največjega verjetja je {d.p}.')

#-----------------------  Naloga (b) -----------------------#

palice_zdruzeno = [157, 69, 35, 19]
f_last = sum([f(i, 5, a) for i in [3, 4, 5]])

x2 = 0
for i in range(3):
    x2 += (palice_zdruzeno[i] - 280*f(i, 5, a))**2 / (280*f(i, 5, a))

x2 += (19 - 280*f_last)**2 / (280*f_last)

print(f'(b) Pearsonova testna statistika je enaka {round(x2)}.')

#-----------------------  Naloga (c) -----------------------#

m_data0 = 280 * [5]
data0 = 157 * [0] + 69 * [1] + 35 * [2] + 17 * [3] + [4, 5]
# Določitev p_i po metodi največjega verjetja.
#def p_i(i, data, m_data):
#    x = data[i]
#    m = m_data[i]
#    f = lambda p: x/p + (x-m)/(1-p)
#    return fsolve(f, 1/2)

# Določitev p_0 po metodi največjega verjetja.
def l(p, data, m_data=m_data0):
    return sum([math.log(f(data[k], m_data[k], p)) for k in range(280)])

def p0(data, m_data=m_data0):
    result = scipy.optimize.minimize_scalar(lambda x: -l(x, data, m_data0), bounds=[0,1], method='bounded')
    return result.x

def statistic(data=data0, m_data=m_data0):
    lam = 0
    p_0 = p0(data)
    for i in range(len(data)):
        m = m_data[i]
        x = data[i]
        if x != 0 and x != 5:
            p = x / m
            lam += x * math.log(p) + (m  - x) * math.log(1 - p)
        lam -= x * math.log(p_0) + (m  - x) * math.log(1 - p_0)
    return 2 * lam

#-----------------------  Naloga (d) -----------------------#

statistika_izmerjenih_podatkov = statistic()
print(f'(d) Testna statistika na podlagi razmerja verjetij je enaka {statistika_izmerjenih_podatkov}.')

samples = 10000
count = 0
#for _ in range(samples):
#    sample = np.random.binomial(5, a, size=n)
#    if statistic(sample) > statistika_izmerjenih_podatkov:
#        count += 1

print(f'(d): Med {samples} simuliranimi vrednostmi preizkusne statistike pri ničelni domnevi, jih {count} preseže vrednost {statistika_izmerjenih_podatkov}.')