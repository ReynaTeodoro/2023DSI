clientesBD = []

class Cliente:
    def __init__(self, dni, nombreCompleto, nroCelular):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular

    def getNombre(self):
        return self.nombreCompleto
    def __str__(self):
        return self.nombreCompleto
    

