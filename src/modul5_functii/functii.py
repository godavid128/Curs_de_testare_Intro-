# TODO functie fara parametri
def sign_up_fara_parametri():
    name = 'david'
    email = 'david@gmail.com'
    password = '123456'
    is_register = False
    print(name, email)
# TODO destop, zona de apelare a functiei
# apelarea functiei fara functiei
if __name__ == '__main__':  # tot ce e scris mai jos, e functional doar de aici, nu din alt fisier: ex.functii2
    sign_up_fara_parametri()
    sign_up_fara_parametri()
print('------------------------------')

# TODO 2.  functie cu parametri
# parametri si parametri arbitrali(optional): (*args, **work). un '*args => tuple; ** => dict
# parametri pozitionali:name, email, passport; parametri default:is_regist; si param arbirtral:*, **
# functia are nevoie totdeauna de 4 parametri, restul cumva ii ignora
def sign_up(name, email, passport, is_register=False, *home_details, **work_details):  # parametram
    print(work_details['street'])
    print(work_details['hause_nr'])
    print(work_details['city'])
    if is_register:
        print('You already have an acount')
    else:
        print('Please enter name, email, password...')
        for h in home_details:
            print(h)
    print(name, email)
    print(passport, is_register)
# 2a. apelarea functiei cu parametri
#     dupa 4 parametri,
if __name__ == '__main__':
    sign_up('ION', 'ion@email.com', 'abcd', is_register=True,
            street='rue de paris', hause_nr=20, city='paris')
    sign_up('MARIA', 'marian@email.com', 'xywz', False,
            'calea doro', 70, 'copsa mica', street='rue de vulpe', hause_nr=22, city='ile')
print('--------------------------')

def get_user(*address):
    # print(address[0])
    for a in address:
        print(a)
if __name__ == '__main__':
    get_user('calea constantei', 'str. timisului', 'str. xyz')
print('----------------------------------')

def get_max_score(students):
    max_g = 0
    students = [{'name': 'ion', 'grade': 5}, {'name': 'maria', 'grade': 7}]
    for s in students:
        for n, g in s.items():  # items  - return lista cu toate cheile din dict
            if n == 'grade':
                print(n, g)
                if g > max_g:
                    max_g = g
    return max_g
print(get_max_score(' '))

# print('Hello', end='***') # printeaza pe aceeasi linie un separator intre 2 mesaje
# print('Hello', 'world', 'Hello world John', sep='@') # separate prin @
# print('Hello', 'world', 'Hello world John') # printeaza fara separator





