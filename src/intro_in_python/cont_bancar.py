class ContBancar:
    # constructor
    def __init__(self, titularCont, iban):
        # atribute, fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    # metode
    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr de incercari {self.incercari_activare}')
        print('------------------------------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat')
            self.activ = True
        else:
            print('Pin gresit')
            self.incercari_activare = self.incercari_activare + 1
            # self.incercari_activare+=1

    def alimentareCont(self, suma):
        self.salut()
        self.sold += suma
        print(f'Ati alimentat {suma}')
        print(f'Aveti in cont {self.sold}')

    def plataCard(self, suma):   # nu se poate defini o metoda in alta (ex.suma), dar
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente')

    def salut(self):   # se poate apela o metoda in alta metoda
        print(f'Buna {self.titularCont}')

