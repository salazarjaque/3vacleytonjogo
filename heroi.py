
from personagem import Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, ataque, defesa, habilidade_especial):
        super().__init__(nome, idade, vida, ataque, defesa)
        self.habilidade_especial = habilidade_especial

    def salvar_refem(self):
        """
        O herói salva um refém, ganhando pontos de vida.
        """
        self.vida += 20
        print(f'{self.nome} salvou um refém e ganhou 20 pontos de vida! Vida atual: {self.vida}')

    def usar_habilidade_especial(self, personagem):
        """
        Usa a habilidade especial do herói.
        """
        dano = self.ataque * 2
        print(f'{self.nome} usou {self.habilidade_especial}! Dano: {dano}')
        personagem.downgrade_vida(dano)

    def defender(self):
        """
        O herói se defende, aumentando temporariamente sua defesa.
        """
        self.defesa += 10
        print(f'{self.nome} está defendendo! Defesa aumentada para {self.defesa}')

    def __str__(self):
        return (f'Herói: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, '
                f'Ataque: {self.ataque}, Defesa: {self.defesa}, '
                f'Habilidade Especial: {self.habilidade_especial}')