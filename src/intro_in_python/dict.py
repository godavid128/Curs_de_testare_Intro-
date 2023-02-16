lista_goala = []
dict_gol = {}

# declarare si initializare un dict
note_elevi = {'Gigi': 10, 'Costel': 9, 'Ana': 10, 'Sebi': 7}

#adaugam elemente
note_elevi['Sebi'] = 7

#printam dictul
print(note_elevi)

# aflam elemente
print(note_elevi['Gigi'])
print(note_elevi.get('Gigi'))

#actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

#aflam dimensiunea
print(len(note_elevi))

# stergem valori
note_elevi.pop('Gigi')
print(note_elevi.get('Gigi', 'nu mai avem acest elev'))
print(note_elevi)

# returneaza doar cheile
print(note_elevi.keys())

notele = [1, 2, 4]
print(max(notele))

