x = 4
y = 2
# interschimbam valoarea variabilei
a = x
x = y
y = a
print(x, y)   #varianta 1 prin crearea unei noi variabile

x, y = y, x
print(x, y)    #varianta 2 prin egalare

x = x + y
y = x - y
x = x - y
print(x, y)    # var 3 prin adun si scadere

# TODO cum am putea face cu imultirea si impartirea
x = x * y
y = x / y
x = x / y
print(x, y)
