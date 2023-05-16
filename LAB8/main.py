from abc import ABC, abstractmethod


class FrequencyCounter(ABC):
    address = ""

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(FrequencyCounter):

    def calculateFreqs(self):

        initLetters = []
        FrqLetters = []
        letters = []

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        letters.append(char.lower())

        uniqLetters = set(letters)

        for letter in uniqLetters:
            frequency = letters.count(letter)
            initLetters.append(letter)
            FrqLetters.append(letter + " = " + str(frequency))

        print("List =", initLetters)
        print("Resulting List =", FrqLetters)


class DictCount(FrequencyCounter):

    def calculateFreqs(self):

        initlLetters = {}
        FrqLetters = {}

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        char = char.lower()
                        initlLetters[char] = initlLetters.get(char, 0)
                        FrqLetters[char] = FrqLetters.get(char, 0) + 1

        print("Dict =", initlLetters)
        print("Updated Dict =", FrqLetters)


listCounter = ListCount("weirdWords.txt")
listCounter.calculateFreqs()

dictCounter = DictCount("weirdWords.txt")
dictCounter.calculateFreqs()
