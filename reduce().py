from functools import reduce

my_list=[1,2,3]

def multiply_by_2(item):
    return item*2

def only_odd(item):
    return item%2 !=0

def accumulator(acc, item):
    print(acc,item)
    return acc + item


print(reduce(accumulator,my_list,10)) #zips first elements of the two lists and so on.
