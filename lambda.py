
my_list=[1,2,3]

def multiply_by_2(item):
    return item*2

def only_odd(item):
    return item%2 !=0

def accumulator(acc, item):
    print(acc,item)
    return acc + item


print(list(map(lambda item: item*2,my_list)))