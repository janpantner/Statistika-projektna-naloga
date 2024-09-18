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
AIC_A = round(8 + n*np.log(RSS_A))

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(3)
plt.plot(np.matmul(X_A, beta_A)[300:], linewidth=1.5, color='green')
plt.plot(Y[300:], linewidth=1.5, color='gray')
plt.xlabel("Meseci začenši z januarjem 2019")
plt.ylabel("Temperatura [°C]")
plt.tight_layout()
plt.savefig("Latex\\Slike\\prvi_model.png")
plt.clf()


#-----------------------  Model (b) -----------------------#

diag = np.diag(np.full(12,1)) 
for i in range(2, 31):
    diag = np.concatenate((diag, np.diag(np.full(12,i))), axis=0) 

X_B = np.concatenate((np.ones((n, 1)), diag), axis = 1)

beta_B = np.matmul(np.matmul(np.linalg.inv(np.matmul(X_B.T, X_B)), X_B.T), Y)

RSS_B = np.linalg.norm(Y - np.dot(X_B, beta_B))

AIC_B = round(26 + n*np.log(RSS_B))

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(3)
plt.plot(np.matmul(X_B, beta_B)[300:], linewidth=1.5, color="red")
plt.plot(Y[300:], linewidth=1.5, color="gray")
plt.xlabel("Meseci začenši z januarjem 2019")
plt.ylabel("Temperatura [°C]")
plt.tight_layout()
plt.savefig("Latex\\Slike\\drugi_model.png")
plt.clf()

#-----------------------  Model (c) -----------------------#

diag = np.diag(np.full(12,1)) 
for i in range(2, 31):
    diag = np.concatenate((diag, np.diag(np.full(12,1))), axis=0)

#X_C = np.concatenate((np.arange(n).reshape([n, 1]), diag), axis = 1)
X_C = np.concatenate((months, diag), axis = 1)

beta_C = np.matmul(np.matmul(np.linalg.inv(np.matmul(X_C.T, X_C)), X_C.T), Y)

for i in beta_C:
    j = str(i[0])
    print(j[0:6])

RSS_C = np.linalg.norm(Y - np.dot(X_C, beta_C))
AIC_C = round(26 + n*np.log(RSS_C))

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(3)
plt.plot(np.matmul(X_C, beta_C)[300:], linewidth=1.5, color="blue")
plt.plot(Y[300:], linewidth=1.5, color="gray")
plt.xlabel("Meseci začenši z januarjem 2019")
plt.ylabel("Temperatura [°C]")
plt.tight_layout()
plt.savefig("Latex\\Slike\\tretji_model.png")
plt.clf()

#-----------------------  Model (d) -----------------------#

diag = np.diag(np.full(12,1)) 
for i in range(2, 31):
    diag = np.concatenate((diag, np.diag(np.full(12,1))), axis=0)

X_D = np.concatenate((np.ones((n, 1)), np.arange(n).reshape([n, 1]), diag), axis = 1)

beta_D = np.matmul(np.matmul(np.linalg.inv(np.matmul(X_D.T, X_D)), X_D.T), Y)

RSS_D = np.linalg.norm(Y - np.dot(X_D, beta_D))
AIC_D = round(28 + n*np.log(RSS_D))

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(3)
plt.plot(np.matmul(X_D, beta_D)[300:], linewidth=1.5, color="purple")
plt.plot(Y[300:], linewidth=1.5, color="gray")
plt.xlabel("Meseci začenši z januarjem 2019")
plt.ylabel("Temperatura [°C]")
plt.tight_layout()
plt.savefig("Latex\\Slike\\cetrti_model.png")
plt.clf()

#----------------------------------------------------------#

print(f'Akaikejeve informacije so zaporedoma {AIC_A}, {AIC_B}, {AIC_C} in {AIC_D}.')