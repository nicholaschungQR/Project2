class RockPaperScissors:
    def __init__(self, A, B) -> None:
        self.your_move = A
        self.my_move = B

    def __del__(self):
        pass

    def __str__(self):
        your_move_translated = {
            'A' : 'rock',
            'B' : 'paper',
            'C' : 'scissors'
        } .get(self.your_move)

        my_move_translated = {
            'X' : 'rock',
            'Y' : 'paper',
            'Z' : 'scissors'
        } .get(self.my_move)
        return f"{your_move_translated}, {my_move_translated}"
    
    def get_value(self):
        return {
            ### YOUR CODE HERE ###
        }.get(self.my_move)

    def calculate_score(self):
        ### YOUR CODE HERE ###
        return
    
# A Y
# B X
# C Z
first_turn = RockPaperScissors('A', 'Y')

print(first_turn)
score = RockPaperScissors.calculate_score(first_turn)