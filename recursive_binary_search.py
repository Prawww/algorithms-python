def rec_binary_search(myList, target):
    if(len(myList) == 0):
        return False
    else:
        midpoint = len(myList) // 2

    if(myList[midpoint] == target):
        return True
    elif(myList[midpoint] > target):
        return rec_binary_search(myList[:midpoint], target)
    else:
        return rec_binary_search(myList[midpoint+1:], target)




def verify(bool):
    if bool:
        print(bool)
    else:
        print("Target not found")


if __name__ == '__main__':
    b = rec_binary_search([1,2,3,4,5,6,7,8], 12)

    verify(b)
