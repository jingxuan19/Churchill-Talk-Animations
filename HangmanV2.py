from english_words import get_english_words_set
from wordfreq import word_frequency
import numpy as np
import string
import itertools
from matplotlib import pyplot as plt
import json


class Hangmanv2:
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

    def probabilitywordfreq(self, samplespace):
        if len(samplespace) == 0:
            return {}
        wordfreqprobs = {}
        for word in samplespace:
            p = word_frequency(word, "en")
            if p == 0:
                p = 10 ** (-9)
            wordfreqprobs[word] = p
        normalise = 1.0 / sum(wordfreqprobs.values())
        for word in wordfreqprobs.keys():
            wordfreqprobs[word] = wordfreqprobs[word] * normalise

        return wordfreqprobs

    def entropycalc(self, probabilities):
        if probabilities == {}:
            return 0
        entropy = 0
        for key in probabilities.keys():
            p = probabilities[key]
            if p != 0:
                entropy -= p * np.log2(p)
        return entropy

    def makeguess(self, answer, potentialletters, samplespace, wordprobabilities):
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

                probability = 0
                for word in possiblewords:
                    probability += wordprobabilities[word]

                if probability != 0:
                    letterentropy[letter] -= probability * np.log2(probability)

                print(probability)

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
        potentialletters = self.letters.copy()

        wordprobabilities = self.probabilitywordfreq(samplespace)

        print("Possible words:", len(samplespace))

        uncertainty = self.entropycalc(wordprobabilities)
        print("Uncertainty:", uncertainty, "bits")

        wordprobabilities = dict(sorted(wordprobabilities.items(), reverse=True, key=lambda item: item[1]))
        print(wordprobabilities)

        guess = self.makeguess(answer, potentialletters, samplespace, wordprobabilities)

        print("Guess:", guess, "Entropy:", self.entropy[guess])

        self.showentropy(self.entropy)

        with open("hangmanv2" + str(letters) + ".json", "w") as outfile:
            json.dump(self.entropy, outfile)

        return self.entropy

    def game(self, letters):
        samplespace = np.array(list(self.web2lowerset))
        samplespace = samplespace[np.vectorize(len)(samplespace) == letters].tolist()
        answer = [' '] * letters
        potentialletters = self.letters.copy()

        guesscount = 0

        wordprobabilities = self.probabilitywordfreq(samplespace)

        while ' ' in answer:
            print("Possible words:", len(samplespace))
            print(samplespace)

            uncertainty = self.entropycalc(wordprobabilities)
            print("Entropy:", uncertainty, "bits")

            wordprobabilities = dict(sorted(wordprobabilities.items(), reverse=True, key=lambda item: item[1]))
            print(wordprobabilities)
            if guesscount == 0:
                try:
                    with open('hangmanv2' + str(letters) + '.json') as json_file:
                        fm = json.load(json_file)
                    self.entropy = fm
                    guess = max(fm, key=fm.get)
                except:
                    guess = self.makeguess(answer, potentialletters, samplespace, wordprobabilities)
            elif guesscount == 1:
                try:
                    with open('hangmanv2' + str(letters) + 'guess2' + '.json') as json_file:
                        fm = json.load(json_file)
                    self.entropy = fm
                    guess = max(fm, key=fm.get)
                except:
                    guess = self.makeguess(answer, potentialletters, samplespace, wordprobabilities)
            else:
                guess = self.makeguess(answer, potentialletters, samplespace, wordprobabilities)

            print("Guess", guess)
            try:
                print("Entropy:", self.entropy[guess])
            except:
                pass
            guesscount += 1

            potentialletters.remove(guess)
            self.showentropy(self.entropy)

            if len(samplespace) <= 100:
                self.showentropy(wordprobabilities)

            # Good correlation, but not generalisable, as considers/ does not consider multiple letters in the same word as a response
            # self.lettercounter(samplespace)
            # self.showentropy(self.lettercount)

            newanswer = list(input())
            while len(newanswer) != letters:
                print("Whoops, not enough characters!")
                newanswer = list(input())
            if newanswer == answer:
                samplespace = self.filter(None, guess, samplespace)
            else:
                answer = newanswer
                samplespace = self.filter(answer, None, samplespace)

            tempprob = 0
            for word in samplespace:
                tempprob += wordprobabilities[word]

            infogained = -np.log2(tempprob)
            # H(S) = H(p_f, 1-p_f) + p_fH(S') + (1-p_f)H(\S')
            wordprobabilities = self.probabilitywordfreq(samplespace)

            print("Information gained:", infogained, "bits")

            if len(samplespace) == 1:
                print(samplespace[0])
                answer = ''
                guesscount += 1

        return guesscount