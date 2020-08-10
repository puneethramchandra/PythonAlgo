def highest_even(list):
    even=[]
    for x in list:
        if x % 2==0:
            even.append(x)
    return max(even)

print(highest_even([10,200,3,4,8,11]))