# pasta q ele pediu
historico_acoes = []

def mostrar_mensagem(mensagem):
    """
    Exibe uma mensagem formatada para o jogador.
    """
    print(f'=== {mensagem} ===')

def mostrar_status(personagem):
    """
    Exibe o status de um personagem.
    """
    print(f'Status de {personagem.nome}: Vida = {personagem.vida}, Ataque = {personagem.ataque}, Defesa = {personagem.defesa}')

def registrar_acao(acao):
    """
    Registra uma ação no histórico do jogo.
    """
    historico_acoes.append(acao)

def mostrar_historico():
    """
    Exibe o histórico de ações do jogo.
    """
    print('=== Histórico de Ações ===')
    for acao in historico_acoes:
        print(acao)