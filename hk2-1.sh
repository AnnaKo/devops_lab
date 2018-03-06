#!/usr/bin/python

Y = int(input("Type in the year number: "))

def LY(Y):
  #if Y <= 1900:
    #print ("Sorry, the year must be greater than 1900. Try again")
  #elif Y >= 10 ** 5:
    #print ("Sorry, the year must be less than 10000. Try again")
  if Y % 4 != 0:
    LY = False
  elif Y % 100 == 0:
    if Y % 400 == 0:
      LY = True
    else:
      LY = False
  else:
    LY = True
  return LY

if LY(Y) == False:
  print LY(Y) 
  print (" is NOT a leap year")
else :
  print LY(Y)
  print (" IS a leap year")
  
