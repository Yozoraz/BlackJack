import random

koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(koloda)


class Player:
    score = 0
    current = 0
    choice = input(' start y/n?\n')


player1 = Player()
player2 = Player()


def Game():
    while True:
        while player1.choice == 'y':
            player1.choice = input('Игрок 1 ходит\n')
            if player1.choice == 'y':
                player1.current = koloda.pop()
                print('Вам попалась карта %d\n' % player1.current)
                player1.score += player1.current
                print('У вас %d очков\n' % player1.score)
            elif player1.choice == 'n':
                print('У вас %d очков\n' % player1.score)
                break
        while player2.choice == 'y':
            player2.choice = input('Игрок 2 ходит\n')
            if player2.choice == 'y':
                player2.current = koloda.pop()
                print('Вам попалась карта %d\n' % player2.current)
                player2.score += player2.current
                print('У вас %d очков\n' % player2.score)
            elif player2.choice == 'n':
                print('У вас %d очков\n' % player2.score)
                break
        break
    return player1.score, player2.score


a, b =Game()


def Winner(score, score2):
    while True:
        if player1.score == player2.score:
            print('нет победителя! У двух игроков одинаковый счёт')
            break
        else:
            while player1.score or player2.score > 21:
                if player1.score >21 and player2.score > 21:
                    print('Нет победителя! У двух игроков перебор')
                    break
                elif player1.score > 21:
                    print('Игрок 2 победил')
                    break
                elif player2.score > 21:
                    print('Игрок 1 победил')
                    break
                break
            while player1.score or player2.score == 21:
                if player1.score == 21:
                    print('Игрок 1 победил')
                    break
                elif player1.score == 21:
                    print('Игрок 2 победил')
                    break
                break
            while player1.score < 21 and player2.score < 21:
                if player1.score > player2.score:
                    print('Игрок 1 победил')
                    break
                elif player2.score > player1.score:
                    print('Игрок 2 победил')
                    break
                break
            break


print('У первого игрока %d очков\n'%player1.score,'У второго игрока %d очков\n' %player2.score)
c = Winner(a,b)

