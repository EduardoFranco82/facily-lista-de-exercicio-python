 '''Implemente a classe Funcionário com um nome e um salário.
Escreva um construtor com dois parâmetros (nome e salário) e métodos
para devolver nome e salário. Crie o método aumentar_salario(percentual_aumento)
que aumente o salário do funcionário em uma certa porcentagem. Escreva um pequeno
 programa que teste sua classe. '''

class Funcionário:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario =salario
    def __str__(self) -> str:
        print(20*'-')
        return f"nome: {self.nome} salario: {self.salario}"
    def aumentar_salario(self,percentual_aumento):
        aumento = self.salario*(percentual_aumento/100)
        self.salario += aumento
        return self.salario

    funcionario1 = Funcionário('edu',2000.00)
    print(funcionario1)
    funcionario1.aumentar_salario(100)
    print(funcionario1)