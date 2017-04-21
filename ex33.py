def append_inc_print(ii, nums):
    print("At the top i is %d" %ii)
    nums.append(ii)

    ii = ii + 1
    print("Numbers now: ", nums)
    print("At the bottom i is %d" %ii)

    return ii, nums

i = 0
numbers = []
is_small = True

while is_small:
    i, numbers = append_inc_print(i, numbers)
    
    if i > 5:
        is_small = False

print("The numbers: ")
for num in numbers:
    print(num)
