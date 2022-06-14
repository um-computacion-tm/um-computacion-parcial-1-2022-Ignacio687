from invalidassignmentexception import InvalidAssignmentException

class Hangman():
    def __init__(self):
        self.word = []
        self.lifes = 5
        self.displeyWord = []

    def set_word(self, word):
        self.word = [letter for letter in word.lower()]
        self.displeyWord = ['_ ' for letter in self.word]

    def show(self):
        displeyWordString = ''.join(self.displeyWord)
        return f'Lifes: {self.lifes} - Word: {displeyWordString}'

    def assign(self, letter):
        letter = letter.lower()
        if letter in self.word:
            indexStart = -1
            for letterCounter in self.word:
                indexStart +=1
                if letter == letterCounter:
                    self.displeyWord[self.word.index(letter, indexStart)] = letter+' '
        else: 
            self.lifes -=1
            raise InvalidAssignmentException

    def winner(self):
        return False if '_ ' in self.displeyWord else True