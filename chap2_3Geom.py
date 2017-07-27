import numpy as np
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


class Geometric:
  def __init__(self,p,n,samples=1000000):
    self.data = np.zeros(samples,dtype=np.int)    
    for i in range(n):
      if i%20==0:
        print i
      tempB = Bernouli(p,samples=samples)
      tempMask = (tempB.data==1)
      self.data[tempMask] = n-i
    self.counter = Counter(self.data)
    
    
    self.prob = {}
    #Remove 0's count    
    self.counter.pop(0, None)
    totalCount = sum(self.counter.values())
    for x in range(n-1):
      y = self.counter.get(x+1,0)      
      self.prob[x+1] = y/float(totalCount)
       

b = Geometric(p=0.1,n=60)
print b.prob
print sum(b.prob.values())

plt.plot(b.prob.keys(), b.prob.values(),'ro-')
plt.show()
plt.bar(b.prob.keys(), b.prob.values(),0.1)
plt.show()