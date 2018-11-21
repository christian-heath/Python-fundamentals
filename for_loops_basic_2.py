# 1.
def makeItBig(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
y = makeItBig([-1,3,5,-5])
print(y)
# 2.
def countPositives(list):
    sum = 0
    for i in range(len(list)):
        if list[i] > 0:
            sum+= 1
    list[len(list)-1] = sum
    return list
y = countPositives([-1,1,1,1])
print(y)
# 3. 
def sumTotal(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
y = sumTotal([1,2,3,4])
print(y)
# 4. 
def multiples(list):
    sum = 0
    for i in range(len(list)):
        sum+= list[i]
    avg = sum/len(list)
    return avg
y = multiples([1,2,3,4])
print(y)
# 5. 
def length(list):
    return len(list)
y = length([1,2,3,4])
print(y)
# 6.
def minimum(list):
    if len(list) < 1:
        return False
    return min(list)
y = minimum([-1,-2,-3])
print(y)
y = minimum([])
print(y)
# 7.
def maximum(list):
    if len(list) < 1:
        return False
    return max(list)
y = maximum([1,2,3,4])
print(y)
y = maximum([])
print(y)
# 8. 
def ultimate(list):
    sum = 0
    for i in range(len(list)):
        sum+= list[i]
    avg = sum/len(list)
    thisdict = dict(
        sumTotal= sum,
        average= avg,
        minimum= min(list),
        maximum= max(list),
        length= len(list)
    )
    return thisdict
y = ultimate([1,2,3,4,5])
print(y)
# 9. 
def reverse(list):
    for i in range(len(list)//2):
        temp = list[len(list)-1-i]
        list[len(list)-1-i] = list[i]
        list[i] = temp
    return list
y = reverse([1,2,3,4,5])
print(y)