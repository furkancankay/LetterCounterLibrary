class LetterCounter:
    def __init__(self,text):
        self.text = text
        self.vowelsCounter = 0
        self.consonantsCounter = 0
        self.numbersCounter = 0
        self.charactersCounter = 0
        self.vowels = "aeiouAEIOU"
        self.consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        self.numbers = "0123456789"
    def run(self):
        for letter in text:
            if letter in self.vowels:
                self.vowelsCounter += 1
            elif letter in self.consonants:
                self.consonantsCounter += 1
            elif letter in self.numbers:
                self.numbersCounter += 1
            else:
                self.charactersCounter += 1
        print(self.vowelsCounter      ,'vowel,'     )
        print(self.consonantsCounter  ,'consonant,' )
        print(self.numbersCounter     ,'number,'    )
        print(self.charactersCounter  ,'character.' )

    def get_vowel_count(self):
        for letter in text:
            if letter in self.vowels:
                self.vowelsCounter += 1
        print('\n',self.vowelsCounter)

    def get_consonant_count(self):
        for letter in text:
            if letter in self.consonants:
                self.consonantsCounter += 1 
        print('\n',self.consonantsCounter )

    def get_number_count(self):
        for letter in text:
            if letter in self.numbers:
                self.numbersCounter += 1
        print('\n',self.numbersCounter)

    def get_character_count(self):
        for letter in text:
            if ((letter in self.numbers) or (letter in self.consonants) or (letter in self.vowels)) == 0:
                self.charactersCounter += 1
        print('\n',self.charactersCounter)

if __name__ == "__main__":
    while True:
        esc = input("To continue press any button except 'e'")
        if(esc == 'e'):
            break
        print('''
o ============== o ============= o
To show vowel letters press:     1
To show consonant letters press: 2
To show how much number press:   3
To show how much char. press:    4
To show all of them press:       5
To exit press:            Anything
o ============== o ============= o
        ''')
        choice = input(': ')
        text = input("Enter your word: ")
        if(choice == '1'):
            Start = LetterCounter(text).get_vowel_count()
        elif(choice == '2'):
            Start = LetterCounter(text).get_consonant_count()
        elif(choice == '3'):
            Start = LetterCounter(text).get_number_count()
        elif(choice == '4'):
            Start = LetterCounter(text).get_character_count()
        elif(choice == '5'):
            Start = LetterCounter(text).run()
        else:
            break
