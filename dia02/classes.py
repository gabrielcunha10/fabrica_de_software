class cachorro:
    def __init__(self,nome,raca,idade,peso):
        self.raca = raca
        self.nome = nome
        self.idade = idade
        self.peso = peso
    def latir(self):
        print(f"Meu nome é {self.nome}")
dog = cachorro("Bob","Vira-lata",10,25)
dog.latir()