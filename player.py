"""
This is the player Class
"""

class Player :
    
    def ___init___(self) :
        self.name = ''
        self.symbol = ''
        self.spaces = []
        self.wins = 0


    def get_name(self) :
        return input("Please enter your name: ")
    
    def get_symbol(self) :
        return input(f"What will {self.name}'s symbol be? (X or O): ")

    def get_info(self) :
        self.name = self.get_name()
        self.symbol = self.get_symbol()