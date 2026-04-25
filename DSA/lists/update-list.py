lst = [1, 2, 3]
lst[0] = 100
lst.append(4)

print(lst)

# Adding elems
lst2 = [1, 2]
lst2.append(3)
lst2.insert(1, 99)
lst2.extend([4, 5])

print(lst2)

# remove elems
lst3 = [1, 2, 3, 4]
lst3.remove(2)
lst3.pop() #removes the last elem
lst3.pop(1) #remove index one
print(lst3)
del lst3[0] #delete by index
lst3.clear() #empty list
print(lst3)