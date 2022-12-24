# Алгоритм Евклида-Algoritmo de Euclides
# Algoritmo binario de Euclides 
# Algoritmo extendido de Euclides 
# Algoritmo binario extendido de Euclides 

def mcd(num1: int, num2: int)->int:  # Funcion 1
  bigNumber = num1 if num1>num2 else num2
  minNumber = num2 if num1>num2 else num1
  while(True):
    i = 1
    while(True):
      i += 1
      if(i*minNumber > bigNumber):
        i-=1
        break
      else:
        continue
    tempNum = bigNumber - (i*minNumber)
    print(f'{bigNumber} = {i} * {minNumber} + {tempNum}')
    bigNumber = minNumber
    minNumber = tempNum
    if(minNumber == 0):
      break
    else:
      continue
  return print ('mcd=',bigNumber)


def mcd_b(num1: int, num2: int)->int: # Funcion 2
  bigNumber = num1 if num1>num2 else num2
  minNumber = num2 if num1>num2 else num1
  g = 1
  while(True):
    i = 1   
    
    while(True):
        if bigNumber%2==0 and minNumber%2==0:
            bigNumber=int(bigNumber/2)
            minNumber=int(minNumber/2)
            g*=2
        else:           
            break
    
    while(True):
      i += 1
      if(i*minNumber > bigNumber):
        i-=1
        break
      else:
        continue
    tempNum = bigNumber - (i*minNumber)
    print(f'{bigNumber} = {i} * {minNumber} + {tempNum}')
    bigNumber = minNumber
    minNumber = tempNum
    if(minNumber == 0):
      break
    else:
      continue
    
  return print ('mcd= ',g*bigNumber)


def mcd_ext(num1: int, num2: int)->int: # Funcion 3
        s = 0; old_s = 1
        t = 1; old_t = 0
        r = num1; old_r = num2

        while r != 0:
            quotient = old_r//r 
            old_r, r = r, old_r - quotient*r
            old_s, s = s, old_s - quotient*s
            old_t, t = t, old_t - quotient*t
        return print(old_r, old_s, old_t)


def mcd_ext_b(num1: int, num2: int)->int: # Funcion 4
    g = 1
    while(True):
        if  num1%2==0 and num2%2==0:
            num1=int(num1/2)
            num2=int(num2/2)
            g*=2
        else:           
            break
    
        s = 0; old_s = 1
        t = 1; old_t = 0
        r = num1; old_r = num2

        while r != 0:
            quotient = old_r//r 
            old_r, r = r, old_r - quotient*r
            old_s, s = s, old_s - quotient*s
            old_t, t = t, old_t - quotient*t
        return print(g*old_r, old_s, old_t)


x= 1540
y = 520

print ('\nАлгоритм Евклида между ', x,' и ',y)
mcd(x,y)

print ('\nБинарный алгоритм Евклида между ',  x,' и ',y)
mcd_b(x,y)

print ('\nРасширенный алгоритм Евклида между ',  x,' и ',y)
mcd_ext(x,y)

print ('\nРасширенный бинарный алгоритм Евклида между ',  x,' и ',y)
mcd_ext_b(x,y)
