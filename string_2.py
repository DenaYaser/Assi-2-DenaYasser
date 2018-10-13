def count_hi(str):
  count=0
 
  for i in  range(len(str)-1):
    if str[i]=='h' and str[i+1]=='i':
      count=count+1
  return count

count_hi('abc hi ho') 
count_hi('ABChi hi') 
count_hi('hihi')
"""""""""""""'''''''''''''''''''''"
def cat_dog(str):
	count=count2=0
	for i in range (len(str)-1):
		if str[i]=='c' and str[i+1]=='a' and str[i+2]=='t':
			count=count+1
		else:
			i=i+1
		if str[i]=='d' and str[i+1]=='o' and str[i+2]=='g':
			count2=count2+1
		else:
			i=i+1

	return count==count2

""""""""""""""""""""""""""""""""
def double_char(str):
  str2 = ""
  for i in str:
    str2 += i*2
  return str2

double_char('The') 
double_char('AAbb')
double_char('Hi-There')
""""""""""""""""""""""""""""""""
def count_code(str):
  count=0
  for i in  range(len(str)):
    if str[i]=='c' and str[i+1]=='o' or str[1+2]=='o' and  str[i+3]=='e':
      count=count+1
    elif str[i]=='c':
      count=1
  return count
count_code('codexxcode')
count_code('aaacodebbb')
count_code('cozexxcope')
""""""""""""""""""""""""""""""""
def xyz_there(str):
  i=0
  while "xyz" in str[i:]:
    if str[i-1+str[i:].index("xyz")] != ".":
      return True
    i += str[i:].index("xyz")+2
  return False
"""""""""""""""""""""""""""""""

