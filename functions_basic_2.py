# 1. Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].
def countDown(x):
    newarr = []
    for i in range(x,-1,-1):
        newarr.append(i)
    return newarr
print(countDown(5))
# 2. Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.
def print_return(list):
    print(list[0])
    return list[1]
print(print_return([5,6]))
# 3. First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.
def first_plus(list):
    return (list[0] + len(list))
y = first_plus([5,3,4,5,6,4])
print(y)
# 4. Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only one element long, have the function return False
def vals_greater(list):
    newarr = []
    if len(list) == 1:
        return False
    for i in range(1,len(list)):
        if list[i] > list[1]:
            newarr.append(list[i])
    print(len(newarr))
    return newarr
y = vals_greater([5,3,4,5,6,7,8,6,2,1])
print(y)
# 5. This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].
def lengthAndValue(size, value):
    newlist = []
    for i in range(size):
        newlist.append(value)
    return newlist
y = lengthAndValue(10,2)
print(y)