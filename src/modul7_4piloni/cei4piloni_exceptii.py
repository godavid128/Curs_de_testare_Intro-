
print('EXCEPTII')
# 1. EXCEPTII - daca rulam un cod, si ne da un eroare
# try = incearca
try:  # in try prinzi o exceptie
    my_list = [1, 2, 3]
    print(my_list[2])
    print(my_list[3])
except IndexError:  # in except o tratezi
    print('Index out of range')
finally:  # in finally poate vrei sa generezi un raport de teste
    print('Astazi suntem in februarie')

try:
    print(x)
except NameError:
    print('x is not defined')

# todo sa executam mai multe tipuri de exceptii din:
#       https://docs.python.org/3/tutorial/errors.html
