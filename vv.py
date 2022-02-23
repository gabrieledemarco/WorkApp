import random
import time


class Player:
    '''
    The Player class includes things that every player has,
    which is name and hp (health points).
    '''

    def __init__(self, name: str, hp: int, strength: int) -> None:
        self.name = name
        self.hp = hp
        self.strength = strength


class UserPlayer(Player):
    '''
    UserPlayer inherits from Player, because it is a more specific
    type of Player. This type of Player is controlled by the user.
    '''

    def __init__(self, name: str) -> None:
        '''
        Construct a UserPlayer with the given name, and a set
        hp and strength. Also define mp for magic, a list
        of possible moves they can make, and an inventory
        dictionary of items they can use.
        '''

        super().__init__(name, 50, 10)  # assign attributes name, hp, strength

        self.mp = 50
        self.moves = ['attack', 'magic attack', 'defend']
        self.inventory = {'potion': 1, 'ether': 1}  # potion should restore hp, ether restores mp

    def attack(self, other: 'Player') -> None:
        '''
        Attack the Player <other> by calling that Player's take_hit method.
        The attack power is based on your own strength.
        '''

        other.take_hit(self.strength)

    def take_hit(self, strength: int) -> None:
        '''
        Lose some hp based on the <strength> given.
        Print message about how much hp you lost.
        '''

        power = random.randint(strength // 2, strength)
        print("{} was attacked, and lost {} hp.".format(self.name, power))
        self.hp = self.hp - power

    def magic_attack(self, other):
        pass

    def defend(self):
        pass

    def make_move(self, opponent: 'Player') -> None:
        '''
        Make a move based on user input.
        '''

        not_valid = True
        while not_valid:
            move = input("What move do you want to take? a: attack, m: magic, d: defend\n")
            not_valid = False
            if move == "a":
                self.attack(opponent)
            elif move == "m":
                self.magic_attack(opponent)
            elif move == "d":
                self.defend()
            else:
                print("Invalid input. Try again.")
                not_valid = True


class Monster(Player):
    '''
    Monster class represents a Computer controlled player.
    The make_move method is thus different for the Monster,
    where the move is randomly chosen based on a randomly
    generated number, rather than through user input.
    '''

    def make_move(self, opponent):
        move = self.moves[random.randint(0, len(self.moves) - 1)]
        if move == "basic attack":
            self.attack(opponent)
        elif move == "special attack":
            self.special_attack(opponent)


class BasicMonster(Monster):
    '''
    BasicMonster class represents a basic type of Monster.
    We inherit the make_move from the Monster class, and this
    BasicMonster only has those two moves, so we don't need
    to add the make_move method here again.
    '''

    def __init__(self) -> None:
        '''
        Construct a BasicMonster with a name, hp, strength
        and list of moves.
        '''

        super().__init__('Basic Monster', 50, 10)  # assign attributes name, hp, strength
        # the super call above uses the original Player class's init method

        self.moves = ['basic attack']

        # Question: What does the following code do?
        if self.hp < 25:
            self.moves.append = ['special attack']

    def attack(self, other: 'Player') -> None:
        '''
        Attack the Player <other> by calling that Player's take_hit method.
        The attack power is based on your own strength.
        '''

        other.take_hit(self.strength)

    def take_hit(self, strength: int) -> None:
        '''
        Lose some hp based on the <strength> given.
        Print message about how much hp you lost.
        '''

        power = random.randint(strength // 2, strength)
        print("{} was attacked, and lost {} hp.".format(self.name, power))
        self.hp = self.hp - power

    def special_attack(self, other):
        '''
        Attack the Player <other> with a special attack that exceeds
        your usual strength.
        '''

        power = random.randint(self.strength, self.strength * 2)
        other.take_hit(40)


class Game:

    def __init__(self, p1: 'Player', p2: 'Player') -> None:
        '''
        Construct a Game with the given players.
        '''
        self.players = (p1, p2)
        self.turn = 0  # keep track of whose turn it is out of the two players

    def whose_turn(self, count: int) -> 'Player':
        '''
        Return the Player whose turn it is.
        '''
        if count % 2 == 0:
            next_player = self.players[0]
        else:
            next_player = self.players[1]
        return next_player

    def play_game(self) -> None:
        '''
        Play the game, with each player taking turns making a move, until
        one player runs out of hp.
        '''

        # print out the starting state of the game
        print(self)
        print('------------')

        winner = None
        while not winner:
            if self.players[0].hp <= 0:
                winner = self.players[1]
            elif self.players[1].hp <= 0:
                winner = self.players[0]
            else:
                # if no one has won yet, play one turn of the game (one player makes one move)
                self.play_one_turn()

        print('And {} is the winner!!!'.format(winner.name))

    def play_one_turn(self) -> None:
        '''
        Play one turn of the game based on which player's turn it is.
        Print state of game that results from this turn.
        '''

        current_player = self.whose_turn(self.turn)  # get the Player whose turn it currently is
        other_player = self.whose_turn(self.turn - 1)  # get the other Player in the game

        print("{}'s TURN".format(current_player.name))

        # if the player is the computer, wait 2 seconds before
        # showing the player's move to make the gameflow feel more natural
        if isinstance(current_player, Monster):
            time.sleep(1)

        current_player.make_move(other_player)

        # print current state of game
        print(self)
        print('------------')

        self.turn += 1

    def __str__(self) -> str:
        '''
        Return string representation of state of game.
        '''

        return "Player 1 hp: {}, Player 2 hp: {}".format(self.players[0].hp, self.players[1].hp)


def main():
    """Prompt the user to configure and play the game."""

    name = input("What is p1's name? ")

    p1 = UserPlayer(name)  # make the first player a User at position (0,0)

    p2 = BasicMonster()

    g = Game(p1, p2)
    g.play_game()


if __name__ == '__main__':
    main()
