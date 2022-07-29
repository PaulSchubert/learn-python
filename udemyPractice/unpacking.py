a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)


print("Unpacking a tuple")

data = (1, 2, 76) # data represents a tuple

x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [12, 13, 14]
data_list.append(15) # with a tuple we couldn't do this and all following code would work
p, q, r = data_list
print(p)
print(q)
print(r)

