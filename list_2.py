def count_evens(nums):
  count=0
  for i in nums:
    if i%2==0:
      count=count+1
  return count

print (count_evens([2, 1, 2, 3, 4]) )
count_evens([2, 2, 0]) 
count_evens([1, 3, 5])
""""""""""""""""""""""""""""""

def sum13(nums):
  sum=0
  flag=False
  if(len(nums)==0):
    return 0
  for i in nums:
    if(i==13):
      flag=True
      continue  
    if(flag):
      flag=False
      continue 
    sum=sum+i
  return sum


print(sum13([1, 2, 2, 1]) )
print (sum13([1, 1]) )
print (sum13([1, 2, 2, 1, 13]))
'""""""""""""""""""""""""""""'
def sum67(nums):
  n=0
  for i in nums:
    if i < 6 :
      n=n+i
    i=i+1
  return n
print (sum67([1, 2, 2]) )
sum67([1, 2, 2, 6, 99, 99, 7]) 
sum67([1, 1, 6, 7, 2])

'""""""""""""""""""""""""""""'

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] ==nums[i+1]:
      return True
      break
    else:
      i=i+1
      
    
    
  return False

print (has22([1, 2, 2]) )
has22([1, 2, 1, 2]) 
has22([2, 1, 2])

""""""""""""""""""""
def centered_average(nums):
  nums.sort()
  sums=sum(nums[1:-1])
  length=(len(nums)-2)
  return  sums/length
centered_average([1, 2, 3, 4, 100]) 
centered_average([1, 1, 5, 5, 10, 8, 7]) 
centered_average([-10, -4, -2, -4, -2, 0]) 
