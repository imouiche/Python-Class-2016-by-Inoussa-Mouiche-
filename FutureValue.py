import math as mt

if __name__=="__main__":

p = 10000
i = 0.08
m = 4
n = 30

Fv = p*m/i*(mt.pow(1+i/m, n*m)-1)
print "future value in 30 years", Fv
