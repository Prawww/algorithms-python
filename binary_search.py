def binary_search(myList, target):
    first = 0
    last = len(myList) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if myList[midpoint] == target:  # Check if target is at midpoint
            return midpoint
        elif myList[midpoint] > target:  # Search in left half
            last = midpoint - 1
        else:  # Search in right half
            first = midpoint + 1

    return None  # Target not found




def verify(index):
    if index is not None:
        print("Index is:", index)
    else:
        print("Target not found")


if __name__ == '__main__':
    b = binary_search([1,2,3,4,5,6,7,8], 8)

    verify(b)

