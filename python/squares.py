#!/usr/bin/python
# -*- coding: utf-8 -*-

def squares():
  for x in xrange(1, 100 + 1):
    print (x*x)

squares()

print "\nNuno\n"


print "\nJenny\n"


def primes():
  print ("1")
  for num in range(2, 50 + 1):
    for div in range(2, num):
      if (num % div) == 0:
        print(num)
        break
    else:
      print("PRIME")

primes()

