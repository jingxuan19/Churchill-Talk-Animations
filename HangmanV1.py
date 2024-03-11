from english_words import get_english_words_set
import numpy as np
import string
import itertools
from matplotlib import pyplot as plt
import json


class Hangmanv1:
    web2lowerset = get_english_words_set(['web2'], lower=True)
    letters = list(string.ascii_lowercase)
    entropy = {}

    lettercount = {}

    def lettercounter(self, samplespace):
        for letter in self.letters:
            self.lettercount[letter] = 0

        for word in samplespace:
            for letter in word:
                self.lettercount[letter] += 1

    def __init__(self):
        return

    def filter(self, answer, banned, samplespace):
        possiblespace = samplespace.copy()
        for word in samplespace:
            if answer == None:
                if banned in word:
                    possiblespace.remove(word)
            else:
                letters = []
                for c in answer:
                    if c != ' ':
                        letters.append(c)

                for i in range(len(answer)):
                    if answer[i] != ' ':
                        if answer[i] != word[i]:
                            possiblespace.remove(word)
                            break
                    else:
                        if word[i] in letters:
                            possiblespace.remove(word)
                            break

        return possiblespace

    def information(self, possiblespace, samplespace):
        p = len(possiblespace) / len(samplespace)
        if p == 0:
            return 0
        return -p * np.log2(p)

    def makeguess(self, answer, potentialletters, samplespace):
        holes = answer.count(' ')

        letterentropy = {}
        for letter in self.letters:
            letterentropy[letter] = 0

        for letter in potentialletters:
            possibleresponses = itertools.product([letter, ' '], repeat=holes)
            for response in possibleresponses:
                print(response, end=" ")
                potentialanswer = answer.copy()
                response = list(response)
                if letter not in response:
                    possiblewords = self.filter(None, letter, samplespace)
                else:
                    for i in range(len(potentialanswer)):
                        if potentialanswer[i] == ' ':
                            potentialanswer[i] = response.pop(0)
                    possiblewords = self.filter(potentialanswer, None, samplespace)

                letterentropy[letter] += self.information(possiblewords, samplespace)
                print(len(possiblewords))

        self.entropy = letterentropy

        return max(letterentropy, key=letterentropy.get)

    def showentropy(self, df):
        plt.figure(figsize=(20, 8))

        ax = plt.axes()
        ax.bar(df.keys(), df.values())

        for key in df.keys():
            plt.text(key, df[key], round(df[key], 2))

        plt.show()

    def firstguess(self, letters):
        samplespace = np.array(list(self.web2lowerset))
        samplespace = samplespace[np.vectorize(len)(samplespace) == letters].tolist()
        answer = [' '] * letters

        print("Possible words:", len(samplespace))

        guess = self.makeguess(answer, self.letters, samplespace)
        print(guess)
        print("Entropy:", self.entropy[guess])

        self.showentropy(self.entropy)

        with open("hangman" + str(letters) + ".json", "w") as outfile:
            json.dump(self.entropy, outfile)

        return self.entropy

    def game(self, letters):
        samplespace = np.array(list(self.web2lowerset))
        samplespace = samplespace[np.vectorize(len)(samplespace) == letters].tolist()
        answer = [' '] * letters
        potentialletters = self.letters.copy()

        guesscount = 0

        while ' ' in answer:
            print("Possible words:", len(samplespace))
            uncertainty = -np.log2(1 / len(samplespace))  # shorthand, not generalisable
            print("Entropy:", uncertainty, "bits")
            print(samplespace)
            if guesscount == 0:
                try:
                    with open('hangman' + str(letters) + '.json') as json_file:
                        fm = json.load(json_file)
                    self.entropy = fm
                    guess = max(fm, key=fm.get)
                except:
                    if letters <= 5:
                        guess = self.makeguess(answer, potentialletters, samplespace)
                    else:
                        guess = 'e'
            else:
                guess = self.makeguess(answer, potentialletters, samplespace)
            print("Guess", guess)
            try:
                print("Entropy:", self.entropy[guess])
            except:
                pass
            guesscount += 1

            potentialletters.remove(guess)
            self.showentropy(self.entropy)

            # Good correlation, but not generalisable, as considers/ does not consider multiple letters in the same word as a response
            # self.lettercounter(samplespace)
            # self.showentropy(self.lettercount)

            newanswer = list(input())
            while len(newanswer) != letters:
                print("Whoops, not enough characters!")
                newanswer = list(input())

            oldlen = len(samplespace)
            if newanswer == answer:
                samplespace = self.filter(None, guess, samplespace)
            else:
                answer = newanswer
                samplespace = self.filter(answer, None, samplespace)
            infogained = -np.log2(len(samplespace) / oldlen)
            print("Information gained:", infogained, "bits")

            if len(samplespace) == 1:
                print(samplespace[0])
                answer = ''
                guesscount += 1

        return guesscount