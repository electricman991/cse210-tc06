import random

class Board:
    """
     A board is defined as a designated playing surface. The
     responsibility of Board is to keep track of the pieces in play.
    """
    def __init__(self):
        """
        The constructor declares and initializes instance attributes with
        their default values. It also invokes the private _prepare method
        """
        self._items = {}  

    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.
        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.
        Returns:
            string: A hint in the form [xxxx]
        """ 

        hint = ""
         
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint  

    def to_string(self):
        """
        The to_string method converts the board data to its
        string representation and returns it to the caller.
        Args:
            self(Board): an instance of Board
        """
        text = "\n-------------------------\n"
        for key, value in self._items.items():
            text += f"Player {key}: {value[1]}, {value[2]}\n"
        text += "-------------------------\n"
        return str(text)    

    def current_guess(self, player, guess):
        """
        The current_guess updates the board with the current guess.
        Args:
            self (Board): an instance of Board.
            guess (Guess): The current guess of the player.
            player (Player): The player whose guess is updated.
        """
        items = self._items[player.get_name()]
        items[1] = guess.get_guess()
        items[2] = self._create_hint(items[0], guess.get_guess())
        self._items[player.get_name()] = items

    def check_hint(self, player):
        """
        The check_hint checks if there are no "x" in the hint.
        Args:
            self (Board): an instance of a Board
            player (Player): the player whose hint is checked
        Returns: true if there are no "x" in the hint
        """
        hint = self._items[player.get_name()][2]

        if hint != "":
            for character in hint:
                if character != "x":
                    return False
            return True

        return False