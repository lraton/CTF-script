from pwn import *
from Crypto.Util.number import *
import numpy
import math

c=3385784341711364291
d=4208232229832232305
m=numpy.power(c,d)
print(m)
p=4208232229832232305
q=4208232229832232305
n=p*q
m=m%n
print(m)
