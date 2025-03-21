class A:
    def uno(self):
        print('Estoy en uno')
        self.dos()  # Llamar al método dos sobre la instancia  self

    def dos(self):
        print('Estoy en dos')
