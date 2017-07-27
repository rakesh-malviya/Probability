import numpy as np
import operator as op
from collections import Counter
from matplotlib import pyplot as plt

class Bernouli:
  def __init__(self,p,samples=1000000):
    randamMax = 100
    
    data = np.random.choice(randamMax,samples)
    mask =(data <randamMax*p)
    data = np.zeros(samples,dtype=np.int)
    data[mask]=1
    self.data = data
    self.counter = Counter(self.data)
    self.prob = {}
    for x,y in self.counter.items():
      self.prob[x] = y/float(samples)
      
class BinomialSample:
  def __init__(self,p,n,samples=100000):
    self.data = np.zeros(samples,dtype=np.int)
    
    for i in range(n):
      if i%20==0:
        print i
      tempBenouli = Bernouli(p,samples=samples)
      self.data += tempBenouli.data
      
    self.counter = Counter(self.data)
    self.prob = {}
    
    for x in range(n):
      y = self.counter.get(x,0)
      self.prob[x] = y/float(samples)
      
class Binomial:
  def __init__(self,p,n):
    self.prob = {}
    self.p = p
    self.n = n
    self.p_pow_table = np.zeros(n+1)
    self.p_1_pow_table = np.zeros(n+1)
    
    p_pow = 1.0
    for k in range(n+1):
      self.p_pow_table[k]=p_pow
      p_pow *=p
      
    p_1_pow = 1.0
    p_1 = 1.0-p
    for k in range(n+1):
      self.p_1_pow_table[k]=p_1_pow
      p_1_pow *=p_1
      
    for k in range(n+1):        
        self.prob[k] = self.pmfFunc(k)
  
  def ncr(self,n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

  def pmfFunc(self,k):
    n = self.n
    returnVal = self.ncr(n,k)*self.p_pow_table[k]*self.p_1_pow_table[n-k]
    return returnVal
    
    
  def PMF(self,x):
    return self.prob.get(x,0)

# b = Binomial(p=0.5,n=9)

      
"""Check how is plot when n*p < 1 and n*p > 1 (Poison random variable)"""
b = Binomial(p=0.01,n=80)
print b.prob
print sum(b.prob.values())

plt.plot(b.prob.keys(), b.prob.values(),'ro-')
plt.show()
plt.bar(b.prob.keys(), b.prob.values(),0.1)
plt.show()
