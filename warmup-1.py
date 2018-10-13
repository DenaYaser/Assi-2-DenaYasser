def sleep_in(weekday, vacation):
  if not weekday or  vacation :
    return True
  else:
    return False

sleep_in(False, False) 
sleep_in(True, False) 
sleep_in(False, True) 

"*****************************************"
def diff21(i):
  if i<=21:
    return 21-i
  else:
    return (i-21)*2

diff21(19) 

"******************************************"
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  if a_smile and not b_smile:
    return False
  if not a_smile and  b_smile:
    return False


monkey_trouble(True, True) 
monkey_trouble(False, False) 
monkey_trouble(True, False)

"*******************************************"
def near_hundred(n):
	if ((abs(100 - n) <= 10) or (abs(200 - n) <= 10)):
		return True
	else:
		return False


near_hundred(93) 
near_hundred(90) 
near_hundred(89)
near_hundred(190) 
near_hundred(189)

"****************************************"
def missing_char(lis, i):
  list1 = lis[:i]   
  list2= lis[i+1:]
  return list1+list2

missing_char('kitten', 1) 
missing_char('kitten', 0) 
missing_char('kitten', 4)

"****************************************"
def pos_neg(a, b, negative):
  if not negative:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
   
  else:
      
    return  (a < 0 and b < 0)

pos_neg(1, -1, False) 
pos_neg(-1, 1, False) 
pos_neg(-4, -5, True) 

