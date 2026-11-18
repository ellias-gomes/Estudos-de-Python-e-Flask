class Fila():
    def __init__(self):
        self.normal = []
        self.preferencial = []
        self.contador = 0

    def inserir(self, idade):
        if idade < 60:
            self.normal.append(idade)
        else:
            self.preferencial.append(idade)

    def remover(self):
        if len(self.preferencial) > 0:
            self.contador = self.contador + 1
            if self.contador == 3:
                self.contador = 0
                return self.normal.pop(0)
            else:
                return self.preferencial.pop(0)
        else:
            return self.normal.pop(0)

    def top(self):
        if len(self.preferencial) > 0:
            return self.preferencial[0]
        else:
            return self.normal[0]

    def empty(self):
        return not len(self.normal) > 0