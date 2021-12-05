
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


def main():
    nums = [1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
    print("Index of 37 is ---> " + str(binary_search(nums, 37)))
    print("Index of 1 is ---> " + str(binary_search(nums, 1)))
    print("Index of 59 is ---> " + str(binary_search(nums, 59)))
    print("Index of 25 is ---> " + str(binary_search(nums, 25)))

if __name__ == "__main__":
    main()