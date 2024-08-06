def list1_in_list2(__lst1: None, __lst2: None) :
    """This function checks if all the items of lst1 are in lst2.
    """
    # Go over all of lst1 items
    counter1 = 0
    while counter1 < len(__lst1):
        found =  False
        # Search the lst1[counter1] in lst2
        counter2 = 0
        while counter2 < len(__lst2):
            if __lst1[counter1] == __lst2[counter2]:
                found = True
            counter2 += 1

        # If we didn't find, we have a number in lst1 which is not in lst2
        if not found:
            return False

        counter1 += 1

    # If we got here, we found all lst1 items in lst2
    return True
print(list1_in_list2([3, 2, 1], [3, 2, 6, 5, 1]))  # should be True
print(list1_in_list2([3, 2, 1], [3, 2, 6, 5]))  # should be False

