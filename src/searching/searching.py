# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # return True or False if value is in binary tree
    # search left side, search right side
    # start at top node
    #

    # start = 0
    # end = (len(arr) - 1)
    if start <= end:

        middle = (start + end) // 2

    # base case
        if arr[middle] == target:
            return middle

        elif target < arr[middle]:

            # left = arr[:middle]
            # end = middle - 1
            return binary_search(arr, target, start, middle - 1)

        else:
            # right = arr[middle:]
            # start = middle + 1
            return binary_search(arr, target, middle + 1, end)
    return -1

    # found = False

    # while end >= start and not found:

    #     middle = (start + end) // 2

    #     # base case
    #     if arr[middle] == target:
    #         found = True
    #         return arr[middle]

    #     elif target < arr[middle]:
    #         binary_search(arr[:middle], target, start, middle - 1)

    #     else:
    #         binary_search(arr[middle:], target, middle + 1, end)

    # return -1
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
