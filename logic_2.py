def no_teen_sum(a, b, c):
  if a<13 and b<13 and c<13 and c<19 :
    return a+b+c
    
  elif a<13 and b<13 and c>13 :
    if c!=15 and c!=16 :
      
      return a+b
    else:
      return a+b+c
      
  elif a<13 and b>13 and c<13 :
    
    if b!=15 and b!=16 :
      return a+c
      
    else:
      return a+b+c
  elif a>13 and b<13 and c<13 :
    
    if a!=15 and a!=16 :
      
      return b+c
    else:
      return a+b+c
      
  elif a>13 and b>13 and c<13 :
    
    if b!=15 and b!=16 and a!=15 and a!=16:
      
      return c
    else:
      return a+b+c
      
  elif a>13 and b<13 and c>13 :
    
    if c!=15 and c!=16 and a!=15 and a!=16:
      
      return b
    else:
      return a+b+c
      
  elif a<13 and b>13 and c>13 :
    
    if b!=15 and b!=16 and c!=15 and c!=16:
      
      return a
    else:
      return a+b+c
  elif a>13 and b>13 and c>13 :
    
    if b!=15 and b!=16 and a!=15 and a!=16 and c!=15 and c!=16:
      
      return 0
    elif b!=15 and b!=16 and a!=15 and a!=16 and c==15 or c==16:
      return c
    elif  b==15 or b==16 and a!=15 and a!=16 and c!=15 and c!=16:
      return b
    elif  b!=15 and b!=16 and a==15 or a==16 and c!=15 and c!=16:
      return a
    elif  b==15 or b==16 and a==15 or a==16 and c!=15 and c!=16:
      return a+b
    elif  b!=15 and b!=16 and a==15 or a==16 and c==15 or c==16:
      return a+c
    elif  b==15 or b==16 and a!=15 and a!=16 and c==15 or c==16:
      return b+c
      
      
  
""""""""""""""""""""""""""
def round10(a):  
  if a<5 :
    return 0
  elif a>=5 and a<15:
    
    return 10
  elif a>=15 and a<=24:
    return 20
  elif a>=25 and a<=34:
    return 30
  elif a>=35 and a<=44:
    return 40
  elif a>=45 and a<=54:
    return 50
  elif a>=55 and a<=64:
    return 60
  elif a>=65 and a<=74:
    return 70
  elif a>=75 and a<=84:
    return 80
  elif a>=85 and a<=94:
    return 90
  else: 
    return 100


def round_sum(m, b, c):
  x=round10(m)
  y=round10(b)
  z=round10(c)
  return x+y+z


round_sum(16, 17, 18) 
round_sum(12, 13, 14) 
round_sum(6, 4, 4)
""""""""""""""""""""
def lone_sum(a, b, c):
  if(a==b and a!=c):
    return c
  if(a==c and a!=b ):
    return b
  if(c==b and c!=a ):
    return a
  if(a==b and b==c):
    return 0
  else :
    return a+b+c
  

    
lone_sum(1, 2, 3) 
lone_sum(3, 2, 3) 
lone_sum(3, 3, 3)
"""""""""""""""""""
def lucky_sum(a, b, c):
  if(a==13):
    return 0
  if(b==13):
    return a
  if(c==13):
    return a+b
  else:
    return a+b+c
 
lucky_sum(1, 2, 13) 
lucky_sum(1, 13, 3) 
