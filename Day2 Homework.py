#Part 1
def max_num(num1, num2, num3):
    return max([num1,num2,num3])

print(max_num(3,5,2))

#Part 2
def mult_list(lst):
    product = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            product = product * i

    # for i in lst:
    #     product = lst[i] * lst[i+1]

    return product


print(mult_list([2,3,4]))

#Part 3

def rev_string(input_string):
    
    return input_string[::-1]

original_string = "Hello, world!"
reversed_string = rev_string(original_string)
print("Reversed string:", reversed_string)

#Part 4

def num_within(num,start_range,end_range):
    return start_range <= num, end_range

print(num_within(3,10,4))
print(num_within(10,2,5))

#Part 5
def pascal(n):
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev_row[j - 1] + prev_row[j]
        print(" ".join(map(str, row)).center(n * 3))

        prev_row = row

pascal(5)
