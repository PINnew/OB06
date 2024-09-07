import random

class Hero():  #Создания класса: Hero
    def __init__(self, name, health=100, attack_power=20):  #Создания атрибутов: name, health, attack_power
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):  #Создания метода
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f'{self.name} атакует {other.name} и наносит {damage} урона.')
        print(f'У {other.name} осталось {other.health} здоровья.')

    def is_alive(self):  #Создания метода
        return self.health > 0


class Game:  #Создания класса: Game
    def __init__(self, player_name):  #Создания атрибутов:
        self.player = Hero(player_name)
        self.computer = Hero('Компьютер')

    def start(self):  #Создания метода
        print(f'Игра начинается! {self.player.name} против {self.computer.name}!')
        turn = 0

        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)  #Ход игрока
            else:
                self.computer.attack(self.player)  #Ход игрока

            turn += 1

            if not self.player.is_alive():
                print(f'{self.player.name} был побеждён! Победил {self.computer.name}.')
                break
            elif not self.computer.is_alive():
                print(f'{self.computer.name} был побеждён! Победил {self.player.name}.')
                break


if __name__ == "__main__":
    player_name = input('Введите имя вашего героя: ')
    game = Game(player_name)
    game.start()
