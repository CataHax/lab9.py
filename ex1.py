# Swap the first and last elements in the list.

def swapp(a):

    lis= []
    for e in range(len(a)):
        if e == 0:
            lis.append(a[4])
        elif e == 4:
            lis.append(a[0])
        else:
            lis.append(a[e])
    return lis


my_list = [1, 4, 55, 6, 70]
d= swapp(my_list)
print(d)

# end

# Shift all elements by one to the right and move the last element into the first position.
# For example, 1 4 9 16 25 would be transformed into 25 1 4 9 16.

def shiftt(b):
    lis=[]
    lis.append(b[4])
    for e in range(len(b)-1):
        lis.append(b[e])
    return lis


my_list = [1, 4, 55, 6, 70]
d= shiftt(my_list)
print(d)

# end
