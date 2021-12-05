def sqrt(a):
  if a < 2:
    return a
  # the initial value for left is 0
  left = 0
  # the initial value for right is the number
  right = a
  # left + 1 >= right will finish while loop
  while left + 1 < right:
    mid = (right + left) // 2
    
    if mid * mid == a:
      # mid is the answer
      return mid
    elif mid * mid < a:
      # there is no sense to search among numbers less than mid
      left = mid
    else:
      # there is no sense to search among numbers bigger than mid
      right = mid
  # the answer is left
  return left
  
def main():
  print("The square root of 11 is ---> " + str(sqrt(11)))
  print("The square root of 9 is ---> " + str(sqrt(9)))