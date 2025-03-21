def linear_search(lst, target):
    """
    //Implements a linear search algorithm
    :param lst: the list of numbers that contains our target
    :param target: the number we are searching for
    :return:
    """
    for i in range(len(lst)):
        if(lst[i] == target):
            return i
    return -1

if __name__ == '__main__':
    lst = [1,2,3,4,5]
    target = 5

    print(linear_search(lst, target))