# 1. 
def randInt(int):
    import random
    x = random.random()*100
    return(int(x))
y = randInt(int)
print(y)
# 2.
def randInt(max=50):
    import random
    x = random.random()*50
    return(int(x))
y = randInt(max=50)
print(y)
# 3. 
def randInt(min=50):
    import random
    x = random.random()*50+50
    return(int(x))
y = randInt(min=50)
print(y)
# 4.
def randInt(min=50,max=500):
    import random
    x = random.random()*max
    while x < min:
        x = random.random()*max
    return(int(x))
y = randInt(min=50, max=500)
print(y)