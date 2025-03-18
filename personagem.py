
class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, idade, vida, ataque, defesa):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.habilidades = []
        self.itens = []

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem.
        """
        self.vida += incremento
        print(f'{self.nome} ganhou {incremento} pontos de vida! Vida atual: {self.vida}')

    def downgrade_vida(self, dano):
        """
        Reduz a vida do personagem, considerando a defesa.
        """
        dano_final = max(0, dano - self.defesa)
        self.vida = max(0, self.vida - dano_final)
        print(f'{self.nome} sofreu {dano_final} de dano! Vida atual: {self.vida}')

    def adicionar_habilidade(self, habilidade):
        """
        Adiciona uma habilidade ao personagem.
        """
        self.habilidades.append(habilidade)
        print(f'{self.nome} aprendeu a habilidade: {habilidade}')

    def adicionar_item(self, item):
        """
        Adiciona um item ao inventário do personagem.
        """
        self.itens.append(item)
        print(f'{self.nome} adquiriu o item: {item}')

    def usar_item(self, item):
        """
        Usa um item do inventário.
        """
        if item in self.itens:
            self.itens.remove(item)
            print(f'{self.nome} usou o item: {item}')
        else:
            print(f'{self.nome} não possui o item: {item}')

    def dialogar(self, mensagem):
        """
        Exibe uma mensagem de diálogo do personagem.
        """
        print(f'{self.nome} diz: {mensagem}')

    def __str__(self):
        return (f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, '
                f'Ataque: {self.ataque}, Defesa: {self.defesa}, '
                f'Habilidades: {self.habilidades}, Itens: {self.itens}')