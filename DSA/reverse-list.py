lst = [2, 3, 4, 5, 6, 7]

print(lst[::-1])


left = 0
right = len(lst) -1

while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1
print(lst)