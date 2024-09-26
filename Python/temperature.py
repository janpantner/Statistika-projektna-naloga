import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

df = pd.read_csv('Podatki\\Temp_LJ.csv')

n = 360

Y = df['TEMPERATURA'].to_numpy()
Y = Y.reshape([n, 1])

#-----------------------  Model (a) -----------------------#

ones = np.ones((12, 1))
months = ones
sin = np.sin(math.pi * np.arange(12) / 6).reshape([12, 1])
cos = np.cos(math.pi * np.arange(12) / 6).reshape([12, 1])
for i in range(2, 31):
    months = np.concatenate((months, i*ones))
    sin = np.concatenate((sin, np.sin(math.pi * np.arange(12) / 6).reshape([12, 1])))
    cos = np.concatenate((cos, np.cos(math.pi * np.arange(12) / 6).reshape([12, 1])))

X_A = np.concatenate((np.ones((n, 1)), months, sin, cos), axis=1)

beta_A = np.matmul(np.matmul(np.linalg.inv(np.matmul(X_A.T, X_A)), X_A.T), Y)

RSS_A = np.linalg.norm(Y - np.dot(X_A, beta_A))
AIC_A = round(2*4 + n*np.log(RSS_A))

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(3)
plt.plot(np.matmul(X_A, beta_A)[300:], linewidth=1.5, color='green')
plt.plot(Y[300:], linewidth=1.5, color='gray')
plt.xlabel("Meseci, začenši z januarjem 2019")
plt.ylabel("Temperatura [°C]")
plt.tight_layout()
plt.savefig("Latex\\Slike\\prvi_model.png")
plt.clf()

#-----------------------  Model (b) -----------------------#

diag = np.diag(np.full(12,1)) 
for i in range(2, 31):
    diag = np.concatenate((diag, np.diag(np.full(12,1))), axis=0)

#X_C = np.concatenate((np.arange(n).reshape([n, 1]), diag), axis = 1)
X_B = np.concatenate((months, diag), axis = 1)

beta_B = np.matmul(np.matmul(np.linalg.inv(np.matmul(X_B.T, X_B)), X_B.T), Y)

RSS_B = np.linalg.norm(Y - np.dot(X_B, beta_B))
AIC_B = round(2*13 + n*np.log(RSS_B))

f.set_figwidth(8)
f.set_figheight(3)

plt.plot(np.matmul(X_B, beta_B)[300:], linewidth=1.5, color="blue")
plt.plot(Y[300:], linewidth=1.5, color="gray")
plt.xlabel("Meseci, začenši z januarjem 2019")
plt.ylabel("Temperatura [°C]")
plt.tight_layout()
plt.savefig("Latex\\Slike\\drugi_model.png")
plt.clf()

#----------------------------------------------------------#

print(f'Akaikejevi informaciji sta zaporedoma {AIC_A} in {AIC_B}.')

#----------------------------------------------------------#

p = 13 # dim V -- B
q = 4 # dim W -- A

F = (RSS_A - RSS_B) * (n-p) / (p-q) / RSS_B

print(f'Testna statistika F je enaka {round(F, 3)}.')
# fisher(p-q, n-p) = fisher(9, 356)