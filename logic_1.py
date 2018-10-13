def love6(a, b):
  if a==6 or b==6:
    return True
  elif a+b==6:
    return True
  elif a-b== 6 or b-a==6:
    return True 
  else:
    return False

love6(6, 4) 
love6(4, 5) 
love6(1, 5)
"""""""
def sorta_sum(a, b):
  sum=a+b
  if sum>=10 and sum<=19:
    return 20
  else:
    return sum

sorta_sum(3, 4) 
sorta_sum(9, 4) 
sorta_sum(10, 11)
""""""""""""""""'""""
def caught_speeding(speed, is_birthday):
  if(is_birthday):
    speed=speed-5
  if(speed <=60):
    return 0
  if(speed >60 and speed<=80):
    return 1
  else :
    return 2

caught_speeding(60, False) 
caught_speeding(65, False) 
caught_speeding(65, True)
""""""""""""""""""""""""""""""
def in1to10(n, outside_mode):
  if n>1 and n<10 and outside_mode != False:
    return False
  elif n>=1 and n<=10 and outside_mode != True:
    return True
  elif outside_mode:
    return True  
  else:
    return False

n1to10(5, False) 
in1to10(11, False) 
in1to10(11, True) 

