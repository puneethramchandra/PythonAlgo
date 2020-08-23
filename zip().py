my_list=[1,2,3]
your_list=[10,20,30]

def multiply_by_2(item):
    return item*2

def only_odd(item):
    return item%2 !=0


print(list(zip(my_list,your_list))) #zips first elements of the two lists and so on.
