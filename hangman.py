
class Hangman():
    def __init__(self):
        self.word = []
        self.lifes = 5
        self.displeyWord = []

    def set_word(self, word):
        self.word = [letter for letter in word]
        self.displeyWord = ['_ ' for letter in self.word]

    def show(self):
        displeyWordString = ''.join(self.displeyWord)
        return f'Lifes: {self.lifes} - Word: {displeyWordString}'

    