def string_times(str, n):
  return str*n

string_times('Hi', 2) 
string_times('Hi', 3) 
string_times('Hi', 1)

"****************************"
def front_times(str, n):
  return str[0:3]*n

front_times('Chocolate', 2) 
front_times('Chocolate', 3)
front_times('Abc', 3)
"*****************************"
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

array123([1, 1, 2, 3, 1]) 
array123([1, 1, 2, 4, 1]) 
array123([1, 1, 2, 1, 2, 3])

"************************************"
def array_count9(nums):
  count=0
  for i in nums:
    if i==9:
      count=count+1

  return count

array_count9([1, 2, 9])
array_count9([1, 9, 9]) 
array_count9([1, 9, 9, 3, 9]) 
