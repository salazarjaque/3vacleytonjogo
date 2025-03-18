# coisar o main
from personagem import Personagem
from vilao import Vilao
from heroi import Heroi
from utils import mostrar_mensagem, mostrar_status, registrar_acao, mostrar_historico

def escolher_acao(heroi, vilao):
    """
    Permite ao jogador escolher uma ação para o herói.
    """
    while True:
        print("\nEscolha uma ação:")
        print("1. Atacar")
        print("2. Defender")
        print("3. Usar Habilidade Especial")
        print("4. Usar Item")
        escolha = input("Digite o número da ação: ")

        if escolha == "1":
            heroi.usar_habilidade_especial(vilao)
            registrar_acao(f'{heroi.nome} atacou {vilao.nome}!')
            break
        elif escolha == "2":
            heroi.defender()
            registrar_acao(f'{heroi.nome} está defendendo!')
            break
        elif escolha == "3":
            heroi.usar_habilidade_especial(vilao)
            registrar_acao(f'{heroi.nome} usou {heroi.habilidade_especial}!')
            break
        elif escolha == "4":
            if heroi.itens:
                print("Itens disponíveis:", heroi.itens)
                item = input("Digite o nome do item que deseja usar: ")
                heroi.usar_item(item)
                registrar_acao(f'{heroi.nome} usou o item: {item}')
            else:
                print("Você não tem itens para usar!")
            break
        else:
            print("Escolha inválida. Tente novamente.")

def batalha(heroi, vilao):
    """
    Simula uma batalha por turnos entre um herói e um vilão.
    """
    mostrar_mensagem(f'Batalha entre {heroi.nome} e {vilao.nome}!')
    turno = 1
    while heroi.vida > 0 and vilao.vida > 0:
        print(f'\n=== Turno {turno} ===')
        mostrar_status(heroi)
        mostrar_status(vilao)

        # turno do herói
        print(f'\nTurno de {heroi.nome}:')
        escolher_acao(heroi, vilao)

        # Ve se o vilão foi derrotado
        if vilao.vida <= 0:
            break

        # turno do vilão
        print(f'\nTurno de {vilao.nome}:')
        vilao.acao_automatica(heroi)

        # Ve se o herói foi derrotado
        if heroi.vida <= 0:
            break

        turno += 1

    if heroi.vida > 0:
        mostrar_mensagem(f'{heroi.nome} venceu a batalha!')
        registrar_acao(f'{heroi.nome} venceu a batalha contra {vilao.nome}!')
    else:
        mostrar_mensagem(f'{vilao.nome} venceu a batalha!')
        registrar_acao(f'{vilao.nome} venceu a batalha contra {heroi.nome}!')

def main():
    # Cria personagens
    heroi = Heroi('Link', 30, 100, 20, 10, 'Espada da Luz')
    vilao = Vilao('Ganon', 45, 120, 25, 5, 'Alta')

    # habilidades e itens
    heroi.adicionar_habilidade('Ataque Rápido')
    heroi.adicionar_item('Poção de Cura')
    vilao.adicionar_habilidade('Sopro de Fogo')
    vilao.adicionar_item('Pedra da Escuridão')

    #inicia a batalha
    batalha(heroi, vilao)

    #mostra o histórico de ações
    mostrar_historico()

if __name__ == "__main__":
    main()