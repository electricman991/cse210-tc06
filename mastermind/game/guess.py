class Guess:
    """A maneuver in the game. The responsibility of Guess is to keep track of the players guesses.
    
    Stereotype: 
        Information Holder
    Attributes:
        _guess (integer): The number guessed by current user.
        
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
            guess
        """
        self._guess = guess

    def get_guess(self):
        """Returns the number that the player guesses.
        Args:
            self (Guess): an instance of Guess.
        """
        return self._guess