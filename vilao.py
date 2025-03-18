
from personagem import Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, ataque, defesa, maldade):
        super().__init__(nome, idade, vida, ataque, defesa)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade

    def ataque_especial(self, personagem):
        """
        Um ataque especial que causa dano adicional baseado no nível de maldade.
        """
        dano_extra = {'Baixa': 5, 'Média': 10, 'Alta': 20}[self.maldade]
        dano_total = self.ataque + dano_extra
        print(f'{self.nome} usou um ataque especial! Dano: {dano_total}')
        personagem.downgrade_vida(dano_total)

    def acao_automatica(self, heroi):
        """
        O vilão realiza uma ação automática durante seu turno.
        """
        from random import choice
        acoes = [self.ataque_especial, self.defender]
        acao = choice(acoes)
        if acao == self.defender:
            acao()
        else:
            acao(heroi)

    def defender(self):
        """
        O vilão se defende, aumentando temporariamente sua defesa.
        """
        self.defesa += 10
        print(f'{self.nome} está defendendo! Defesa aumentada para {self.defesa}')

    def __str__(self):
        return (f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, '
                f'Ataque: {self.ataque}, Defesa: {self.defesa}, Maldade: {self.maldade}')
