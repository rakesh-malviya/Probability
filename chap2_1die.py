from astropy.units import second
print "Chapter 2"
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt


class Die:
  def __init__(self,sides=6,rollCount=1000000):
    self.rollCount = rollCount
    self.data = np.random.choice(sides,rollCount)+1    
    self.counter = Counter(self.data)
  
  def prob(self,x):
    if x > 0 and x <=6:
      return self.counter[x]/float(self.rollCount)
    
    
firstRoll = Die()
print firstRoll.counter
print firstRoll.prob(1)
print 1.0/6.0


secondRoll = Die()


# Sum of two rolls random variable probability

totalCount = secondRoll.rollCount
sumData = firstRoll.data + secondRoll.data
counter = Counter(sumData)
sum2roll = {}


for x,y in counter.items():
  sum2roll[x] = float(y)/float(totalCount)
  
print sum2roll

#probability mass function plot
plt.plot(sum2roll.keys(), sum2roll.values(),'ro-')
plt.show()

# random variable X = max roll in two independent rolls of a fair 4-sided die
roll1 = Die(sides=4)
roll2 = Die(sides=4)

# print np.concatenate([np.reshape(roll1.data, (-1,1)),np.reshape(roll2.data, (-1,1))],axis=1).shape
roll1.data = np.reshape(roll1.data, (-1,1))
roll2.data = np.reshape(roll2.data, (-1,1))

maxData = np.max(np.concatenate([roll1.data,roll2.data],axis=1), axis=1)
print maxData.shape

counter = Counter(maxData)
max2roll = {}


for x,y in counter.items():
  max2roll[x] = float(y)/float(totalCount)
  
print max2roll
plt.plot(max2roll.keys(), max2roll.values(),'ro-')
plt.show()