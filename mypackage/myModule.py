def top_n(items, n):
    """This function returns the top n values in the list sorted in descending manner.
    args
        items -- array like object 
        n -- int (number of items)
    return value -- n-top most values
    """
    for i in range(n):# order the list in ascending order
        for j in range(len(items) - 1 - i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    top_n = items[-n:] #take the last n items from the ascending ordered list
    return top_n[::-1] #get the list in reverse oreder (i.e. descending)


print(top_n([1, 7, 2, 3, 9, 20], 3))