

def add(x, y):
    return x + y

#
# print(add(1, 2))
#

# f = lambda x,y : x + y
# print(f(1, 2))

def test01(m):
    # return m(1, 2)
    return add(1, 2)




# print(test01(f))
print(test01(add))

