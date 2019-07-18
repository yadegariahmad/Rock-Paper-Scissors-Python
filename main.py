import sys


class Main:
    PlayerOne = {
        'Name': None,
        'Score': 0
    }

    PlayerTwo = {
        'Name': None,
        'Score': 0
    }

    def __init__(self):
        print('Player One:\n')
        self.getPlayerInfo(self.PlayerOne)

        print('Player Two:\n')
        self.getPlayerInfo(self.PlayerTwo)

        self.play()

    def getPlayerInfo(self, player):
        print('Please enter your name:')
        player['Name'] = input()

    def play(self):
        print('{} make your move. (r,p,s)\n'.format(self.PlayerOne['Name']))
        playerOneMove = input().lower()

        print('{} make your move. (r,p,s)\n'.format(self.PlayerTwo['Name']))
        playerTwoMove = input().lower()

        self.checkWinner(playerOneMove, playerTwoMove)
        self.showScores()
        self.repeat()

    def checkWinner(self, p1Move, p2Move):
        if (
            (p1Move == 'r' and p2Move == 's') or
            (p1Move == 's' and p2Move == 'p') or
            (p1Move == 'p' and p2Move == 'r')
        ):
            print('Winner is {}'.format(self.PlayerOne['Name']))
            self.PlayerOne['Score'] += 1
        elif (
            (p2Move == 'r' and p1Move == 's') or
            (p2Move == 's' and p1Move == 'p') or
            (p2Move == 'p' and p1Move == 'r')
        ):
            print('Winner is {}'.format(self.PlayerTwo['Name']))
            self.PlayerTwo['Score'] += 1
        elif p1Move == p2Move:
            print('Draw')

    def showScores(self):
        print('{Name} score is {Score}'.format(**self.PlayerOne))
        print('{Name} score is {Score}'.format(**self.PlayerTwo))

    def repeat(self):
        print(
            '{} do you wanna play again? (y/n)'.format(self.PlayerOne['Name'])
        )
        p1Answer = input().lower()

        print(
            '{} do you wanna play again? (y/n)'.format(self.PlayerTwo['Name'])
        )
        p2Answer = input().lower()

        if p1Answer == 'y' and p2Answer == 'y':
            self.play()
        else:
            print('Thank you.')
            sys.exit()


Main()
