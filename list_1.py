def first_last6(nums):
  if nums[-1]==6 or nums[0]==6:
    return True
  return False
first_last6([1, 2, 6]) 
first_last6([6, 1, 2, 3])
first_last6([13, 6, 1, 2, 3])
""""""""""""""""""""""""""""""""""""""
def common_end(a, b):
  if (len(a))>=1 and (len(b))>=1:
    if a[0]==b[0] or a[(len(a))-1]==b[(len(b))-1]:
      return True
    return False
  return False

common_end([1, 2, 3], [7, 3]) 
common_end([1, 2, 3], [7, 3, 2])
common_end([1, 2, 3], [1, 3])

"""""""""""""""""""""""""""""'''"""""""""
def same_first_last(nums):
  if (len(nums)) >=1 and nums[-1]==nums[0]:
    
    return True
  return False

same_first_last([1, 2, 3])
same_first_last([1, 2, 3, 1]) 
same_first_last([1, 2, 1])
""""""""""""""""""""""'""'""'""""''''''"
def reverse3(nums):
  return nums[::-1]
reverse3([1, 2, 3]) 
reverse3([5, 11, 9]) 
reverse3([7, 0, 0]) 
"**************************************"
def sum2(nums):
  if len(nums)>=2:
    return nums[0]+nums[1]
  elif len(nums)==0:
    return 0
  else:
    return nums[0]

sum2([1, 2, 3])
sum2([1, 1]) 
sum2([1, 1, 1, 1])
"**************************************"
def has23(nums):
  if nums[0]==2 or nums[0]==3 or nums[1]==2 or nums[1]==3:
    return True
  return False

has23([2, 5]) 
has23([4, 3]) 
has23([4, 5]) 


