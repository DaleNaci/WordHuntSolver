from letter import Letter


class Word:
    def __init__(self):
        self.letters = []


    def add_letter(self, letter):
        self.letters.append(letter)


    def get_word(self):
        s = ""

        for lttr in self.letters:
            s += lttr.get_letter()

        return s
