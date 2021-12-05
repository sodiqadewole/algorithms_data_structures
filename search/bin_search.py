
def binary_search(array, target):
    if len(array) == 0:
        return -1
    left = 0
    right = len(array) - 1
    # edge case where target is at beginning
    if array[left] == target:
        return left
    elif array[right] == target:
        return right
    # loop while not at edge
    while left + 1 < right:
        mid = (left + right) // 2
        # case where target is the middle
        if array[mid] == target:
            return mid
        # case where target is to left
        elif array[mid] < target:
            left = mid # binary_search(target, array[:mid])
        else:
            right = mid # binary_search(target, array[mid:])
    return -1

def search_insert(arr, target):
    left, right = 0, len(arr)
    if arr[left] == target:
        return left
    elif arr[right-1] == target:
        return right
    while left + 1 < right:
        mid = left + right // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid
    # check if left is the index to insert target
    if arr[left] >= target:
        return left
    # right is the insert index
    return right

def binarySearch(nums, target, leftmost):
  # the initial value for left index is 0
  left = 0
  # the initial value for right index is the number of elements in the array
  right = len(nums)
  # left + 1 >= right will finish while loop
  while left + 1 < right:
    mid = (right + left) // 2
    if nums[mid] == target:
      if leftmost:
        right = mid
      else:
        left = mid
    elif nums[mid] < target:
      # there is no sense to search in the left half of the array
      left = mid
    else:
      # there is no sense to search in the right half of the array
      right = mid
  # left can be the index to answer
  if nums[left] == target:
    return left
  # right can be the index to answer
  if right < len(nums) and nums[right] == target:
    return right
  # there is no target in the array
  return -1

def count_occurence(nums, target):
  left = binarySearch(nums, target, True)
  if left < 0: 
    return -1
  right = binarySearch(nums, target, False)
  return right - left + 1

# def count_occurence(target, arr):
#     counter_left, counter_right = 0, 0
#     if binary_search(arr, target) != -1:
#         idx = binary_search(arr, target)
#         print(idx)
#         # counter_left += 1
#         while arr[idx-counter_left] == arr[idx] and arr[idx-counter_left] >= 0:
#             counter_left += 1
#         while arr[idx+counter_right] == arr[idx] and arr[idx+counter_right] <= len(arr):
#             counter_right += 1
#     return counter_left + counter_right


def search_duplicate(arr):
    left, right = 0, len(arr)
    
    while left+1 < right:
        mid = (left + right) //2
        if mid == arr[mid] and left < arr[left]:
            return mid
        elif arr[mid] < mid:
            left = mid
        else:
            right = mid
    if arr[left] == left:
        return left
    if right < len(arr) and arr[right] == right:
        return right
    return -1


def main():
    nums = [1,3,5,7,11,11,13,17,19,23,29,31,37,41,43,47,53,59]
    arr = [1, 5, 8, 9, 11, 13, 15, 19, 21]
    arr2 = [-8, -2, -1, 0, 2, 5, 8, 9]
    # print("Index of 37 is ---> " + str(binary_search(nums, 37)))
    # print("Index of 1 is ---> " + str(binary_search(nums, 1)))
    # print("Index of 59 is ---> " + str(binary_search(nums, 59)))
    # print("Index of 25 is ---> " + str(binary_search(nums, 25)))
    # print("Length of array ---> ")
    # print("Insert Index of 0 is ---> " + str(search_insert(nums, 0)))
    # print("Insert Index of 60 is ---> " + str(search_insert(nums, 60)))
    # print("Duplicate is --> " + str(search_duplicate(arr2)))
    print("Number of occurences --> " + str(count_occurence([1, 5, 5, 5, 11, 11, 15, 19, 19], 11)))

if __name__ == "__main__":
    main()