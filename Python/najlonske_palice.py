import math
import scipy.optimize
from scipy.stats import binom
import scipy

#-----------------------  Naloga (a) -----------------------#

palice = [157, 69, 35, 17, 1, 1]
# Izračun logaritma verjetja.
def f(k, n, p):
    return (math.factorial(n)/math.factorial(k)/math.factorial(n-k)) * p ** k * (1-p) ** (n-k)
def l(p):
    return sum([math.log(f(k, 5, p))*(palice[k]) for k in range(6)])

# Izračun maksimuma verjetja.
result = scipy.optimize.minimize_scalar(lambda x: -l(x), bounds=[0,1], method='bounded')
a = result.x

print(f'(a) Ocena za p po metodi največjega verjetja je {a}.')

# Alternativno

data = 157 * [0] + 69 * [1] + 35 * [2] + 17 * [3] + [4, 5]

d = scipy.stats.fit(binom, data, bounds={"n":[5]}).params

print(f'(a) Ocena za p po metodi največjega verjetja je {d.p}.')

#-----------------------  Naloga (b) -----------------------#

palice_zdruzeno = [157, 69, 35, 19]
f_last = sum([f(i, 5, a) for i in [3, 4, 5]])

x2 = 0
for i in range(3):
    x2 += (palice_zdruzeno[i] - 280*f(i, 5, a))**2 / (280*f(i, 5, a))

x2 += (19 - 280*f_last)**2 / (280*f_last)

print(f'(b) Pearsonova testna statistika je enaka {x2}.')

#-----------------------  Naloga (c) -----------------------#



#-----------------------  Naloga (d) -----------------------#

