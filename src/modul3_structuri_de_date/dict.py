my_dict = {
    'animal': 'pisica',
    123: 'acesta este un numar',
    True: [
        {
            'user': 'go',
            'parola': 'david',
        },
        {'user': 'ion',
         'parola': 'marcel',
         }
    ],
    52.2: 'latitudinea romaniei'
}
my_dict_2 = dict(string='pisica', numbers='thisisanumber',
                 myboolean=[dict(user='go', parola='david'), dict(user='ion', parola='marcel')],
                 parole={
                     1: 1,
                     True: 'yes',
                 })
print(my_dict[True][1]['parola'])
my_dict['email'] = 'gmail@gmail.com'
print(my_dict)
my_dict['email'] = 'gmail@yahoo.com'
print(my_dict)
del my_dict['email'] # sterge emailul
print(my_dict)
# TODO SA MAI FACEM ALTE METODE
print('TODO')
print(my_dict.items())
