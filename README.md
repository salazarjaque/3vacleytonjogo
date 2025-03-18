# DESAFIO 🕹️ Improve This Game 🕹️

### Universidade Federal Rural de Pernambuco  
**Departamento de Estatística e Informática**  
**Bacharelado em Sistemas de Informação**  
**Disciplina: Princípios de Programação**

a classe Personagem foi expandida para incluir atributos como ataque, defesa, habilidades e itens
classe Heroi foi criada, herdando de Personagem, e ganhou métodos específicos como usar_habilidade_especial() e defender()
classe Vilao também foi aprimorada, com a adição de um método acao_automatica() que faz o vilão agir escolhendo entre atacar ou defender
o jogo agora funciona em turnos, onde o usuario escolhe ações para o herói (como atacar, defender, usar habilidades etc), e o vilão realiza ações automaticamente em seu turno.
A batalha continua até que a vida de um dos personagens (herói ou vilão) chegue a zero.
O código foi modularizado, com funções auxiliares no arquivo utils.py, o que facilita a manutenção e expansão do jogo

Heróis e vilões agora possuem habilidades especiais e itens para usarem nas batalha.
O jogador pode gerenciar o inventário do herói e escolher quando usar itens.
Mensagens interativas foram adicionadas para guiar o jogador.
O status dos personagens (vida, ataque, defesa) é exibido em cada turno.
Todas as ações realizadas durante a batalha são registradas e exibidas ao final do jogo.

inspirada em pokemom eu coloquei a batalha por turnos, onde o usuario controla um herói e enfrenta um vilão onde o usuario escolhe ações para o herói (como atacar, defender, usar habilidades ou itens), enquanto o vilão realiza ações automaticamente em seu turno usando random.
foram adicionados novos atributos e métodos nas classes Personagem, Heroi e Vilao, como ataque, defesa, habilidades e itens, permitindo que os personagens tenham mais opções durante a batalha. A função escolher_acao(heroi, vilao) foi criada para permitir que o jogador tome decisões em cada turno, enquanto o vilão usa a função acao_automatica(heroi) para realizar ações de forma automática. Além disso, um sistema de histórico de ações foi implementado para registrar todas as ações durante a batalha, exibindo-as ao final do jogo. A interface foi aprimorada com mensagens claras e interativas, e o status dos personagens (vida, ataque, defesa) é exibido em cada turno
