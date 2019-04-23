# -*- coding: cp1252 -*-
#Assessment#1 – (Recursion, Math Fundamentals)
def FirstFactorial(num):
  if num <0:
    return 'You must input positive value.'
  if num==0:
    return 1
  #recursive function
  f= num* FirstFactorial(num-1)
  return(f)
num = int(raw_input("Input:"))
print FirstFactorial(num)
