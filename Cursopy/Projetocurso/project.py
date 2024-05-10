from random import randint


class Dados:
    def __init__(self, faces: int) -> None:
        self.faces = faces

    def jogar_dado(self) -> int:
        return randint(1, self.faces)

    def mudar_faces(self, faces) -> None:
        self.faces = faces


class Player:
    def __init__(self, nome: str, dado: Dados) -> None:
        self.nome = nome
        self.dado = dado
        self.ponto = 0

    def jogar_dado(self) -> int:
        face = self.dado.jogar_dado()
        return face

    def get_ponto(self) -> int:
        return self.ponto

    def set_ponto(self, novo_ponto) -> None:
        self.ponto += novo_ponto


class Battle:
    def __init__(self, player1: Player, player2: Player, numero_round: int) -> None:
        self.player1 = player1
        self.player2 = player2
        self.numero_round = numero_round

    def inicar_batalha(self):
        i = 0
        while i < self.numero_round:
            ponto_jogador1 = self.player1.jogar_dado()
            ponto_jogador2 = self.player2.jogar_dado()

            self.player1.set_ponto(ponto_jogador1)
            self.player2.set_ponto(ponto_jogador2)

            print(f'round: {i}')
            self.mostrar_resultado()

            i += 1

    def mostrar_resultado(self) -> None:
        print(f'Jogador {self.player1.nome} tem {self.player1.get_ponto()}')
        print(f'Jogador {self.player2.nome} tem {self.player2.get_ponto()}')


dado_round = Dados(6)

dado_jogador1 = Dados(8)
dado_jogador2 = Dados(12)

cleverson = Player("cleverson", dado_jogador1)
talles = Player("talles", dado_jogador2)

batalha = Battle(cleverson, talles, dado_round.jogar_dado())

batalha.inicar_batalha()

