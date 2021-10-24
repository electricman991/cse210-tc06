from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    Attributes:
        board (Board): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        guess (Guess): An instance of the class of objects known as Guess.
        roster (Roster): An instance of the class of objects known as Roster.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """        
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._roster = Roster()
        self.hint = (    "x = correct number in the correct place\n"
                         "o = correct number but incorrect position\n"
                         "* = incorrect number\n"
                         )


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        
        self._console.write(self.hint)

        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            self._board.prepare(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the guess from the current player.
        Args:
            self (Director): An instance of Director.
        """
        # Display Game Board
        board = self._board.to_string()
        self._console.write(board)

        # Get Players next guess
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        player_guess = str(self._console.read_number(("What is your guess? ")))
        guess = Guess(player_guess)
        player.set_guess(guess)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current guess.
        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        guess = player.get_guess()
        #self._console.write(self.hint_key)
        self._board.current_guess(player, guess)

    def _do_outputs(self):
        """
        The _do_outputs will determine and display the winner.
        Args:
            self (Director): An instance of Director.
        """
        if self._board.check_hint(self._roster.get_current()):
            current_player = self._roster.get_current()
            name = current_player.get_name()
            self._console.write(f"\nCongratulations {name.upper()}!  You have won the game!")
            self._keep_playing = False

        self._roster.next_player()