def first_two(str):
  return str[0:2]

first_two('Hello') 
first_two('abcdefg') 
first_two('ab')
"***************************"
def first_half(str):
  x=len(str)-1
  xx=x/2
  return str[0:xx+1]

first_half('WooHoo') 
first_half('HelloThere') 
first_half('abcdef')

"****************************"
def without_end(str):
  return str[1:len(str)-1]
without_end('Hello') 
without_end('java') 
without_end('coding') 

"**************************"
def left2(str):
  return str[2:len(str)]+str[0:2]
left2('Hello') 
left2('java') 
left2('Hi')
"**************************"
def make_abba(a, b):
  return a+b+b+a
make_abba('Hi', 'Bye') 
make_abba('Yo', 'Alice') 
make_abba('What', 'Up') 
