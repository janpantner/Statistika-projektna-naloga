import math
import scipy.optimize

palice = [157, 69, 35, 17, 1, 1]


#-----------------------  Naloga (a) -----------------------%

# Izračun logaritma verjetja.
def f(k, n, p):
    return (math.factorial(n)/math.factorial(k)/math.factorial(n-k)) * p ** k * (1-p) ** (n-k)
def l(p):
    return sum([math.log(f(k, 5, p))*(palice[k]) for k in range(6)])

# Izračun maksimuma verjetja.
result = scipy.optimize.minimize_scalar(lambda x: -l(x), bounds=[0,1], method='bounded')
a = result.x

print(f"(a) Ocena za p po metodi največjega verjetja je {a}.")

#-----------------------  Naloga (b) -----------------------%